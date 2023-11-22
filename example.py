from os.path import expanduser
from ctypes import c_ulonglong

from pyprovision import *

import uuid
import secrets

# path to the folder containing libstoreservicescore and libCoreADI for your architecture!!
adi = ADI("./libraries/")
# where adi.pb will be stored
adi.provisioning_path = "./adi-data/"

# where apple device info will be stored (to persist adi data across sessions)
# device = Device("./example-device.json")
if not device.initialized:
    # Pretend to be a MacBook Pro
    device.server_friendly_description = "<MacBookPro13,2> <macOS;13.1;22C65> <com.apple.AuthKit/1 (com.apple.dt.Xcode/3594.4.19)>"
    device.unique_device_identifier = str(uuid.uuid4()).upper()
    device.adi_identifier = secrets.token_hex(8).lower()
    device.local_user_uuid = secrets.token_hex(32).upper()

# we re-use the identifier from the device we saved
adi.identifier = device.adi_identifier
# DSID (default store identifier iirc), is -2 for production servers apparently
dsid = c_ulonglong(-2).value

print("Is it provisioned? ", adi.is_machine_provisioned(dsid))
print("(re)provisioning...")

provisioning_session = ProvisioningSession(adi, device)
provisioning_session.provision(dsid)

print("Is it provisioned? ", adi.is_machine_provisioned(dsid))
otp = adi.request_otp(dsid)
print("OTP: ", otp.one_time_password, ", MID: ", otp.machine_identifier)

