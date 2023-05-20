import database as _database

import sqlalchemy as _sql
import sqlalchemy.orm as _orm

class Item(_database.Base):
    __tablename__ = "items"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    name = _sql.Column(_sql.String(255), unique=True, index=True, nullable=False)
    description = _sql.Column(_sql.Text)
    price = _sql.Column(_sql.Integer, unique=True, index=True, nullable=False)
    on_offer = _sql.Column(_sql.Boolean, default=False)

    def __str__(self):
        return f"Item(id={self.id}, name='{self.name}', description='{self.description}', price={self.price}, on_offer={self.on_offer})"