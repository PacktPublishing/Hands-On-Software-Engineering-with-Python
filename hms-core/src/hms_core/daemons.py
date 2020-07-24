#!/usr/bin/env python
"""
TODO: Document the module.
Provides classes and functionality for SOME_PURPOSE
"""

#######################################
# Any needed from __future__ imports  #
# Create an "__all__" list to support #
#   "from module import member" use   #
#######################################

__all__ = [
    # Constants
    # Exceptions
    # Functions
    # ABC "interface" classes
    # ABC abstract classes
    'BaseDaemon',
    'BaseDaemonizable',
    'BaseRequestHandler',
    # Concrete classes
]

#######################################
# Module metadata/dunder-names        #
#######################################

__author__ = 'Brian D. Allbee'
__copyright__ = 'Copyright 2018, all rights reserved'
__status__ = 'Development'

#######################################
# Standard library imports needed     #
#######################################

import abc
import atexit
import logging
import os
import signal
import sys
import tempfile
import yaml

from types import FrameType

#######################################
# Third-party imports needed          #
#######################################

#######################################
# Local imports needed                #
#######################################

#######################################
# Initialization needed before member #
#   definition can take place         #
#######################################

#######################################
# Module-level Constants              #
#######################################

#######################################
# Custom Exceptions                   #
#######################################

#######################################
# Module functions                    #
#######################################

#######################################
# ABC "interface" classes             #
#######################################

#######################################
# Abstract classes                    #
#######################################

class BaseDaemon(metaclass=abc.ABCMeta):
    """
Provides baseline functionality, interface requirements, and type-identity for 
objects that can act as a daemon/service managed by facilities in the local OS 
(like systemd) or by third-party service-configurators (like NSSM)
"""
    ###################################
    # Class attributes/constants      #
    ###################################

    _handler_classes = {}
    _handler_keys = []
    # - Default logging information
    _logging = {
        'name':None,
        'format':'%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        'file':{
            'logfile':None,
            'level':logging.INFO,
        },
        'console':{
            'level':logging.ERROR,
        }
    }

    ###################################
    # Property-getter methods         #
    ###################################

    def _get_config_file(self) -> (str,None):
        return self._config_file

    def _get_logger(self) -> (logging.Logger,):
        return self._logger

