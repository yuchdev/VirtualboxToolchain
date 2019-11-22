import os
import sys
import stat
import shutil
import argparse
import logging
import log_helper

logger = log_helper.setup_logger(name="cmake_runner", level=logging.DEBUG, log_to_file=False)


###########################################################################
def on_rm_error(*args):
    """
    In case the file or directory is read-only and we need to delete it
    this function will help to remove 'read-only' attribute
    :param args: (func, path, exc_info) tuple
    """
    # path contains the path of the file that couldn't be removed
    # let's just assume that it's read-only and unlink it.
    _, path, _ = args
    logger.warning("OnRmError: {0}".format(path))
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)


def prepare_build_dirs():
    if not os.path.isdir('build'):
        os.mkdir('build')
        os.chdir('build')


def prepare_build_directory():
    """
    Cleanup 'build-cmake' dir, check CMakeLists.txt presence
    :raise: RuntimeError if CMakeLists.txt is absent
    """
    os.mkdir('build-cmake')
    os.chdir('build-cmake')
    logger.info("We are in {0}".format(os.getcwd()))
    if not os.path.join(os.getcwd(), 'CMakeLists.txt'):
        raise RuntimeError('CMakeLists.txt should be present in the solution directory')

###########################################################################

def environment_value(environment_name):
    """
    :param environment_name: Name of the environment variable
    :return: Value of the environment variable or the empty string if not exists
    """
    try:
        return os.environ[environment_name]
    except KeyError:
        return ''


def set_windows_environment():
    """
    Read environment variables for Visual Studio environment scripts
    Normally we have something like:
    ProgramFiles=C:\Program Files
    VS120COMNTOOLS=C:\Program Files\Microsoft Visual Studio 12.0\Common7\Tools\
    However we should double-check
    """
    vs2015_common_tools = environment_value('VS140COMNTOOLS')

    # run VS bat-file
    if vs2015_common_tools == '':
        vs2015_common_tools = 'C:\\Program Files\\Microsoft Visual Studio 14.0\\Common7\\Tools\\'
    vc_environment_bat = os.path.join(vs2015_common_tools, '..\\..\\VC\\vcvarsall.bat')
    if not os.path.exists(vc_environment_bat):
        vc_environment_bat = os.path.join(vs2015_common_tools, '..\\..\\VC\\bin\\vcvars32.bat')
    if not os.path.exists(vc_environment_bat):
        raise RuntimeError('Cannot detect visual studio environment')
    logger.info('Setting Visual Studio environment')
    logger.info("Run setting environment: {0}".format(vc_environment_bat))
    os.system('"{0}"'.format(vc_environment_bat))


def set_unix_environment():
    """
    Read environment variables for the POSIX build
    :return:
    """
    raise NotImplementedError(set_unix_environment())


def run_cleanup():
    """
    Clean-up build directory
    :return: Python OS return code
    """
    logger.info("Clean-up build directory")
    if os.path.isdir('build-cmake'):
        shutil.rmtree('build-cmake', onerror=on_rm_error)
    return 0


def configure_qt_directory(qt_path):
    """
    Configure Cmake command to use Qt directory
    :param qt_path: Path to Qt installation ending with actual version of MSVS (msvc2015, msvc2017)
    :return: String containing CMake configuration parameter for Qt location
    """
    return " -DCMAKE_PREFIX_PATH={0}".format(qt_path) if qt_path is not None else ""


def configure_openssl_directory(openssl_path):
    """
    Configure Cmake command to use OpenSSL directory
    :param openssl_path: Path to OpenSSL root, contains bin, lib and include
    :return: String containing CMake configuration parameter for OpenSSL location
    """
    return " -DOPENSSL_ROOT_DIR={0}".format(openssl_path) if openssl_path is not None else ""


def run_cmake(system_version, qt_path, openssl_path, config):
    """
    Execute CMake in the solution dir (CMakeLists.txt must be present), OpenSSL path should be set
    :param qt_path: Path to Qt installation ending with actual version of MSVS (msvc2015, msvc2017)
    :param system_version: Windows version in MAJOR.MINOR format. Windows 7 is 6.1
    :param openssl_path: Path to OpenSSL root, contains bin, lib and include
    :param config:  What to compile: PANIC_BUTTON, DESIRE_VPN, HTTP_SERVER
    :return: CMake return code
    """
    prepare_build_directory()
    cmake_command = "cmake .. -DCMAKE_SYSTEM_VERSION={0}{1}{2} -D{3}=ON".format(
        system_version, configure_qt_directory(qt_path), configure_openssl_directory(openssl_path), config)
    logger.info(cmake_command)
    return os.system(cmake_command)


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
        qt_default_path = 'C:/Qt/5.8/msvc2015'
    elif os.name == 'posix':
        set_unix_environment()
        qt_default_path = '/opt/Qt/5.8/msvc2015'
        system_version = '1'

    parser = argparse.ArgumentParser(description='Command-line interface')
    parser.add_argument('--cmake',
                        help='Generate build files using CMake',
                        action='store_true',
                        default=False,
                        required=False)

    parser.add_argument('--cleanup',
                        help='Perform CMake directory cleanup',
                        action='store_true',
                        default=False,
                        required=False)

    parser.add_argument('--qt',
                        help='Path to Qt directory which contains bin, lib and include',
                        dest='qt',
                        default=qt_default_path,
                        required=False)

    parser.add_argument('--openssl',
                        help='Path to OpenSSL root, contains bin, lib and include',
                        dest='openssl',
                        required=False)

    parser.add_argument('--config',
                        help='CMake configuration: {PANIC_BUTTON|DESIRE_VPN|HTTP_SERVER}',
                        dest='config',
                        default='PANIC_BUTTON',
                        required=False)

    args = parser.parse_args()

    if args.cleanup:
        logger.info('Cleanup up Visual Studio environment')
        return run_cleanup()
    elif args.config:
        return run_cmake(system_version, args.qt, args.openssl, args.config)
    else:
        parser.print_usage()
        return 0


###########################################################################
if __name__ == '__main__':
    sys.exit(main())
