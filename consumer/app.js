const c_funtions = require('./bin/c-functions.js');
const cpp_funtions = require('./bin/cpp-functions.js')

c_funtions().then((instance) => {
    instance._ZlibVersion(); // direct calling works
    instance.ccall("ZlibVersion"); // using ccall etc. also work
});

cpp_funtions.onRuntimeInitialized = async _ => {
    cpp_funtions.ZlibVersion();
}
