from itertools import product
from sqlalchemy.orm import Session

from  models import Categories,SubCat,Products 

from schemas import (
    CategoriesCreate,SubsategoriesCreate,ProductCreate,
    CategoriesBase,SubCatBase,ProductBase
)

from database import SessionLocal,Base,engine


def create_database():
    return Base.metadata.create_all(bind= engine)

#Categories
def get_cat(db: Session):
    return db.query(Categories).all()

def get_cat_id(db: Session,cat_id:int):
    return db.query(Categories).filter(Categories.id == cat_id).first()

def create_cat(db:Session, cat:CategoriesCreate):
    name = cat.name
    db_cat = Categories(name=name)
    db.add(db_cat)
    db.commit()
    db.refresh(db_cat)
    return db_cat

def update_cat(db:Session, cat_id: int, cat: CategoriesCreate):
    db_cat = get_cat_id(db=db,cat_id=cat_id)
    db_cat.name = cat.name
    db.commit()
    db.refresh(db_cat)
    return db_cat

def delete_cat(db:Session, cat_id: int):
    db.query(Categories).filter(Categories.id == cat_id).delete()
    db.commit()

#Sub-categories
def get_subcat(db: Session):
    return db.query(SubCat).all()

def get_subcat_id(db: Session,subcat_id:int):
    return db.query(SubCat).filter(SubCat.id == subcat_id).first()

def create_subcat(db:Session, subcat:SubsategoriesCreate):
    db_cat = SubCat(name=subcat.name,category_id=subcat.category_id)
    db.add(db_cat)
    db.commit()
    db.refresh(db_cat)
    return db_cat

def update_subcat(db:Session, subcat_id: int, subcat: SubsategoriesCreate):
    db_subcat = get_subcat_id(db=db,subcat_id = subcat_id)
    db_subcat.name = subcat.name
    db_subcat.category_id = subcat.category_id
    db.commit()
    db.refresh(db_subcat)
    return db_subcat

def delete_subcat(db:Session, subcat_id:int):
    db.query(SubCat).filter(SubCat.id == subcat_id).delete()
    db.commit()

#Products
def get_product(db: Session):
    return db.query(Products).all()

def get_product_id(db: Session,product_id:int):
    return db.query(Products).filter(Products.id == product_id).first()

def create_product(db:Session ,product:ProductCreate):
    db_product = Products(
        name = product.name,
        category_id = product.category_id,
        subcategory_id = product.subcategory_id,
        price = product.price,
        size = product.size
        )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db:Session, product_id: int, product: ProductCreate):
    db_product = get_product_id(db=db,product_id = product_id)
    db_product.name = product.name
    db_product.category_id = product.category_id
    db_product.subcategory_id = product.subcategory_id
    db_product.price = product.price
    db_product.size = product.size
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db:Session, product_id:int):
    db.query(Products).filter(Products.id == product_id).delete()
    db.commit()