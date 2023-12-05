#!/usr/bin/python3
# AUTH: codenvibes
"""
Module to generate Python files with specified names, including a basic
shebang, author tag, and empty module docstring.
"""
import os


def gen_pyfile():
    file_names = input("File Name(s) (space-seperated): ").split(' ')

    for name in file_names:
        name = name.strip()

        with open(name, "w") as python_file:
            python_file.write('#!/usr/bin/python3\n')
            python_file.write('# AUTH: codenvibes\n')
            python_file.write('"""\n\n"""\n')
            os.chmod(name, 0o764)


if __name__ == "__main__":
    gen_pyfile()
