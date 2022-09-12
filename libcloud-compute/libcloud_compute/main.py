from email.mime import image
from pprint import pprint

from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
from libcloud.compute.base import NodeAuthPassword

import secret

to_drive = get_driver(Provider.VULTR)
drive = to_drive(secret.vultr_key)

def filter_id(list_val: list, filter, property: str = 'id'):
    for item in list_val:
        if item[property] == filter:
            return item

size = drive.list_sizes()[0]
image = filter_id(drive.list_images(), 'Ubuntu 20.04 LTS x64', 'name')


pprint(drive.list_locations())
pprint(size)
pprint(image)

auth = NodeAuthPassword('averysecretpw')
node = drive.create_node("MagicNode", size, image, )
