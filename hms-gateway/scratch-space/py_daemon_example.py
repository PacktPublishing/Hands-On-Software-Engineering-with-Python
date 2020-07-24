#!/usr/bin/env python
"""
A bare-bones daemon implementation.
"""

import syslog

from daemon import DaemonContext
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
    with DaemonContext():
        main_program()
