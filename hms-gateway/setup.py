#!/usr/bin/env python

from setuptools import setup

# The actual setup function call:
setup(
    name='HMS-Artisan-Gateway',
    version='0.1.dev0',
    author='Brian D. Allbee',
    description='',
    package_dir={
        'hms_gateway':'src',
        # ...
    },
    # Can also be automatically generated using 
    #     setuptools.find_packages...
    packages=[
        'hms_gateway',
        # ...
    ],
    package_data={
#        'hms_gateway':[
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
)
