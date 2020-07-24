#!/usr/bin/env python

import configparser

config = configparser.ConfigParser()
config.read('myservice.ini')
    
for section in config:
    # - Show each section's name
    print(('-- %s ' % section).ljust(80, '-'))
    section = config[section]
    # - Show each configured value in the section
    for key in section:
        value = section.get(key)
        print(
            (' + %s ' % key).ljust(24, '.') 
            + ' (%s) %s' % (
                type(value).__name__, value
            )
        )
    print()