#     def _get_property_name(self) -> str:
#         return self._property_name

    ###################################
    # Property-setter methods         #
    ###################################

    def _set_config_file(self, value:(str,)):
        if type(value) != str:
            raise TypeError(
                '%s.config_file expects a string value that points '
                'to a readable configuration-file on the local file-'
                'system, but was passed "%s" (%s)' % 
                (self.__class__.__name__, value, type(value).__name__)
            )
        if not os.path.isfile(value):
            if type(value) != str:
                raise TypeError(
                    '%s.config_file expects a string value that '
                    'points to a readable configuration-file on the '
                    'local file-system, but was passed "%s" (%s), '
                    'which is not a file' % 
                    (
                        self.__class__.__name__, value, 
                        type(value).__name__
                    )
                )
        if not os.access(value, os.R_OK):
            if type(value) != str:
                raise TypeError(
                    '%s.config_file expects a string value that '
                    'points to a readable configuration-file on the '
                    'local file-system, but was passed "%s" (%s), '
                    'which is not a READABLE file' % 
                    (
                        self.__class__.__name__, value, 
                        type(value).__name__
                    )
                )
        self.debug(
            '%s.config_file set to %s' % (self.__class__.__name__, value)
        )
        self._config_file = value

    ###################################
    # Property-deleter methods        #
    ###################################

    def _del_config_file(self):
        self._config_file = None

    def _del_logger(self):
        self._logger = None

    ###################################
    # Instance property definitions   #
    ###################################

    config_file = property(
        _get_config_file, None, None, 
        'Gets the configuration-file used to set up the instance'
    )
    logger = property(
        _get_logger, None, None, 
        'Gets the logger for the instance'
    )

    ###################################
    # Object initialization           #
    ###################################

    def __init__(self, config_file:(str,)):
        """
Object initialization.

self .............. (BaseDaemon instance, required) The instance to 
                    execute against
config_file ....... (str, file-path, required) The location of the 
                    configuration-file to be used to configure the 
                    daemon instance

The configuration-file is YAML, and allows the following items to be set by 
default:

logging:
  console:
    level: error
  file:
    level: debug
    logfile: /var/log/daemon-name.log
  format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
  name: daemon-name
"""
        # - Call parent initializers if needed
        # - Set default instance property-values using _del_... methods
        self._del_config_file()
        self._del_logger()
        # - Set instance property-values from arguments using 
        #   _set_... methods
        self._set_config_file(config_file)
        # - Perform any other initialization needed
        # - Read configuration and override items as needed
        self.configure()
        # - Set up logging
        self._create_logger()
        # - Set up handlers to allow graceful shut-down
        signal.signal(signal.SIGINT, self.stop)
        signal.signal(signal.SIGTERM, self.stop)
        self.debug(
            'SIGINT and SIGTERM hanlders for %s created' % 
            (self.__class__.__name__)
        )
        # - Set up the local flag that indicates whether we're expected 
        #   to be running or not:
        self._running = False

    ###################################
    # Object deletion                 #
    ###################################

    ###################################
    # Abstract methods                #
    ###################################

    @abc.abstractmethod
    def main(self):
        """
The main event-loop (or whtever is equivalent) for the service instance.
"""
        raise NotImplementedError(
            '%s.main has not been implemented as required by '
            'BaseDaemon' % (self.__class__.__name__)
        )

    @abc.abstractmethod
    def _on_configuration_loaded(self, **config_data):
        """
Applies the configuration to the instance. Since there are configuration values 
that may exist for any instance of the class, this method should be called by 
derived classes in addition to any local configuration.
"""
        if config_data.get('logging'):
            # - Since the class' logging settings are just a dict, we can 
            #   just update that dict, at least to start with:
            self.__class__._logging.update(config_data['logging'])
            # - Once the update is complete, we do need to change any logging-
            #   level items, though. We'll start with the file-logging:
            file_logging = self.__class__._logging.get('file')
            if file_logging:
                file_level = file_logging.get('level')
                if not file_level:
                    file_logging['level'] = logging.INFO
                elif type(file_level) == str:
                    try:
                        file_logging['level'] = getattr(
                            logging, file_level.upper()
                        )
                    except AttributeError:
                        file_logging['level'] = logging.INFO
            # - Similarly, console-logging
            console_logging = self.__class__._logging.get('console')
            if console_logging:
                console_level = console_logging.get('level')
                if not console_level:
                    console_logging['level'] = logging.INFO
                elif type(console_level) == str:
                    try:
                        console_logging['level'] = getattr(
                            logging, console_level.upper()
                        )
                    except AttributeError:
                        console_logging['level'] = logging.INFO

    ###################################
    # Service-action methods          #
    ###################################

    def cleanup(self):
        """
Performs whatever clean-up actions/activities need to be executed after the 
main process-loop terminates. Override this in your daemon-class if needed, 
otherwise it can be left alone.
"""
        self.info('%s.cleanup called' % (self.__class__.__name__))

    def find_request_handler(self, key:(str,)):
        """
Finds a registered BaseRequestHandler class that is expected to be able 
to handle the request signified by the key value, creates an instance 
of the class, and returns it.
"""
        # - Set up the _handler_keys if it hasn't been defined yet. The 
        #   goal here is to have a list of registered keys, sorted from 
        #   longest to shortest so that we can match based on the 
        #   longest registered key/path/command-name/whatever that 
        #   matches the incoming value:
        if not self.__class__._handler_keys:
            self.__class__._handler_keys = sorted(
                self.__class__._handler_classes.keys(),
                key=lambda k: len(k), 
                reverse=True
            )
        # - Find the first (longest) key that matches the incoming key:
        for candidate_key in self.__class__._handler_keys:
            if candidate_key.startswith(key):
                # - If we find a match, then create an instance of 
                #   the class and return it
                result = self.__class__._handler_classes[candidate_key]
                return result(self)
        return None

    def preflight(self):
        """
Performs whatever pre-flight actions/activities need to be executed before 
starting the main process. Override this in your daemon-class if needed, 
otherwise it can be left alone.
"""
        self.info('%s.preflight called' % (self.__class__.__name__))

    def restart(self):
        """
Resarts the daemon-process by calling the instance's stop then start methods. 
This may not be directly accessible (at least not in any useful fashion) 
outside the running instance, but external daemon/service managers should be 
able to simply kill the running process and start it up again.
"""
        self.info('Restarting %s' % self.__class__.__name__)
        self.stop()
        self.start()

    def start(self):
        """
Starts the daemon/service that the instance provides.
"""
        if self._running:
            self.info(
                '%s instance is already running' % (self.__class__.__name__)
            )
            return
        self.preflight()
        self.info('Starting %s.main' % self.__class__.__name__)
        self.main()
        self.cleanup()

    def stop(self, signal_num:(int,None)=None, frame:(FrameType,None)=None):
        """
Stops the daemon-process. May be called by a signal event-handler, in which 
case the signal_num and frame values will be passed. Can also be called 
directly withgout those argument-values.

signal_num ........ (int, optional, defaults to None) The signal-number, 
                    if any, that prompted the shutdown.
frame ............. (Stack-frame, optional, defaults to None) The associated 
                    stack-frame.
"""
        self.info('Stopping %s' % self.__class__.__name__)
        self.debug('+- signal_num ... %s' % (signal_num))
        self.debug('+- frame ........ %s' % (frame))
        self._running = False

    ###################################
    # Instance methods                #
    ###################################

    def configure(self):
        """
Reads the instance's configuration-file, converts it to a dictionary of values, 
then hands the responsibility for actually configuring the instance off to its
required _on_configuration_loaded method
"""
        try:
            self.info('Loading configuration for %s' % self.__class__.__name__)
        except RuntimeError:
            # - This should only happen during start-up...
            print('Loading configuration for %s' % self.__class__.__name__)
        try:
            fp = open(self.config_file, 'r')
            config_data = yaml.load(fp)
            fp.close()
        except Exception as error:
            raise RuntimeError(
                '%s.config could not read configuration-data from '
                '%s, %s was raised: %s' % 
                (
                    self.__class__.__name__, config_file, 
                    error.__class__.__name__, error
                )
            )
        # - With the configuration read, it's time to actually 
        #   configure the instance
        self._on_configuration_loaded(**config_data)

    def _create_logger(self):
        """
Creates the instance's logger object, sets up formatting for log-entries, and 
handlers for various log-output destinations
"""
        if not self.__class__._logging.get('name'):
            raise AttributeError(
                '%s cannot establish a logging facility because no '
                'logging-name value was set in the class itself, or '
                'through configuration settings (in %s).' % 
                (self.__class__.__name__, self.config_file)
            )
        try:
            logging_settings = self.__class__._logging
            # - Global log-format
            formatter = logging.Formatter(logging_settings['format'])
            # - The main logger
            self._logger = logging.getLogger(
                logging_settings['name']
            )
            # - By default, the top-level logger instance will accept anything. 
            #   We'll change that to the appropriate level after checking the 
            #   various log-level settings:
            final_level = logging.DEBUG
            if logging_settings.get('file'):
                # - We're logging *something* to a file, so create a handler 
                #   to that purpose:
                if not self.__class__._logging['file'].get('logfile'):
                    raise AttributeError(
                        '%s cannot establish a logging facility because no '
                        'log-file value was set in the class itself, or '
                        'through configuration settings (in %s).' % 
                        (self.__class__.__name__, self.config_file)
                    )
                # - The actual file-handler
                file_handler = logging.FileHandler(
                    logging_settings['file']['logfile']
                )
                # - Set the logging-level accordingly, and adjust final_level
                file_handler.setLevel(logging_settings['file']['level'])
                final_level = min(
                    [
                        logging_settings['file']['level'],
                        final_level
                    ]
                )
                # - Set formatting and attach it to the main logger:
                file_handler.setFormatter(formatter)
                self._logger.addHandler(file_handler)
            if logging_settings.get('console'):
                # - We're logging *something* to the console, so create a 
                #   handler to that purpose:
                # - The actual console-handler
                console_handler = logging.StreamHandler()
                # - Set the logging-level accordingly, and adjust final_level
                console_handler.setLevel(logging_settings['console']['level'])
                final_level = min(
                    [
                        logging_settings['console']['level'],
                        final_level
                    ]
                )
                # - Set formatting and attach it to the main logger:
                console_handler.setFormatter(formatter)
                self._logger.addHandler(console_handler)
            # - For efficiency's sake, use the final_level at the logger itself. 
            #   That should (hopefully) allow logging to run (trivially) 
            #   faster, since it'll know to skip anything that isn't handled by 
            #   at least one handler...
            self._logger.setLevel(final_level)
        except Exception as error:
            raise RuntimeError(
                '%s could not complete the set-up of its logging '
                'facilities because %s was raised: %s' % 
                (
                    self.__class__.__name__, error.__class__.__name__, 
                    error
                )
            )
        # - Log the fact that we can log stuff now :-)
        self.info(
            'Logging started. Other messages may have been output to '
            'stdout/terminal prior to now'
        )

    ###################################
    # Logging methods                 #
    ###################################

    def critical(self, msg, *args, **kwargs):
        if self.logger:
            self.logger.critical(msg, *args, **kwargs)
        else:
            print('CRITICAL - %s' % msg)

    def debug(self, msg, *args, **kwargs):
        if self.logger:
            self.logger.debug(msg, *args, **kwargs)
        else:
            print('DEBUG    - %s' % msg)

    def error(self, msg, *args, **kwargs):
        if self.logger:
            self.logger.error(msg, *args, **kwargs)
        else:
            print('ERROR    - %s' % msg)

    def info(self, msg, *args, **kwargs):
        if self.logger:
            self.logger.info(msg, *args, **kwargs)
        else:
            print('INFO     - %s' % msg)

    def warn(self, msg, *args, **kwargs):
        if self.logger:
            self.logger.warn(msg, *args, **kwargs)
        else:
            print('WARNING  - %s' % msg)

    ###################################
    # Overrides of built-in methods   #
    ###################################

    ###################################
    # Class methods                   #
    ###################################

    @classmethod
    def register_handler(cls, handler_class:(type,), *keys):
        """
Registers a BaseRequestHandler *class* as a candidate for handling 
requests for the specified keys"""
        if type(handler_class) != type \
            or not issubclass(handler_class, BaseRequestHandler):
            raise TypeError(
                '%s.register_handler expects a *class* derived from '
                'BaseRequestHandler as its handler_class argument, but '
                'was passed "%s" (%s), which is not such a class' % 
                (cls.__name__, value, type(value).__name__)
            )
        if not keys:
            raise ValueError(
                '%s.register_handler expects one or more keys, each '
                'a string-value, to register the handler-class with, '
                'but none were provided' % (cls.__name__)
            )
        # - Check for malformed keys
        bad_keys = [
            key for key in keys
            if type(key) != str
            or '\n' in key
            or '\r' in key
            or '\t' in key
            or key.strip() != key
            or not key.strip()
        ]
        if bad_keys:
            raise ValueError(
                '%s.register_handler expects one or more keys, each a '
                'single-line, non-empty string-value with no leading '
                'or trailing white-space, and no white-space other '
                'than spaces, but was passed a list including %s, '
                'which do not meet these criteria' % 
                (cls.__name__, '"' + '", "'.join(bad_keys) + '"')
            )
        # - Check for keys already registered
        existing_keys = [
            key for key in keys if key in cls._handler_classes.keys()
        ]
        if existing_keys:
            raise KeyError(
                '%s.register_handler is not allowed to replace handler-'
                'classes already registered, but is being asked to do '
                'so for %s keys' % 
                (cls.__name__, '"' + '", "'.join(existing_keys) + '"')
            )
        # - If this point is reached, everything is hunky-dory, so add 
        #   the handler_class for each key:
        for key in keys:
            cls._handler_classes[key] = handler_class

    ###################################
    # Static methods                  #
    ###################################

