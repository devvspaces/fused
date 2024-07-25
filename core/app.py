from core.exceptions import DecryptionError
from db.models import Word
from db.repository import WordRepository
from .crypto import encrypt, decrypt


class App:
    def __init__(self):
        self.repository = WordRepository()

    def add_new_word(
        self, password: str, name: str, words: str, description: str = ""
    ):
        word = Word(name=name, words=encrypt(
            words, password), description=description)
        return self.repository.create(word)

    def get_basic_details(self):
        words = self.repository.get_all()
        return [word.serialize() for word in words]

    def get_all_words(self, password: str):
        words = self.repository.get_all()
        responses = []
        for word in words:
            try:
                word.words = decrypt(word.words, password)
                responses.append(word)
            except DecryptionError:
                pass
        return responses

    def get_word(self, password: str, name: str):
        word = self.repository.get(name)
        try:
            word.words = decrypt(word.words, password)
        except DecryptionError:
            return {}
        return word

    def find_word_by_name(self, password: str, name: str):
        words = self.repository.find_by_name(name)
        responses = []
        for word in words:
            try:
                word.words = decrypt(word.words, password)
                responses.append(word)
            except DecryptionError:
                pass
        return responses

    def find_word_by_description(self, password: str, description: str):
        words = self.repository.find_by_description(description)
        responses = []
        for word in words:
            try:
                word.words = decrypt(word.words, password)
                responses.append(word)
            except DecryptionError:
                pass
        return responses

    def find_word_by_both(self, password: str, name: str, description: str):
        words = self.repository.find_by_both(name, description)
        responses = []
        for word in words:
            try:
                word.words = decrypt(word.words, password)
                responses.append(word)
            except DecryptionError:
                pass
        return responses

    def get_word_by_id(self, id: int, password: str):
        word = self.repository.get_by_id(id)
        word.words = decrypt(word.words, password)
        return word

    def delete_word(self, id: int):
        return self.repository.delete(id)

    def clear_words(self):
        self.repository.clear()
