#include <iostream>
#include <zlib.h>

#include <emscripten/bind.h>

using namespace emscripten;

void ZlibVersion(){
  std::cout << "Using zlib version: " << zlibVersion() << " in C++" << std::endl;
}

EMSCRIPTEN_BINDINGS(cpp_functions) {
    function("ZlibVersion", &ZlibVersion);
}
