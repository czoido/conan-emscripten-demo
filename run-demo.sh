conan create emsdk-demo-pkg --profile:host=conan-profiles/emscripten.profile --profile:build=default --build=missing
cd consumer
conan install conanfile.txt --profile:host=../conan-profiles/emscripten.profile --profile:build=default
node app.js