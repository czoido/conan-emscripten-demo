#include <stdio.h>
#include <zlib.h>

#include <emscripten.h>

EMSCRIPTEN_KEEPALIVE
const char * ZlibVersion() {
  return zlibVersion();
}
