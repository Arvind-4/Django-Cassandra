import os
import pathlib
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()

ENCRYPTION_KEY = os.environ.get("ENCRYPTION_KEY", None)


def generate_key():
    key = Fernet.generate_key().decode("UTF-8")
    os.environ["ENCRYPTION_KEY"] = key
    print("ENCRYPTION_KEY:", key)
    return key


if ENCRYPTION_KEY is None:
    generate_key()


def encrypt_dir(input_dir, output_dir):
    key = ENCRYPTION_KEY
    if not key:
        raise Exception("ENCRYPTION_KEY is not found")
    fer = Fernet(key)  # f"{}:"
    input_dir = pathlib.Path(input_dir)
    output_dir = pathlib.Path(output_dir)
    output_dir.mkdir(exist_ok=True, parents=True)
    for path in input_dir.glob("*"):
        _path_bytes = path.read_bytes()  # open(filepath, 'rb')
        data = fer.encrypt(_path_bytes)
        rel_path = path.relative_to(input_dir)
        dest_path = output_dir / rel_path
        dest_path.write_bytes(data)


def decrypt_dir(input_dir, output_dir):
    key = ENCRYPTION_KEY
    if not key:
        raise Exception("ENCRYPTION_KEY is not found")
    fer = Fernet(key)  # f"{}:"
    input_dir = pathlib.Path(input_dir)
    output_dir = pathlib.Path(output_dir)
    output_dir.mkdir(exist_ok=True, parents=True)
    for path in input_dir.glob("*"):
        _path_bytes = path.read_bytes()  # open(filepath, 'rb')
        data = fer.decrypt(_path_bytes)
        rel_path = path.relative_to(input_dir)
        dest_path = output_dir / rel_path
        dest_path.write_bytes(data)
