from sqlalchemy import Column,String,ForeignKey,Integer
import sqlalchemy.orm as _orm

from database import Base


class Categories(Base):
    __tablename__ = "Categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

class SubCat(Base):
    __tablename__ = "SubCategories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    category_id = Column(Integer,ForeignKey("Categories.id"))

    category = _orm.relationship('Categories', foreign_keys=[category_id])
class Products(Base):
    __tablename__ = "Products"
    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer,ForeignKey("Categories.id"))
    subcategory_id = Column(Integer,ForeignKey("SubCategories.id"))
    name = Column(String, unique=True, index=True)
    price = Column(Integer)
    size = Column(String)

    category = _orm.relationship('Categories', foreign_keys=[category_id])
    subcategory = _orm.relationship('SubCat',foreign_keys=[subcategory_id])


