cmake_minimum_required(VERSION 3.10)
project(Homework02_3)

set(CMAKE_CXX_STANDARD 17)

add_subdirectory(external)

find_package(OpenGL REQUIRED)

set(libs
        ${OPENGL_LIBRARY}
        glfw
        glad
        glm
)

set(UTILS_DIR ${CMAKE_SOURCE_DIR}/src/utils)
FILE(GLOB_RECURSE UTILS_SRC "${UTILS_DIR}/*.cpp" "${UTILS_DIR}/*.h")

set(HOMEWORKS TexturedRectangles TexturedSquareAnimation)

foreach(hw ${HOMEWORKS})
    set(HW_DIR src/${hw})

    FILE(GLOB_RECURSE HW_SRC
            "${HW_DIR}/*.cpp"
            "${HW_DIR}/*.h"
    )

    add_executable(${hw} ${HW_SRC} ${UTILS_SRC})

    target_link_libraries(${hw} ${libs})
    target_include_directories(${hw} PRIVATE ${UTILS_DIR})

    add_custom_command(
            TARGET ${hw} POST_BUILD
            COMMAND ${CMAKE_COMMAND} -E copy_directory
            "${CMAKE_SOURCE_DIR}/${HW_DIR}/res"
            "$<TARGET_FILE_DIR:${hw}>/res"
            COMMENT "Copying resources for ${hw}..."
    )
endforeach()