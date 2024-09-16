import hashlib
import sys

filename = sys.argv[-1]
with open(filename, 'rb') as file_obj:
    file_contents = file_obj.read()

    md5_hash = hashlib.md5(file_contents).hexdigest()

    print(md5_hash)
