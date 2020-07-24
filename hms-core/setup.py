#!/usr/bin/env python

import sys
sys.path.append('../standards')
sys.path.append('tests/test_hms_core')

from setuptools import setup

# The actual setup function call:
setup(
    name='HMS-Core',
    version='0.1.dev0',
    author='Brian D. Allbee',
    description='',
    package_dir={
        '':'src',
        # ...
    },
    # Can also be automatically generated using 
    #     setuptools.find_packages...
    packages=[
        'hms_core',
        # ...
    ],
    package_data={
#        'hms_core':[
#            'filename.ext',
#            # ...
#        ]
    },
    entry_points={
#        'console_scripts':[
#            'executable_name = namespace.path:function',
#            # ...
#        ],
    },
    test_suite='tests.test_hms_core',
)
