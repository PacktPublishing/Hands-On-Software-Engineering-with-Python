#!/usr/bin/env python

import logging

# - Define a format for log-output
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
# - Get a logger. Once defned anywhere, loggers (with all their 
#   settings and attached formats and handlers) can be retrieved 
#   elsewhere by getting a logger instance using the same name.
logger = logging.getLogger('logging-example')
logger.setLevel(logging.DEBUG)
# - Create a file-handler to write log-messages to a file
file_handler = logging.FileHandler('example.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
# - Attach handler to logger
logger.addHandler(file_handler)

# - Log some messages to show that it works:
logger.critical('This is a CRITICAL-level message')
logger.debug('This is a DEBUG-level message')
logger.error('This is an ERROR-level message')
logger.info('This is an INFO-level message')
logger.warn('This is a WARNING-level message')


def some_function(*args, **kwargs):
    logger.info('some_function(%s, %s) called' % (str(args), str(kwargs)))
    if not args and not kwargs:
        logger.warn(
            'some_function was called with no arguments'
        )
    elif args:
        logger.debug('*args exists: %s' % (str(args)))
        try:
            x, y = args[0:2]
            logger.debug('x = %s, y = %s' % (x, y))
            return x / y
        except ValueError as error:
            logger.error(
                '%s: Could not get x and y values from '
                'args %s' % 
                (error.__class__.__name__, str(args))
            )
        except Exception as error:
            logger.error(
                '%s in some_function: %s' % 
                (error.__class__.__name__, error)
            )
    logger.info('some_function complete')

logger.info('Calling with no arguments')
some_function()
logger.info('Calling with x and y values')
some_function(1,2)
logger.info('Calling with a bad y-value')
some_function(1,0)
