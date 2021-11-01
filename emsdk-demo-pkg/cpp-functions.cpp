#include <iostream>
#include <zlib.h>

#include <emscripten/bind.h>

using namespace emscripten;

std::string ZlibVersion(){
  return std::string(zlibVersion());
}

EMSCRIPTEN_BINDINGS(cpp_functions) {
    function("ZlibVersion", &ZlibVersion);
}
