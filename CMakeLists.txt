cmake_minimum_required(VERSION 3.10)
project(fhe_house_price_prediction)

set(CMAKE_CXX_STANDARD 17)

# Find OpenFHE
find_package(OpenFHE REQUIRED)

if(OpenFHE_FOUND)
    include_directories(${OpenFHE_INCLUDE_DIRS})
    link_directories(${OpenFHE_LIBRARY_DIRS})
    add_executable(fhe_inference main.cpp)
    target_link_libraries(fhe_inference OpenFHE::openfhe)
else()
    message(FATAL_ERROR "OpenFHE not found. Please install OpenFHE and set the OpenFHE_DIR variable.")
endif()