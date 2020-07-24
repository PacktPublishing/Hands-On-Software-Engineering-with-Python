#!/usr/bin/env python

from setuptools import setup

# The actual setup function call:
setup(
    name='HMS-Central-Office-Application',
    version='0.1.dev0',
    author='Brian D. Allbee',
    description='',
    package_dir={
        'hms_co':'src',
        # ...
    },
    # Can also be automatically generated using 
    #     setuptools.find_packages...
    packages=[
        'hms_co',
        # ...
    ],
    package_data={
#        'hms_co':[
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
