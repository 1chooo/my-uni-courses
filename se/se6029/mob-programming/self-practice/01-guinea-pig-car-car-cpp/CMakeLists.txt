cmake_minimum_required(VERSION 3.26)
project(guinea-pig-car-car VERSION 0.0.1 DESCRIPTION "Mob Programming Guinea Pig Car Car")

set(CMAKE_CXX_STANDARD 17)

include_directories(inc)  # 添加 inc 目錄以便能夠找到 .h 檔案

# add_executable(guinea-pig-car-car src/main.cpp src/calc.cpp src/car.cpp src/ambulance.cpp src/police_car.cpp src/trash_truck.cpp)
file(GLOB SOURCES "src/*.cpp")  # Use a wildcard to include all .cpp files in src directory

add_executable(guinea-pig-car-car ${SOURCES})