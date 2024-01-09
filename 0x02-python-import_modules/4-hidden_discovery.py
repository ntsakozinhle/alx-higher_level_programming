#!/usr/bin/python3
import py_compile

def print_name(file_path):
    try:
        compiled = py_compile.compile(file_path)
        code_object = py_compile.read_compiled_file(compiled)

        names = [name for name in dir(code_object)
                if not name.startswith('__')]
        name.sort()

        for name in names:
            print(name)

    except py_compile.PyCompileError as e:
        print(f"Error compiling {file_path}: {e}")

print_name('hidden_4.pyc')
