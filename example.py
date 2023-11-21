from os.path import expanduser
from ctypes import c_ulonglong

from pyprovision import *

adi = ADI(expanduser("~/.config/Sideloader/lib/"))
adi.provisioning_path = expanduser("~/.config/Sideloader")

device = Device(expanduser("~/.config/Sideloader/device.json"))
if not device.initialized:
    pass # TODO implement that in the example

adi.identifier = device.adi_identifier
dsid = c_ulonglong(-2).value
print(adi.is_machine_provisioned(dsid))
print(adi.request_otp(dsid).one_time_password)
provisioning_session = ProvisioningSession(adi, device)
# DOES NOT WORK, DO THE REQUESTS YOURSELF
# provisioning_session.provision(c_ulonglong(-2).value)
