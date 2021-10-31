#include <stdio.h>
#include <zlib.h>

#include <emscripten.h>

EMSCRIPTEN_KEEPALIVE
void ZlibVersion() {
  printf ("Using zlib version: %s in C\n", zlibVersion());
}
