import sqlalchemy
import databases

# db init
DATABASE_URL = "sqlite:///sql_app.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(
    DATABASE_URL
)
metadata.create_all(engine)
# SQL model
cats = sqlalchemy.Table("cats", metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("breed", sqlalchemy.String(64), unique=True),
    sqlalchemy.Column("loc_origin", sqlalchemy.String(32)),
    sqlalchemy.Column("body_type", sqlalchemy.String(8)),
    sqlalchemy.Column("coat_lenght", sqlalchemy.Integer),
    sqlalchemy.Column("pattern", sqlalchemy.Boolean)
)