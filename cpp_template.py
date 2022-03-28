#!/usr/bin/python3
import argparse
import os
import shutil
import re

def replace_file(file_path, project_name):
    pat_lc = 'momo'
    pat_uc = 'MOMO'

    with open(file_path, 'r+', encoding='utf-8') as file:
        content = file.read()
        content = re.sub(pat_lc, project_name.lower(), content)
        content = re.sub(pat_uc, project_name.upper(), content)

        # Clear file and insert the new content
        file.seek(0)
        file.truncate(0)
        file.write(content)




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", help = "project name")
    args = parser.parse_args()

    # Name argument must be set
    if not args.name:
        print('Please provide a project name.')
        exit(1)

    cwd = os.getcwd()
    project_path = os.path.join(cwd, args.name)

    os.system("git clone --recurse-submodules -j8 https://github.com/philipwastakenwastaken/cpp_template.git " + args.name)

    git_folder = os.path.join(project_path, '.git')
    shutil.rmtree(git_folder)

    git_modules = os.path.join(project_path, '.gitmodules')
    os.remove(git_modules)

    files_to_replace = ['src/main.cpp', 'src/core/core.hpp', 'src/core/hardware.hpp', 'src/core/log.cpp',\
                        'src/core/log.hpp', 'src/render/opengl/gl_shader.cpp', 'src/render/opengl/gl_shader.hpp',\
                        'src/render/opengl/index_buffer.cpp', 'src/render/opengl/index_buffer.hpp',\
                        'src/render/opengl/vertex_array.cpp', 'src/render/opengl/vertex_array.hpp',\
                        'src/render/opengl/vertex_buffer_layout.cpp', 'src/render/opengl/vertex_buffer_layout.hpp',\
                        'src/render/opengl/vertex_buffer.cpp', 'src/render/opengl/vertex_buffer.hpp',\
                        'src/render/window.cpp', 'src/render/window.hpp',\
                        'src/util/bits.hpp', 'src/util/hex.hpp', 'src/util/rng.cpp', 'src/util/rng.hpp',\
                        'src/util/timer.cpp', 'src/util/timer.hpp',\
                        'src/CMakeLists.txt', 'CMakeLists.txt', 'test/CMakeLists.txt',\
                        'test/gtest_main.cpp', 'test/gtest_util.cpp',\
                        'cmake/Cache.cmake', 'cmake/CompilerWarnings.cmake', 'cmake/PreventInSourceBuilds.cmake',\
                        'cmake/Sanitizers.cmake', 'cmake/StandardProjectSettings.cmake', 'cmake/StaticAnalyzers.cmake']

    for file_name in files_to_replace:
        replace_file(os.path.join(project_path, file_name), args.name)

    os.mkdir(os.path.join(project_path, 'build'))
