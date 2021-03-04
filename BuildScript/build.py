import os
import sys
import stat
import shutil
import argparse
from log_helper import logger


def main():
    """
    Sets build environment for the target platform and runs CMake
    :return: CMake return code
    """
    prepare_build_dirs()

    # Set environment for Windows or POSIX
    global qt_default_path
    system_version = '0'
    if os.name == 'nt':
        set_windows_environment()
        system_version = '{0}.{1}'.format(sys.getwindowsversion().major, sys.getwindowsversion().minor)
        logger.info("SYSTEM_VERSION={0}".format(system_version))
        qt_default_path = 'C:/Qt/5.6.3/msvc2010_64'
    elif os.name == 'posix':
        set_unix_environment()
        qt_default_path = '/opt/Qt/5.8/msvc2015'
        system_version = '1'

    parser = argparse.ArgumentParser(description='Command-line interface')

    parser.add_argument('--cleanup',
                        help='Perform build directory cleanup',
                        action='store_true',
                        default=False,
                        required=False)

    args = parser.parse_args()
    return 0


###########################################################################
if __name__ == '__main__':
    sys.exit(main())
