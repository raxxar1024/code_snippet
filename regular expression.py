# -*- coding: utf-8 -*-
import re

url = '/plan_edit_63?msg_id=60'

# pattern = re.compile(r'/plan_edit_\d+\?msg_id=\d+')
pattern = re.compile(r'\d+')
match = pattern.findall(url)
if match:
    print match

