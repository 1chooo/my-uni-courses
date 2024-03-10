# compile main program
g++ -Iinclude src/*.cpp -o bin/main.out

# compile test program
g++ -Iinclude test/test_HelloWorld.cpp src/HelloWorld.cpp -o bin/test.out

# run test program
./bin/test.out