class BaseRequestHandler(metaclass=abc.ABCMeta):
    """
Provides baseline functionality, interface requirements, and 
type-identity for objects that can process daemon/service requests, 
generating and returning a response, serialized to some string-based 
format.
"""
    ###################################
    # Class attributes/constants      #
    ###################################

    _default_formatter = None

    ###################################
    # Property-getter methods         #
    ###################################

    def _get_daemon(self) -> (BaseDaemon,):
        return self._daemon

    ###################################
    # Property-setter methods         #
    ###################################

    def _set_daemon(self, value:(BaseDaemon,)) -> None:
        if not isinstance(value, BaseDaemon):
            raise TypeError(
                '%s.daemon expects an instance of a class derived '
                'from BaseDaemon, but was passed "%s" (%s)' % 
                (self.__class__.__name__, value, type(value).__name__)
            )
        self._daemon = value

    ###################################
    # Property-deleter methods        #
    ###################################

    def _del_daemon(self) -> None:
        self._daemon = None

    ###################################
    # Instance property definitions   #
    ###################################

    daemon = property(
        _get_daemon, None, None, 
        'Gets, sets or deletes the daemon associated with the instance'
    )

    ###################################
    # Object initialization           #
    ###################################

    def __init__(self, daemon:(BaseDaemon,)):
        """
Object initialization.

self .............. (BaseRequestHandler instance, required) The 
                    instance to execute against
daemon ............ (BaseDaemon instance, required) The daemon that the 
                    request to be handled originated with.
"""
        # - Call parent initializers if needed
        # - Set default instance property-values using _del_... methods
        self._del_daemon()
        # - Set instance property-values from arguments using 
        #   _set_... methods
        self._set_daemon(daemon)
        # - Perform any other initialization needed

    ###################################
    # Object deletion                 #
    ###################################

    ###################################
    # Abstract methods                #
    ###################################

    @abc.abstractmethod
    def __call__(self, request:(dict,), formatter=None) -> (str,):
        """
Makes the instance callable, providing a mechanism for processing the 
supplied request, generating a data-structure containing the response 
for the request, formatting that response, and returning it.

self .............. (BaseRequestHandler instance, required) The 
                    instance to execute against
request ........... (dict, required) The request to be handled
formatter ......... (BaseResponseFormatter instance, optional, if not 
"""
        pass

    ###################################
    # Instance methods                #
    ###################################

    ###################################
    # Overrides of built-in methods   #
    ###################################

    ###################################
    # Class methods                   #
    ###################################

    ###################################
    # Static methods                  #
    ###################################

