# Deletes all non-.v/.c/.h files from all student subfolders
# Assumes no files with the same name

import fnmatch,os,shutil

rootPath = r"/Users/martin/Downloads/submissions/students"
pattern = '*'


for root, dirs, files in os.walk(rootPath):
    # Iterate through all students
    for student in os.scandir(root):
        if student.is_dir():
            print(student)
        else:
            continue
        # Use student directory as root path
        rootPath = os.path.join(root, student)
   
        # Remove unrelated files within each student directory
        for root, dirs, files in os.walk(rootPath):
            for filename in files:
                if filename.endswith("MC68K.v") or filename.endswith("AddressDecoder_Verilog.v") or filename.endswith("tetris.h") or filename.endswith("tetris.c") or filename.startswith("M68kDebug"):
                    # Move to top level of student directory
                    if root != rootPath:
                        shutil.move(os.path.join(root, filename), rootPath)
                    continue
                else:
                    print(f'deleting {os.path.join(root, filename)}')
                    os.remove(os.path.join(root,     filename))

        for root, dirs, files in os.walk(rootPath, topdown=False):
            # Remove all subfolders, which should be empty
            for dir in dirs:
                os.rmdir(os.path.join(root, dir))

    break