from core.app import App
from typer import Typer
import json
from core.signer import pgp_decrypt_file, pgp_encrypt_file
from getpass import getpass
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

app = Typer()
core = App()


@app.command()
def add(name: str, words: str, description: str = ""):
    password = getpass("Enter your password: ")
    word = core.add_new_word(password, name, words, description)
    print(json.dumps(word.serialize(), indent=4))


@app.command()
def get_basic():
    words = core.get_basic_details()
    print(json.dumps(words, indent=4))


@app.command()
def get_all():
    password = getpass("Enter your password: ")
    words = [word.serialize() for word in core.get_all_words(password)]
    print(json.dumps(words, indent=4))


@app.command()
def get(name: str):
    password = getpass("Enter your password: ")
    word = core.get_word(password, name)
    print(json.dumps(word.serialize(), indent=4))


@app.command()
def find_name(name: str):
    password = getpass("Enter your password: ")
    words = [word.serialize()
             for word in core.find_word_by_name(password, name)]
    print(json.dumps(words, indent=4))


@app.command()
def find_description(description: str):
    password = getpass("Enter your password: ")
    words = [word.serialize()
             for word in core.find_word_by_description(password, description)]
    print(json.dumps(words, indent=4))


@app.command()
def find_both(name: str, description: str):
    password = getpass("Enter your password: ")
    words = [word.serialize()
             for word in core.find_word_by_both(password, name, description)]
    print(json.dumps(words, indent=4))


@app.command()
def delete(id: int):
    password = getpass("Enter your password: ")
    core.get_word_by_id(id, password)
    word = core.delete_word(id)
    print(json.dumps(word.serialize(), indent=4))


@app.command()
def clear():
    password = getpass("Enter your password: ")
    [word.serialize() for word in core.get_all_words(password)]
    core.clear_words()
    app.info("All words have been deleted.")


@app.command()
def encrypt_db(key_path: str, db_path: str = "db.sqlite3"):
    """
    Encrypt the database file using the PGP key.

    :param key_path: Path to the PGP key file
    :type key_path: str
    :param db_path: db file path, defaults to "db.sqlite3"
    :type db_path: str, optional
    """
    DB_PATH = BASE_DIR / db_path
    KEY_PATH = BASE_DIR / key_path
    pgp_encrypt_file(str(DB_PATH), str(KEY_PATH))


@app.command()
def decrypt_db(key_path: str, db_path: str = "db.sqlite3"):
    DB_PATH = BASE_DIR / db_path
    KEY_PATH = BASE_DIR / key_path
    passphrase = getpass("Enter your passphrase: ")
    pgp_decrypt_file(str(DB_PATH), passphrase)


if __name__ == "__main__":
    app()
