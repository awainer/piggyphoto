from __future__ import print_function
import piggyphoto
from pprint import pprint
C = piggyphoto.Camera()

pprint(C.list_files("/store_00020001/DCIM/100CANON"))
pprint(C.list_folders("/store_00020001/DCIM/100CANON"))

C.close()