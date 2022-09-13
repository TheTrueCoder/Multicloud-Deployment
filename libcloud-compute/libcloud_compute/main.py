# import requests_debugger
# requests_debugger.set(max_depth=10)

from pprint import pprint
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
from libcloud.compute.base import NodeAuthPassword

import secret

to_drive = get_driver(Provider.VULTR)
drive = to_drive(secret.vultr_key)

# to_drive = get_driver(Provider.DIGITAL_OCEAN)
# drive = to_drive(secret.do_key, api_version="v2")

def filter_id(list_val: list, filter, property: str = 'id'):
    for item in list_val:
        if property == 'id':
            if item.id == filter:
                return item
        elif property == 'name':
            if filter in item.name:
                return item

# def test(a):
#     if 'Ubuntu 20.04' in a.name:
#         return True

# pprint(list(filter(test, drive.list_images())))
# pprint(drive.list_locations())

size = drive.list_sizes()[0]
image = filter_id(drive.list_images(), 'Ubuntu 20.04 LTS', 'name')
location = filter_id(drive.list_locations(), 'nyc1')
# 'syd'

pprint(location)
pprint(size)
pprint(image)

auth = NodeAuthPassword('averysecretpw')
node = drive.create_node("hello", size, image, location, auth)
