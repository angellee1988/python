#!/usr/bin/python

import re

pattern = re.compile(r'\d+')
m = pattern.match('one12twothree34four')
print(m)
