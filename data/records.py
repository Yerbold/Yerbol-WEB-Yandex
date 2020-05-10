import sqlalchemy
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Records(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'records'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    cookies_per_second = sqlalchemy.Column(sqlalchemy.Integer)
    cookies_per_click = sqlalchemy.Column(sqlalchemy.Integer)
    total_amount = sqlalchemy.Column(sqlalchemy.Integer)
    player = sqlalchemy.Column(sqlalchemy.String)