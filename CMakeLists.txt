cmake_minimum_required(VERSION 3.16)

project(obd2-linux
    VERSION 0.1.0
    LANGUAGES C
)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_C_EXTENSIONS OFF)

add_library(obd2
    src/obd2.c
)

target_include_directories(obd2
    PUBLIC
        ${PROJECT_SOURCE_DIR}/include
)

add_executable(obd2_example
    example/obd2_example.c
)

target_link_libraries(obd2_example
    PRIVATE
        obd2
)