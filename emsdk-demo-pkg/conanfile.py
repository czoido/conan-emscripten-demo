from conans import ConanFile, CMake


class ConanEmsdkDemo(ConanFile):
    name = "emsdk-demo-pkg"
    version = "0.1"
    description = "Simple demo with emsdk from c3i"
    topics = ("conan", "emscripten", "javascript")
    license = "MIT"
    url = "https://github.com/czoido/conan-emscripten-demo"
    homepage = "https://github.com/czoido/conan-emscripten-demo"
    settings = {"os": ["Emscripten"]}
    requires = "zlib/1.2.11"
    exports_sources = ["CMakeLists.txt", "cpp-functions.cpp", "c-functions.c"]
    generators = ["cmake"]

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()
