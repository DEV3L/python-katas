import hashlib

def sha_str(input_str):
    hash_object = hashlib.sha1(input_str.encode())
    return hash_object.hexdigest()
