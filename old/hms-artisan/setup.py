#!/usr/bin/env python

from setuptools import setup

# The actual setup function call:
setup(
    name='HMS-Artisan-Application',
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
        'hms_artisan',
        # ...
    ],
    package_data={
#        'hms_artisan':[
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
