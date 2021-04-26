import os
import sys
import argparse
from log_helper import logger
from replace_content import REPLACE_CONTENT


# TODO: https://www.nltk.org/api/nltk.html
# TODO: https://github.com/seatgeek/fuzzywuzzy


def preview_string(fill_string, preview_len=20):
    """
    :param fill_string: Potentially long string
    :param preview_len: length of preview string without "..."
    :return: Shortened preview string, beginning of fill string and "..."
    """
    if len(fill_string) < preview_len:
        return fill_string.lstrip()

    return "%s..." % fill_string[0:preview_len].lstrip().rstrip()


def search_replace(file_content, find_str, replace_str):
    """
    :param file_content: file content; basically, a string where we perform search
    :param find_str: substring to find
    :param replace_str: string to put instead
    :return: pair (copy of 'file_content' with replaced strings, number of occurrences)
    """
    num_occurrences = file_content.count(find_str)
    file_content = file_content.replace(find_str, replace_str)
    return file_content, num_occurrences


def replace_infile(target_file, find_str, replace_str):
    """
    :param target_file: file name where to perform replace
    :param find_str: substring to find
    :param replace_str: string to put instead
    """
    # Read in the file
    logger.debug(f"Full path to the file: {target_file}")
    with open(target_file, 'r') as fr:
        file_content = fr.read()

    # Replace the target string
    file_content, num_occurrences = search_replace(file_content, find_str, replace_str)
    preview_str = preview_string(find_str)
    logger.info(f"In {target_file} have been found and replaced {num_occurrences} occurrences of '{preview_str}'")

    # Write the file out again
    with open(target_file, 'w') as fw:
        fw.write(file_content)


def count_occurrences(target_file, file_content, replacement_pairs):
    """
    :param target_file: file name where to count text occurrences
    :param file_content: this file content
    :param replacement_pairs: list of ReplacePair objects; we are interested only in ReplacePair.old_text
    """
    for replacement_pair in replacement_pairs:
        num_occurrences = file_content.count(replacement_pair.old_text)
        preview_str = preview_string(replacement_pair.old_text)
        logger.info(f"In {target_file} {num_occurrences} occurrences of '{preview_str}' have been found")


def replace_occurrences(target_file, replacement_pairs):
    """
    :param target_file: file name where to count text occurrences
    :param replacement_pairs: list of ReplacePair objects; we are interested only in ReplacePair.old_text
    """
    for replacement_pair in replacement_pairs:
        replace_infile(target_file, replacement_pair.old_text, replacement_pair.new_text)


def only_count(project_dir):
    """
    :param project_dir:
    """
    logger.info("Only count text occurrences, do not perform actual replace")
    for target_file, replacements in REPLACE_CONTENT.items():
        logger.info(f"Count replacements in {target_file}")
        target_file = os.path.join(os.path.realpath(project_dir), target_file)
        with open(target_file, 'r') as f:
            file_content = f.read()
            count_occurrences(target_file, file_content, replacements)


def replace_all(project_dir):
    """
    :param project_dir:
    """
    logger.info("Search and replace all text occurrences")
    for target_file, replacements in REPLACE_CONTENT.items():
        logger.info(f"Perform replacements in {target_file}")
        target_file = os.path.join(os.path.realpath(project_dir), target_file)
        replace_occurrences(target_file, replacements)


def main():
    """
    Sets build environment for the target platform and runs CMake
    :return: CMake return code
    """

    parser = argparse.ArgumentParser(description='Command-line interface')
    parser.add_argument('--project-dir',
                        help='Root directory of Virtualbox source code',
                        default=os.path.realpath(__file__),
                        required=False)
    parser.add_argument('--only-count',
                        help='Only count text occurrences, do not replace',
                        action='store_true',
                        default=False,
                        required=False)

    args = parser.parse_args()
    logger.info(f"Project dir is {args.project_dir}")

    if args.only_count:
        only_count(project_dir=args.project_dir)
    else:
        replace_all(project_dir=args.project_dir)

    return 0


###########################################################################
if __name__ == '__main__':
    sys.exit(main())