class BaseResponseFormatter(metaclass=abc.ABCMeta):
    """
Provides baseline functionality, interface requirements, and 
type-identity for objects that can format response data-structures 
to any of several serialized string representations.
"""
    ###################################
    # Class attributes/constants      #
    ###################################

    ###################################
    # Property-getter methods         #
    ###################################

    def _get_daemon(self) -> (BaseDaemon,):
        return self._daemon

    def _get_request_handler(self) -> str:
        return self._request_handler

    ###################################
    # Property-setter methods         #
    ###################################

    def _set_daemon(self, value:(BaseDaemon,)) -> None:
        if not isinstance(value, BaseDaemon):
            raise TypeError(
                '%s.daemon expects an instance of a class derived '
                'from BaseDaemon, but was passed "%s" (%s)' % 
                (self.__class__.__name__, value, type(value).__name__)
            )
        self._daemon = value

    def _set_request_handler(self, value:(BaseRequestHandler,)) -> None:
        if not isinstance(value, BaseRequestHandler):
            raise TypeError(
                '%s.request_handler expects an instance of a class '
                'derived from BaseRequestHandler, but was passed '
                '"%s" (%s)' % 
                (self.__class__.__name__, value, type(value).__name__)
            )
        self._request_handler = value

    ###################################
    # Property-deleter methods        #
    ###################################

    def _del_daemon(self) -> None:
        self._daemon = None

    def _del_request_handler(self) -> None:
        self._request_handler = None

    ###################################
    # Instance property definitions   #
    ###################################

    daemon = property(
        _get_daemon, None, None, 
        'Gets, sets or deletes the daemon associated with the instance'
    )
    request_handler = property(
        _get_request_handler, None, None, 
        'Gets, sets or deletes the request_handler associated with '
        'the instance'
    )

    ###################################
    # Object initialization           #
    ###################################

    def __init__(self, 
        daemon:(BaseDaemon,), 
        request_handler:(BaseRequestHandler,),
    ):
        """
Object initialization.

self .............. (BaseResponseFormatter instance, required) The 
                    instance to execute against
daemon ............ (BaseDaemon instance, required) The daemon that the 
                    request to be handled originated with.
request_handler ... (BaseRequesthandler instance, required) The request-
                    handler object associated with the instance.
"""
        # - Call parent initializers if needed
        # - Set default instance property-values using _del_... methods
        self._del_daemon()
        self._del_request_handler()
        # - Set instance property-values from arguments using 
        #   _set_... methods
        self._set_daemon(daemon)
        self._set_request_handler(request_handler)
        # - Perform any other initialization needed

    ###################################
    # Object deletion                 #
    ###################################

    ###################################
    # Abstract methods                #
    ###################################

    @abc.abstractmethod
    def __call__(self, response:(dict,)) -> (str,):
        """
Makes the instance callable, providing a mechanism for formatting a 
standard response-dictionary data-structure.

self .............. (BaseRequestHandler instance, required) The 
                    instance to execute against
response .......... (dict, required) The response to be formatted
"""
        pass

    ###################################
    # Instance methods                #
    ###################################

