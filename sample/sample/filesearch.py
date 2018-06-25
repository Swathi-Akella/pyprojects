# filefinder.py  module contains function to assist
# finding filesin working with directory hierarchies.
# Based on the os.walk() function.
import os
import re
import os.path as path


def find_files(pattern, base='.'):
    regex = re.compile(pattern)
    file_matches = []
    for root, dirs, files in os.walk(base):
        for file in files:
            if regex.match(file):
                file_matches.append(path.join(root,file))
    return file_matches

def main():
    matches  = find_files('*.py','.')
    print(matches)

if __name__ == '__main__':
    main()
