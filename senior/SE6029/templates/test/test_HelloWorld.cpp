// include necessary headers for testing
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

// main function for running tests
int main() {
    // run the test function
    testHelloWorld();

    return 0;
}
