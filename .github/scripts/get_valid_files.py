import sys

def main():
    all_files = sys.args[0]
    print(all_files)
    valid_file_extensions = ['.c','.c++','.cc','.c#','.cpp','.cs','.cxx','.cbl','.cob','.cpy','.fs','.go','.h','.hs','.java','.js','.kt','.lisp','.cl','.m','.ml','.pas','.php','.pl','.rb','.rs','.scala','.f90','.f','.for']
    result = []

    for file in all_files:
        if "."+file.split(".")[1] in valid_file_extensions:
            result.append(file)

    return result


if __name__ == "__main__":
    main()