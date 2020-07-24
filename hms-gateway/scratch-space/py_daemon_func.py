#!/usr/bin/env python
"""
A simple daemon-like function that can be started from the command-line.
"""

import syslog

from time import sleep

def main_program():
    iterations = 0
    syslog.syslog('Starting %s' % __file__)
    while True:
        # TODO: Perform whatever request-acquisition and response-
        #       generation is needed here...
        syslog.syslog('Event Loop (%d)' % iterations)
        sleep(10)
        iterations += 1
    syslog.syslog('Exiting %s' % __file__)

if __name__ == '__main__':
    main_program()
