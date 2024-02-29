# `C++` Project Templates 


## Project Structure

```
PROJECT_ROOT
├── bin/
│   └── main.out
├── include/
│   └── HelloWorld.h
├── src/
│   ├── HelloWorld.cpp
│   └── main.cpp
├── test/
│   └── test_HelloWorld.cpp
├── build.sh
└── README.md
```


## How to **compile and execute** the `MAIN PROGRAM` with this templates?
```sh
g++ -Iinclude -o src/*.cpp -o bin/main.out && ./bin/main.out
```

### with the test
```sh
# compile main program
g++ -Iinclude src/*.cpp -o bin/main.out

# compile test program
g++ -Iinclude test/test_HelloWorld.cpp src/HelloWorld.cpp -o bin/test.out

# run test program
./bin/test.out
```


### `bin/`

This directory contains the compiled binary file of the project.

### `include/`

This directory contains the header files of the project.

#### `HelloWorld.h`
```cpp
#ifndef HELLOWORLD_H
#define HELLOWORLD_H

void helloWorld();

#endif
```

### `src/`

This directory contains the source files of the project.

#### `HelloWorld.cpp`
```cpp
#include "HelloWorld.h"
#include <iostream>

void helloWorld() {
    std::cout << "Hello, World!" << std::endl;
}
```

#### `main.cpp`
```cpp
#include "HelloWorld.h"

int main() {
    helloWorld();
    return 0;
}
```

### `test/`

This directory contains the test files of the project.

#### `test_HelloWorld.cpp`
```cpp
#include <iostream>
#include <sstream> 
#include "HelloWorld.h"

void testHelloWorld() {
    // create an output stream to capture console output
    std::stringstream out;

    // redirect std::cout to the output stream
    std::streambuf* coutBuf = std::cout.rdbuf();
    std::cout.rdbuf(out.rdbuf());

    // call the function to be tested
    helloWorld();

    // restore the original std::cout
    std::cout.rdbuf(coutBuf);

    // check if the output matches the expected output
    if (out.str() == "Hello, World!\n") {
        std::cout << "Test Passed: HelloWorld() function produces correct output." << std::endl;
    } else {
        std::cout << "Test Failed: HelloWorld() function produces incorrect output." << std::endl;
    }
}

int main() {
    testHelloWorld();

    return 0;
}
```
