#!/usr/bin/env python

import re

from email.utils import parseaddr

EMAIL_CHECK = re.compile(
    r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
)

for value in [
    'brian.allbee@gmail.com',
    'brian.allbee+hosep-test@gmail.com',
    'flobnar'
    ]:
    try:
        check_value = parseaddr(value)[1]
        valid = (check_value != '')
        if valid:
            remnant = EMAIL_CHECK.sub('', check_value)
            print('remnant ... %s' % remnant)
            if not remnant:
                print('%s was valid' % value)
            else:
                raise ValueError(
                    '%s was invalid after regex (%s [%s])' % 
                    (value, check_value, remnant)
                )
        else:
            raise ValueError(
                '%s was invalid after parseaddr (%s)' % 
                (value, check_value)
            )
    except Exception as error:
        print(error)
