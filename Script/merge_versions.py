import os
import sys
import shutil
import argparse
from filecmp import dircmp
from log_helper import logger


EXCLUDES = ["README.md", ".gitignore", ".git"]


class RecursiveDircmp:

    def __init__(self):
        """
        """
        self.right_only = []
        self.left_only = []

    def dir_equal(self, left, right):
        """
        Compare two directories recursively. Files in each directory are
        assumed to be equal if their names and contents are equal.
        :param left: First directory path
        :param right: Second directory path
        @return: True if the directory trees are the same and there were no errors
        while accessing the directories or files; False otherwise.
       """
        logger.info("Compare {} and {}".format(left, right))
        dirs_cmp = dircmp(left, right)
        ret = True
        if len(dirs_cmp.left_only) > 0 or len(dirs_cmp.right_only) > 0:
            self.left_only.extend([os.path.join(os.path.abspath(left), item) for item in dirs_cmp.left_only if item not in EXCLUDES])
            self.right_only.extend([os.path.join(os.path.abspath(right), item) for item in dirs_cmp.right_only])
            logger.debug("Append {} to left_only".format(dirs_cmp.left_only))
            logger.debug("Append {} to right_only".format(dirs_cmp.right_only))

        logger.debug("Common dirs: {}".format(dirs_cmp.common_dirs))
        for common_dir in dirs_cmp.common_dirs:
            inner_left = os.path.join(left, common_dir)
            inner_right = os.path.join(right, common_dir)
            if not self.dir_equal(inner_left, inner_right):
                ret = False
        return ret


def main():
    """
    :return: Exec return code
    """
    parser = argparse.ArgumentParser(description='Command-line interface')
    parser.add_argument('--old-version',
                        help='Old version of Virtualbox, which we want to update',
                        required=True)
    parser.add_argument('--new-version',
                        help='New  version of Virtualbox, where from we copy updates',
                        required=True)
    parser.add_argument('--git-repo',
                        help='Directory which contains Git repo to merge; old_version by default',
                        default=None,
                        required=False)
    parser.add_argument('--only-compare',
                        help='Only compare old and new versions; do not merge',
                        action='store_true',
                        default=False,
                        required=False)

    args = parser.parse_args()
    git_repo = args.old_version if args.git_repo is None else args.git_repo
    diff = RecursiveDircmp()
    diff.dir_equal(args.old_version, args.new_version)
    logger.info("Remove from the old version: {}".format(diff.left_only))
    logger.info("Added in new version: {}".format(diff.right_only))

    with open('remove_from_old.txt', 'w') as f:
        f.writelines(["{}\n".format(item) for item in diff.left_only])
    with open('added_to_new.txt', 'w') as f:
        f.writelines(["{}\n".format(item) for item in diff.right_only])

    if args.only_compare:
        return 0

    os.chdir(git_repo)
    logger.info("Change directory to Git repo %s" % git_repo)
    for remove_item in diff.left_only:
        os.system("git rm -rf {}".format(remove_item))
    shutil.copytree(args.new_version, args.old_version, dirs_exist_ok=True)
    logger.info("Adding new files to Git repo...")
    os.system("git add -A")
    logger.info("Adding new files complete")
            
    return 0


###########################################################################
if __name__ == '__main__':
    sys.exit(main())
