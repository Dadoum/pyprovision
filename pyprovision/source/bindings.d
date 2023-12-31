module bindings;

version = Python_3_0_Or_Later;
version = PydPythonExtension;

import deimos.python.Python;
import pyd.pyd;

import provision;

extern(C) void PydMain() {
    module_init();
    wrap_class!(
        ADI,
        PyName!"ADI",
        // Docstring!"",
        Init!(string),
        Property!(ADI.provisioningPath, PyName!"provisioning_path"),
        Property!(ADI.identifier, PyName!"identifier"),
        Def!(ADI.loadLibrary, PyName!"load_library"),
        Def!(ADI.eraseProvisioning, PyName!"erase_provisioning"),
        Def!(ADI.synchronize, PyName!"synchronize"),
        Def!(ADI.destroyProvisioning, PyName!"destroy_provisioning"),
        Def!(ADI.endProvisioning, PyName!"end_provisioning"),
        Def!(ADI.startProvisioning, PyName!"start_provisioning"),
        Def!(ADI.isMachineProvisioned, PyName!"is_machine_provisioned"),
        Def!(ADI.dispose, PyName!"dispose"),
        Def!(ADI.requestOTP, PyName!"request_otp"),
    )();
    wrap_class!(
        ADI.OneTimePassword,
        PyName!"OneTimePassword",
        Property!(ADI.OneTimePassword.oneTimePassword, PyName!"one_time_password"),
        Property!(ADI.OneTimePassword.machineIdentifier, PyName!"machine_identifier")
    )();
    wrap_class!(
        ADI.ClientProvisioningIntermediateMetadata,
        PyName!"ClientProvisioningIntermediateMetadata",
        Property!(ADI.ClientProvisioningIntermediateMetadata.clientProvisioningIntermediateMetadata, PyName!"client_provisioning_intermediate_metadata"),
        Property!(ADI.ClientProvisioningIntermediateMetadata.session, PyName!"session")
    )();
    wrap_class!(
        ADI.SynchronizationResumeMetadata,
        PyName!"SynchronizationResumeMetadata",
        Property!(ADI.SynchronizationResumeMetadata.synchronizationResumeMetadata, PyName!"synchronization_resume_metadata"),
        Property!(ADI.SynchronizationResumeMetadata.machineIdentifier, PyName!"machine_identifier")
    )();
    
    wrap_class!(
        Device,
        PyName!"Device",
        Init!(string),
        Property!(Device.uniqueDeviceIdentifier, PyName!"unique_device_identifier"),
        Property!(Device.serverFriendlyDescription, PyName!"server_friendly_description"),
        Property!(Device.adiIdentifier, PyName!"adi_identifier"),
        Property!(Device.localUserUUID, PyName!"local_user_uuid"),
        Property!(Device.initialized, PyName!"initialized"),
        Def!(Device.write, PyName!"write"),
    )();

    wrap_class!(
        ProvisioningSession,
        PyName!"ProvisioningSession",
        Init!(ADI, Device),
        Def!(ProvisioningSession.loadURLBag, PyName!"load_url_bag"),
        Def!(ProvisioningSession.provision, PyName!"provision"),
    )();
}

import pyd.def;
import pyd.exception;
import pyd.thread;
import deimos.python.Python;
import core.runtime;

extern(C) shared bool _D2rt6dmain212_d_isHaltingOb;
alias _D2rt6dmain212_d_isHaltingOb _d_isHalting;
extern(C) {

    void rt_init();
    void rt_term();

    pragma(crt_constructor)
    void hacky_init() {
        rt_init();
    }

    pragma(crt_destructor)
    void hacky_fini() {
        if(!_d_isHalting){
            rt_term();
        }
    }

} /* extern(C) */

extern(C) export PyObject* PyInit_pyprovision() {
    return pyd.exception.exception_catcher(delegate PyObject*() {
        pyd.thread.ensureAttached();
        pyd.def.pyd_module_name = "pyprovision";
        PydMain();
        return pyd.def.pyd_modules[""];
    });
}
