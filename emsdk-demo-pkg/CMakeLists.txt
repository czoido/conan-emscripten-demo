cmake_minimum_required(VERSION 2.8)

project(ConanHello)

include(conanbuildinfo.cmake)
conan_basic_setup()

add_executable(c-functions c-functions.c)
target_include_directories(c-functions PRIVATE ${CONAN_INCLUDE_DIRS})
target_link_libraries(c-functions PRIVATE ${CONAN_LIBS})
set_target_properties(c-functions PROPERTIES LINK_FLAGS "-o c-functions.js -s MODULARIZE -s EXPORTED_RUNTIME_METHODS=['ccall','cwrap']")

install(TARGETS c-functions
  RUNTIME DESTINATION bin
  LIBRARY DESTINATION lib
  ARCHIVE DESTINATION lib)
  
install(FILES
  ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/c-functions.js
  ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/c-functions.wasm
  DESTINATION bin)

add_executable(cpp-functions cpp-functions.cpp)
target_include_directories(cpp-functions PRIVATE ${CONAN_INCLUDE_DIRS})
target_link_libraries(cpp-functions PRIVATE ${CONAN_LIBS})
set_target_properties(cpp-functions PROPERTIES LINK_FLAGS "--bind -o cpp-functions.js -s EXPORTED_FUNCTIONS=[] -s EXPORTED_RUNTIME_METHODS=['ccall','cwrap']")

install(TARGETS cpp-functions
  RUNTIME DESTINATION bin
  LIBRARY DESTINATION lib
  ARCHIVE DESTINATION lib)
  
install(FILES
  ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/cpp-functions.js
  ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/cpp-functions.wasm
  DESTINATION bin)
