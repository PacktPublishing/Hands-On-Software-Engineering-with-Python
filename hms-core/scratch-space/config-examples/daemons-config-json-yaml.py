#!/usr/bin/env python

import json, yaml

CONFIG={
    'logging':{
        'name':'daemon-name',
        'format':'%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        'file':{
            'logfile':'/var/log/daemon-name.log',
            'level':'debug',
        },
        'console':{
            'level':'error',
        }
    },
}


# - Convert to JSON
with open('example-config.json', 'w') as fp:
    json.dump(CONFIG, fp, indent=4)

# - Convert to YAML
with open('example-config.yaml', 'w') as fp:
    yaml.dump(CONFIG, fp, default_flow_style=False)