#     def instance_method(self, arg:str, *args, **kwargs):
#         """TODO: Document method
# DOES_WHATEVER
# 
# self .............. (BaseResponseFormatter instance, required) The 
#                     instance to execute against
# arg ............... (str, required) The string argument
# *args ............. (object*, optional) The arglist
# **kwargs .......... (dict, optional) keyword-args, accepts:
#  - kwd_arg ........ (type, optional, defaults to SOMETHING) The SOMETHING 
#                     to apply
# """
#         pass

    ###################################
    # Overrides of built-in methods   #
    ###################################

    ###################################
    # Class methods                   #
    ###################################

    ###################################
    # Static methods                  #
    ###################################

class BaseDaemonizable(BaseDaemon):
    """
Provides baseline functionality, interface requirements, and type-identity for 
objects that can act as a daemon/service managed by SysV on POSIX systems that 
still use it, or similar process-controls.

All that need be done to use this is to derive the service-class from 
BaseDaemonizalbe instead of BaseDaemon. It will handle all of the additional 
differences without any further effort.

Relies on os.fork which is NOT supported in Windows!
"""
    ###################################
    # Class attributes/constants      #
    ###################################

    _pidfile = None
    _sdterr = None
    _stdin = None
    _stdout = None

    ###################################
    # Property-getter methods         #
    ###################################

    def _get_pidfile(self) -> str:
        return self._pidfile

    def _get_stderr(self) -> str:
        return self._stderr

    def _get_stdin(self) -> str:
        return self._stdin

    def _get_stdout(self) -> str:
        return self._stdout

    ###################################
    # Property-setter methods         #
    ###################################

    def _set_pidfile(self, value:(str,)) -> None:
        if type(value) != str:
            raise TypeError(
                '%s.pidfile expects a string value that is a valid file-system '
                'path that the instance can read from and write to, but was '
                'passed "%s" (%s)' % 
                (self.__class__.__name__, value, type(value).__name__)
            )
        if not os.path.exists(value):
            path_dir = os.path.dirname(value)
            if not os.path.exists(path_dir):
                raise ValueError(
                    '%s.pidfile expects a string value that is a valid file-'
                    'system path that the instance can read from and write to, '
                    'but was passed "%s" (%s), which doesn\'t exist, and whose '
                    'parent directory (%s) doesn\'t exist either' % 
                    (
                        self.__class__.__name__, value, type(value).__name__, 
                        path_dir
                    )
                )
            if not os.access(path_dir, os.R_OK):
                raise ValueError(
                    '%s.pidfile expects a string value that is a valid file-'
                    'system path that the instance can read from and write to, '
                    'but was passed "%s" (%s), which doesn\'t exist, and whose '
                    'parent directory (%s) doesn\'t allow read-access' % 
                    (
                        self.__class__.__name__, value, type(value).__name__, 
                        path_dir
                    )
                )
            if not os.access(path_dir, os.W_OK):
                raise ValueError(
                    '%s.pidfile expects a string value that is a valid file-'
                    'system path that the instance can read from and write to, '
                    'but was passed "%s" (%s), which doesn\'t exist, and whose '
                    'parent directory (%s) doesn\'t allow write-access' % 
                    (
                        self.__class__.__name__, value, type(value).__name__, 
                        path_dir
                    )
                )
        else:
            if not os.access(value, os.R_OK):
                raise ValueError(
                    '%s.pidfile expects a string value that is a valid file-'
                    'system path that the instance can read from and write to, '
                    'but was passed "%s" (%s), which doesn\'t allow '
                    'read-access' % 
                    (self.__class__.__name__, value, type(value).__name__)
                )
            if not os.access(value, os.W_OK):
                raise ValueError(
                    '%s.pidfile expects a string value that is a valid file-'
                    'system path that the instance can read from and write to, '
                    'but was passed "%s" (%s), which doesn\'t allow '
                    'write-access' % 
                    (self.__class__.__name__, value, type(value).__name__)
                )
        self._pidfile = value

    def _set_stderr(self, value:str) -> None:
        if type(value) != str:
            raise TypeError(
                '%s.stderr expects a string value that is a valid file-system '
                'path that the instance can write to, but was passed '
                '"%s" (%s)' % 
                (self.__class__.__name__, value, type(value).__name__)
            )
        if not os.path.exists(value):
            path_dir = os.path.dirname(value)
            if not os.path.exists(path_dir):
                raise ValueError(
                    '%s.stderr expects a string value that is a valid file-'
                    'system path that the instance can write to, but was '
                    'passed "%s" (%s), which doesn\'t exist, and whose parent '
                    'directory (%s) doesn\'t exist either' % 
                    (
                        self.__class__.__name__, value, type(value).__name__, 
                        path_dir
                    )
                )
            if not os.access(path_dir, os.W_OK):
                raise ValueError(
                    '%s.stderr expects a string value that is a valid file-'
                    'system path that the instance can write to, but was '
                    'passed "%s" (%s), which doesn\'t exist, and whose parent '
                    'directory (%s) doesn\'t allow write-access' % 
                    (
                        self.__class__.__name__, value, type(value).__name__, 
                        path_dir
                    )
                )
        else:
            if not os.access(value, os.W_OK):
                raise ValueError(
                    '%s.stderr expects a string value that is a valid file-'
                    'system path that the instance can write to, but was '
                    'passed "%s" (%s), which doesn\'t allow write-access' % 
                    (self.__class__.__name__, value, type(value).__name__)
                )
        self._stderr = value

    def _set_stdin(self, value:str) -> None:
        if type(value) != str:
            raise TypeError(
                '%s.stdin expects a string value that is a valid file-system '
                'path that the instance can write to, but was passed '
                '"%s" (%s)' % 
                (self.__class__.__name__, value, type(value).__name__)
            )
        if not os.path.exists(value):
            path_dir = os.path.dirname(value)
            if not os.path.exists(path_dir):
                raise ValueError(
                    '%s.stdin expects a string value that is a valid file-'
                    'system path that the instance can read from, but was '
                    'passed "%s" (%s), which doesn\'t exist, and whose parent '
                    'directory (%s) doesn\'t exist either' % 
                    (
                        self.__class__.__name__, value, type(value).__name__, 
                        path_dir
                    )
                )
            if not os.access(path_dir, os.R_OK):
                raise ValueError(
                    '%s.stdin expects a string value that is a valid file-'
                    'system path that the instance can read from, but was '
                    'passed "%s" (%s), which doesn\'t exist, and whose parent '
                    'directory (%s) doesn\'t allow read-access' % 
                    (
                        self.__class__.__name__, value, type(value).__name__, 
                        path_dir
                    )
                )
            if not os.access(path_dir, os.W_OK):
                raise ValueError(
                    '%s.stdin expects a string value that is a valid file-'
                    'system path that the instance can read from, but was '
                    'passed "%s" (%s), which doesn\'t exist, and whose parent '
                    'directory (%s) doesn\'t allow write-access to create the'
                    'file in the first place' % 
                    (
                        self.__class__.__name__, value, type(value).__name__, 
                        path_dir
                    )
                )
        else:
            if not os.access(value, os.R_OK):
                raise ValueError(
                    '%s.stdin expects a string value that is a valid file-'
                    'system path that the instance can read from, but was '
                    'passed "%s" (%s), which doesn\'t allow write-access' % 
                    (self.__class__.__name__, value, type(value).__name__)
                )
        self._stdin = value

    def _set_stdout(self, value:str) -> None:
        if type(value) != str:
            raise TypeError(
                '%s.stdout expects a string value that is a valid file-system '
                'path that the instance can write to, but was passed '
                '"%s" (%s)' % 
                (self.__class__.__name__, value, type(value).__name__)
            )
        if not os.path.exists(value):
            path_dir = os.path.dirname(value)
            if not os.path.exists(path_dir):
                raise ValueError(
                    '%s.stdout expects a string value that is a valid file-'
                    'system path that the instance can write to, but was '
                    'passed "%s" (%s), which doesn\'t exist, and whose parent '
                    'directory (%s) doesn\'t exist either' % 
                    (
                        self.__class__.__name__, value, type(value).__name__, 
                        path_dir
                    )
                )
            if not os.access(path_dir, os.W_OK):
                raise ValueError(
                    '%s.stdout expects a string value that is a valid file-'
                    'system path that the instance can write to, but was '
                    'passed "%s" (%s), which doesn\'t exist, and whose parent '
                    'directory (%s) doesn\'t allow write-access' % 
                    (
                        self.__class__.__name__, value, type(value).__name__, 
                        path_dir
                    )
                )
        else:
            if not os.access(value, os.W_OK):
                raise ValueError(
                    '%s.stdout expects a string value that is a valid file-'
                    'system path that the instance can write to, but was '
                    'passed "%s" (%s), which doesn\'t allow write-access' % 
                    (self.__class__.__name__, value, type(value).__name__)
                )
        self._stdout = value

    ###################################
    # Property-deleter methods        #
    ###################################

    def _del_pidfile(self) -> None:
        self._pidfile = None

    def _del_stderr(self) -> None:
        self._stderr = None

    def _del_stdin(self) -> None:
        self._stdin = None

    def _del_stdout(self) -> None:
        self._stdout = None

    ###################################
    # Instance property definitions   #
    ###################################

    pidfile = property(
        _get_pidfile, None, None, 
        'Gets the path to the file that the instance records its PID in'
    )
    stderr = property(
        _get_stderr, None, None, 
        'Gets the path to the file that the instance uses for stderr output'
    )
    stdin = property(
        _get_stdin, None, None, 
        'Gets the path to the file that the instance uses for stdin input'
    )
    stdout = property(
        _get_stdout, None, None, 
        'Gets the path to the file that the instance uses for stdout output'
    )

