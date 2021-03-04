import os
import sys
import argparse
from log_helper import logger


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


def replace_infile(filename, find_str, replace_str):
    """
    :param filename: file name where to perform replace
    :param find_str: substring to find
    :param replace_str: string to put instead
    """
    # Read in the file
    with open(filename, 'r') as target_file:
        file_content = target_file.read()

    # Replace the target string
    file_content, num_occurrences = search_replace(file_content, find_str, replace_str)
    preview_str = "%s..." % find_str[0, 10]
    logger.info(f"In {filename} have been found and replaced {num_occurrences} occurrences of '{preview_str}'")

    # Write the file out again
    with open(filename, 'w') as file:
        file.write(file_content)


def main():
    """
    Sets build environment for the target platform and runs CMake
    :return: CMake return code
    """

    parser = argparse.ArgumentParser(description='Command-line interface')
    parser.add_argument('--cmake',
                        help='Generate build files using CMake',
                        action='store_true',
                        default=False,
                        required=False)

    args = parser.parse_args()

    return 0


###########################################################################
if __name__ == '__main__':
    sys.exit(main())
