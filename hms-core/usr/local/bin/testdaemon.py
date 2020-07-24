#!/usr/bin/env python

# - Import the service-class
from some_package import testdaemon

# - The location of the config-file
config_file = '/path/to/config.yaml'
# - Create an instance of the service class
d = testdaemon(config_file)
# - Start it.
d.start()
