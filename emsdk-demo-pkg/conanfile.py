from conans import ConanFile
from conan.tools.cmake import CMake


class ConanEmsdkDemo(ConanFile):
    name = "emsdk-demo-pkg"
    version = "0.1"
    description = "Simple demo with emsdk from c3i"
    topics = ("conan", "emscripten", "javascript")
    license = "MIT"
    url = "https://github.com/czoido/conan-emscripten-demo"
    homepage = "https://github.com/czoido/conan-emscripten-demo"
    settings = "os", "arch", "compiler", "build_type"
    requires = "zlib/1.2.11"
    exports_sources = ["CMakeLists.txt", "cpp-functions.cpp", "c-functions.c"]
    generators = "CMakeDeps", "CMakeToolchain"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.install()
