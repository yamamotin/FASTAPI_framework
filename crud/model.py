import sqlalchemy
from app import metadata

# SQL model
cats = sqlalchemy.Table(
    "cats",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("breed", sqlalchemy.String(64), unique=True),
    sqlalchemy.Column("loc_origin", sqlalchemy.String(32)),
    sqlalchemy.Column("coat_lenght", sqlalchemy.Integer),
    sqlalchemy.Column("pattern", sqlalchemy.Boolean),
)
