const c_funtions = require('./c-functions.js');
const cpp_funtions = require('./cpp-functions.js')

c_funtions().then((instance) => {
    instance._zlibversion(); // direct calling works
    instance.ccall("zlibversion"); // using ccall etc. also work
});

cpp_funtions.onRuntimeInitialized = async _ => {
    cpp_funtions.zlibversion();
}
