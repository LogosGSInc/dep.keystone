from dep_keystone.hashing import sha256_file_bytes


def test_sha256_file_bytes():
    data = b"abc"
    digest = sha256_file_bytes(data)
    assert digest == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
