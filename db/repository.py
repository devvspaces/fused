from .models import Word
from .db import session


class WordRepository:
    def __init__(self):
        self.session = session

    def get_all(self):
        return self.session.query(Word).all()

    def get_by_id(self, id: int):
        return self.session.query(Word).filter(Word.id == id).first()

    def create(self, word: Word):
        self.session.add(word)
        self.session.commit()
        return word

    def delete(self, id: int):
        word = self.get_by_id(id)
        self.session.delete(word)
        self.session.commit()
        return word

    def clear(self):
        self.session.query(Word).delete()
        self.session.commit()

    def find_by_name(self, name: str):
        return self.session.query(Word).filter(Word.name.contains(name)).all()

    def find_by_description(self, description: str):
        return self.session.query(Word)\
            .filter(Word.description.contains(description)).all()

    def find_by_both(self, name: str, description: str):
        return self.session.query(Word)\
            .filter(Word.name.contains(name) | Word.description.ilike(description).contains(description)).all()
