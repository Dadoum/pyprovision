from os.path import expanduser

from pyprovision import *

adi = ADI(expanduser("~/.config/Sideloader/lib/"))
adi.provisioning_path = "./test/"

device = Device(expanduser("~/.config/Sideloader/device.json"))
if not device.initialized:
    pass # TODO implement that in the example

provisioning_session = ProvisioningSession(adi, device)
# DOES NOT WORK, DO THE REQUESTS YOURSELF
# provisioning_session.provision(c_ulonglong(-2).value)
