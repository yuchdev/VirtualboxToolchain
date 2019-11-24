import os
import sys
import argparse
import logging
import log_helper

__dec__ = """Bulk files processor. 
Does not intended to be universal, change the code every time you need different conditions.
Allows rename or remove, non-recursive or recursive 
"""

logger = log_helper.setup_logger(name="validation_script", level=logging.DEBUG, log_to_file=False)


def main():
    """
    Perform directory processing
    :return: System return code
    """
    parser = argparse.ArgumentParser(description='Command-line interface')
    parser.add_argument('--config-dir',
                        help='Path to local config file',
                        metavar='DIR',
                        required=False)

    parser.add_argument('--virtualbox',
                        help='Validate specific configuration for Virtualbox.exe',
                        action='store_true',
                        required=False)

    parser.add_argument('--additions',
                        help='Validate specific configuration for GuestAdditions.iso',
                        action='store_true',
                        required=False)

    args = parser.parse_args()

    if not args.config_dir:
        config_dir = os.path.dirname(os.path.realpath(__file__))
        logger.info("Locate LocalConfig.kmk in a working directory by default")
    else:
        config_dir = os.path.abspath(args.config_dir)

    if not os.path.isdir(config_dir):
        logger.warning("LocalConfig directory does not exist: %s " % config_dir)

    local_config = os.path.join(config_dir, "LocalConfig.kmk")

    if not os.path.isfile(local_config):
        logger.warning("LocalConfig.kmk does not exist: %s " % local_config)

    logger.info("LocalConfig.kmk located at %s" % local_config)

    if args.virtualbox:
        logger.info("Validate specific configuration for Virtualbox.exe")
    if args.additions:
        logger.info("Validate specific configuration for GuestAdditions.iso")

    return 0


###########################################################################
if __name__ == '__main__':
    sys.exit(main())
