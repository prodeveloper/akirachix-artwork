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
        Artwork.create_table(safe=True)
    except OperationalError:
        pass
    try:
        Artwork.create(
            name="monkey_singing",
            description="Awesome Artistic Monkey",
            thumbnail_link="static/music-3507317_640.jpg",
            fullimage_link="static/music-3507317_1920.jpg"
            )
    except IntegrityError:
        pass
    try:
            Artwork.create(
                name="mercedes",
                description="The car with an awesome interior",
                thumbnail_link="static/mercedes-3510327_640.jpg",
                fullimage_link="static/mercedes-3510327_1920.jpg"
            )
    except IntegrityError as e:
        pass
