#!/usr/bin/env python

import re

URL_CHECK = re.compile(
    r'(^https?://[A-Za-z0-9][-_A-Za-z0-9]*\.[A-Za-z0-9][-_A-Za-z0-9\.]*$)'
)

for value in [
    'https://cxos.io',
    'http://www.google.com',
    'https://',
    'ook.com',
    ]:
    try:
        remnant = URL_CHECK.sub('', value)
        print('remnant ... %s' % remnant)
        if not remnant:
            print('%s was valid' % value)
        else:
            raise ValueError(
                '%s was invalid after regex (%s)' % 
                (value, remnant)
            )
    except Exception as error:
        print(error)
    print()