#     abstract_property = abc.abstractproperty()

#     property_name = property(
#         # TODO: Remove setter and deleter if access is not needed
#         _get_property_name, _set_property_name, _del_property_name, 
#         'Gets, sets or deletes the property_name (str) of the instance'
#     )

    ###################################
    # Object initialization           #
    ###################################

    def __init__(self, config_file:(str,)):
        """
Object initialization.

self .............. (BaseDaemon instance, required) The instance to 
                    execute against
config_file ....... (str, file-path, required) The location of the 
                    configuration-file to be used to configure the 
                    daemon instance

The configuration-file is YAML, and allows the following items to be set by 
default:

logging:
  console:
    level: error
  file:
    level: debug
    logfile: /var/log/daemon-name.log
  format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
  name: daemon-name

TODO:
- Add support for daemonizable-instance properties, maybe? They'd include:
  daemon:
    pidfile: /tmp/testdaemon/pid
    stdin: /path/to/stdin/file
    stdout: /path/to/stdout/file
    stderr: /path/to/stderr/file
"""
        # - Call parent initializers LAST because calling it first breaks the 
        #   configuration stdXXX assignment...
        BaseDaemon.__init__(self, config_file)
        # - Set default instance property-values using _del_... methods
        self._del_pidfile()
        self._del_stderr()
        self._del_stdin()
        self._del_stdout()
        # - Set instance property-values from arguments using 
        #   _set_... methods
        if hasattr(self.__class__, '_pidfile') and self.__class__._pidfile:
            self._set_pidfile(self.__class__._pidfile)
        else:
            self._set_pidfile(
                os.path.join(
                    tempfile.gettempdir(), self.__class__.__name__.lower()
                ) + '.pid'
            )

    ###################################
    # Object deletion                 #
    ###################################

    ###################################
    # Abstract methods                #
    ###################################

    @abc.abstractmethod
    def _on_configuration_loaded(self, **config_data):
        """
Applies the configuration to the instance. Since there are configuration values 
that may exist for any instance of the class, this method should be called by 
derived classes in addition to any local configuration.
"""
        # - Find and handle any daemonizable-specific configuration values:
        self.info('config_data ..... %s' % config_data)
        daemon_config = config_data.get('daemon')
        self.info('daemon_config ... %s' % daemon_config)
        # - stderr
        self.debug('Configuration stderr ... %s' % (daemon_config.get('stderr')))
        if daemon_config.get('stderr'):
            self._set_stderr(daemon_config['stderr'])
        # - stdin
        self.debug('Configuration stdin .... %s' % (daemon_config.get('stdin')))
        if daemon_config.get('stdin'):
            self._set_stdin(daemon_config['stdin'])
        # - stdout
        self.debug('Configuration stdout ... %s' % (daemon_config.get('stdout')))
        if daemon_config.get('stdout'):
            self._set_stdout(daemon_config['stdout'])
        # - Call the parent method to perform common logging set-up
        BaseDaemon._on_configuration_loaded(self, **config_data)

    @abc.abstractmethod
    def main(self):
        """
The main event-loop (or whtever is equivalent) for the service instance.

NOTE: It's apparent that BaseDaemonizable instances, if their main loop uses 
      any print() calls, will stop functioning and die silently if their 
      calling environment (terminal, whatever) is terminated, so *don't 
      print() anything* here.
"""
        raise NotImplementedError(
            '%s.main has not been implemented as required by '
            'BaseDaemon' % (self.__class__.__name__)
        )

    ###################################
    # Instance methods                #
    ###################################

    def daemonize(self):
        """
Daemonizes the service/daemon process using the "UNIX double-fork magic" trick. 
See 
- Stevens' "Advanced Programming in the UNIX Environment" for details 
  (ISBN 0201563177)
  http://www.erlenstar.demon.co.uk/unix/faq_2.html#SEC16
- Sander Marechal's Daemon class
  https://gist.github.com/TrafalgarLiu/e9f5b33464ac78fa7fc4
"""
        self.info('%s.daemonize called' % (self.__class__.__name__))
        try:
            # - Try to fork and exit the current process
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError as error:
            # If it fails, we need to report why and exit...
            self.error(
                'Initial process-fork of %s failed with %s: %s' % 
                (self.__class__.__name__, error.__class__.__name__, error)
            )
            sys.exit(error.errno)
        self.debug('+- Initial fork completed')
        # - The original code this is based on includes code at this point to
        #   "decouple from the parent environment" which may or may not be 
        #   needed:
        #   - Changing the current/runtime directory
        #     os.chdir('/')
        #   - Breaking any terminal connection, allowing the daemon-process to 
        #     continue even if a calling terminal is shut down
        os.setsid()
        #   - Calling os.umask to set the permissions-mask for files created by
        #     the process
        #     os.umask(0)
        self.debug('+- Decoupling from parent environment complete')
        try:
            # - Try to fork and exit the just-created/-forked process
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError as error:
            # If it fails, we need to report why and exit...
            print(
                'Second process-fork of %s failed with %s: %s' % 
                (self.__class__.__name__, error.__class__.__name__, error)
            )
            sys.exit(error.errno)
        self.debug('+- Second fork completed')
        # - The original code this is based on includes code at this point to 
        #   deal with stdin, stdout and stderr redirection, which may or may 
        #   not be needed.
        # - Write the PID file for the instance
        pid = os.getpid()
        fp = open(self.pidfile, 'w')
        fp.write(str(pid))
        fp.close()
        self.debug('+- PID (%s) written to %s' % (pid, self.pidfile))
        # - Register the del_pidfile method to remove the pid-file when the 
        #   process stops:
        atexit.register(self.del_pidfile)
        self.info('%s.daemonize complete' % (self.__class__.__name__))

    def del_pidfile(self):
        os.unlink(self.pidfile)

    def preflight(self):
        """
Performs any of the various pre-flight operations needed
"""
        self.info('%s.preflight called' % (self.__class__.__name__))
        if self.stderr:
            self.debug('+- Redirecting stderr to %s' % self.stderr)
            # - Flush it first
            sys.stderr.flush()
            # - Open the stderr file for append
            sys.stderr = open(self.stderr, 'a+')
        if self.stdin:
            self.debug('+- Redirecting stdin to %s' % self.stdin)
            # - Open the file for read
            if not os.path.exists(self.stdin):
                fp = open(self.stdin, 'a')
                fp.close()
            sys.stdin = open(self.stdin, 'r')
        if self.stdout:
            self.debug('+- Redirecting stdout to %s' % self.stdout)
            # - Flush it first
            sys.stdout.flush()
            # - Open the stdout file for append
            sys.stdout = open(self.stdout, 'a+')
        self.info('%s.preflight complete' % (self.__class__.__name__))

    def start(self):
        if self._running:
            self.info(
                '%s instance is already running' % (self.__class__.__name__)
            )
            return
        self.daemonize()
        self.preflight()
        self.info('Starting %s.main' % self.__class__.__name__)
        self.main()
        self.cleanup()

    ###################################
    # Overrides of built-in methods   #
    ###################################

    ###################################
    # Class methods                   #
    ###################################

    ###################################
    # Static methods                  #
    ###################################

#######################################
# Concrete classes                    #
#######################################

#######################################
# Initialization needed after member  #
#   definition is complete            #
#######################################

#######################################
# Imports needed after member         #
#   definition (to resolve circular   #
#   dependencies - avoid if at all    #
#   possible                          #
#######################################

#######################################
# Code to execute if the module is    #
#   called directly                   #
#######################################

if __name__ == '__main__':
    pass
