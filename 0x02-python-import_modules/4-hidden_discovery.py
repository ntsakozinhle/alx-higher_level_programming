#!/usr/bin/python3
if __name__ == "__main__":
    from py_compile import compile
    def print_name(file_path):
        try:
            compiled = compile(file_path)
            code_object = compile.read_compiled_file(compiled)
            names = [name for name in dir(code_object)
                    if not name.startswith('__')]
            name.sort()
            for name in names:
                print(name)
        except compile.PyCompileError as e:
            print(f"Error compiling {file_path}: {e}")

    print_name('hidden_4.pyc')
