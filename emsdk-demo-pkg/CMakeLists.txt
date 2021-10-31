cmake_minimum_required(VERSION 3.15)

project(ConanHello)

find_package(ZLIB REQUIRED)

add_executable(c-functions c-functions.c)
set_target_properties(c-functions PROPERTIES LINK_FLAGS "-s MODULARIZE -s EXPORTED_RUNTIME_METHODS=['ccall','cwrap']")
set_target_properties(c-functions PROPERTIES SUFFIX ".js")
target_link_libraries(c-functions PRIVATE zlib::zlib)

install(TARGETS c-functions
  RUNTIME DESTINATION bin
  LIBRARY DESTINATION lib
  ARCHIVE DESTINATION lib)
  
install(FILES
  c-functions.js
  c-functions.wasm
  DESTINATION bin)

add_executable(cpp-functions cpp-functions.cpp)
set_target_properties(cpp-functions PROPERTIES LINK_FLAGS "--bind -s EXPORTED_FUNCTIONS=[] -s EXPORTED_RUNTIME_METHODS=['ccall','cwrap']")
set_target_properties(cpp-functions PROPERTIES SUFFIX ".js")
target_link_libraries(cpp-functions PRIVATE zlib::zlib)

install(TARGETS cpp-functions
  RUNTIME DESTINATION bin
  LIBRARY DESTINATION lib
  ARCHIVE DESTINATION lib)
  
install(FILES
  cpp-functions.js
  cpp-functions.wasm
  DESTINATION bin)
