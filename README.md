# conan-emscripten-demo

Create both C and C++ functions, compile them using emscripten with Conan using emsdk package and consume those functions from NodeJS.

```bash
conan create emsdk-demo-pkg --profile:host=conan-profiles/emscripten.profile --profile:build=default --build=missing
cd consumer
conan install conanfile.txt --profile:host=../conan-profiles/emscripten.profile --profile:build=default
node app.js
```
