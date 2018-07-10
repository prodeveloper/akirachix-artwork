from peewee import (CharField,
                    SqliteDatabase,
                    Model,
                    TextField,
                    OperationalError,
                    IntegrityError)
db = SqliteDatabase("artwork.db")


class Artwork(Model):
    name = CharField(max_length=1000, unique=True)
    description = TextField(default="Good image")
    thumbnail_link = CharField(max_length=1000)
    fullimage_link = CharField(max_length=1000)

    class Meta:
        database = db


def initialize():
    try:
        Artwork.create_table()
    except OperationalError:
        pass
