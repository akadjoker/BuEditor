cmake_minimum_required(VERSION 3.20)
cmake_policy(SET CMP0072 NEW)

project(BuEditor VERSION 0.1.0)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/bin)

set(SDL2_DISABLE_INSTALL ON CACHE BOOL "Disable SDL2 install rules" FORCE)
set(SDL_SHARED OFF CACHE BOOL "Disable SDL shared library" FORCE)
set(SDL_STATIC ON CACHE BOOL "Enable SDL static library" FORCE)
set(SDL_TEST OFF CACHE BOOL "Disable SDL test library" FORCE)
set(SDL_TESTS OFF CACHE BOOL "Disable SDL test programs" FORCE)
set(SDL_AUDIO OFF CACHE BOOL "Disable SDL audio subsystem" FORCE)
set(SDL_HAPTIC OFF CACHE BOOL "Disable SDL haptic subsystem" FORCE)
set(SDL_SENSOR OFF CACHE BOOL "Disable SDL sensor subsystem" FORCE)
set(SDL_VULKAN OFF CACHE BOOL "Disable SDL Vulkan support" FORCE)
set(SDL_KMSDRM OFF CACHE BOOL "Disable SDL KMSDRM video backend" FORCE)
set(SDL_KMSDRM_SHARED OFF CACHE BOOL "Disable SDL KMSDRM shared loading" FORCE)
set(SDL_RPI OFF CACHE BOOL "Disable SDL Raspberry Pi backend" FORCE)
set(SDL_VIVANTE OFF CACHE BOOL "Disable SDL Vivante backend" FORCE)
set(SDL_OFFSCREEN OFF CACHE BOOL "Disable SDL offscreen backend" FORCE)

add_subdirectory(vendor/imgui)
add_subdirectory(vendor/SDL)

set(BUEDITOR_SOURCES
    ${CMAKE_CURRENT_SOURCE_DIR}/src/main.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/src/DocumentSymbols.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/src/GifRecorder.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/src/ImGuiConsole.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/src/ImGuiFileDialog.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/src/TextEditor.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/src/LanguageDefinitions.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/src/imgui_impl_sdl2.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/src/imgui_impl_opengl3.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/src/vendor/regex/src/regex.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/src/vendor/regex/src/static_mutex.cpp
)

add_executable(BuEditor ${BUEDITOR_SOURCES})
set_target_properties(BuEditor PROPERTIES OUTPUT_NAME "bueditor")

target_include_directories(BuEditor PRIVATE
    ${CMAKE_SOURCE_DIR}/vendor/imgui
    ${CMAKE_CURRENT_SOURCE_DIR}/src
    ${CMAKE_CURRENT_SOURCE_DIR}/src/vendor
    ${CMAKE_CURRENT_SOURCE_DIR}/src/vendor/regex/include
)

target_compile_definitions(BuEditor PRIVATE BOOST_REGEX_STANDALONE BOOST_REGEX_NO_LIB)

if(WIN32)
    target_compile_definitions(BuEditor PRIVATE WINGDIAPI=)
    if(NOT MSVC)
        target_compile_options(BuEditor PRIVATE -U_DLL)
    endif()
endif()

target_link_libraries(BuEditor PRIVATE imgui SDL2::SDL2-static)

if(WIN32)
    target_link_libraries(BuEditor PRIVATE opengl32)

    if(TARGET SDL2::SDL2main)
        target_link_libraries(BuEditor PRIVATE SDL2::SDL2main)
    endif()

    if(MSVC)
        target_link_libraries(BuEditor PRIVATE Winmm.lib)
    else()
        target_link_libraries(BuEditor PRIVATE winmm)
    endif()
else()
    target_link_libraries(BuEditor PRIVATE GL m)
endif()
