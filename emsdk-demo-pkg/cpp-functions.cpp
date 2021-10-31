#include <iostream>
#include <zlib.h>

#include <emscripten/bind.h>

using namespace emscripten;

void ZlibVersion(){
  std::cout << "Using zlib version: " << zlibVersion() << std::endl;
}

EMSCRIPTEN_BINDINGS(cpp_functions) {
    function("ZlibVersion", &ZlibVersion);
}
