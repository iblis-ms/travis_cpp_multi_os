
cmake_minimum_required(VERSION 2.8.7)

project(TravisMultiOs CXX)

set(PROGRAM_NAME "${PROJECT_NAME}_${CMAKE_SYSTEM_NAME}_${CMAKE_CXX_COMPILER_ID}")

message(STATUS "Program name: ${PROGRAM_NAME}")
add_executable(${PROGRAM_NAME} main.cpp)
