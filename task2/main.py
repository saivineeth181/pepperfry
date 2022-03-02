from itertools import product
from typing import List
from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
import services as _services, schemas as _schemas
from database import SessionLocal

app = FastAPI()

_services.create_database()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Categories
@app.post("/category/",response_model=_schemas.CategoriesBase)
def create_data(cat:_schemas.CategoriesCreate,db: Session=Depends(get_db)):
    return _services.create_cat(db=db,cat=cat)

@app.get('/category/',response_model=list[_schemas.CategoriesBase])
def read_data(db: Session=Depends(get_db)):
    cat = _services.get_cat(db)
    return cat

@app.put('/category/{cat_id}',response_model= _schemas.CategoriesBase)
def update_category(cat_id:int,cat:_schemas.CategoriesCreate,db: Session=Depends(get_db)):
    return _services.update_cat(db=db,cat=cat,cat_id=cat_id)

@app.delete('/category/{cat_id}')
def delete_category(cat_id:int, db:Session=Depends(get_db)):
    _services.delete_cat(db=db,cat_id=cat_id)
    return {"message": f"successfully deleted Category with id: {cat_id}"}

#Sub - Categories
@app.post("/subcategory/",response_model=_schemas.SubCatBase)
def create_data(subcat:_schemas.SubsategoriesCreate,db: Session=Depends(get_db)):
    return _services.create_subcat(db=db,subcat=subcat)

@app.get('/subcategory/',response_model=list[_schemas.SubCatBase])
def read_data(db: Session=Depends(get_db)):
    subcat = _services.get_subcat(db)
    return subcat

@app.put('/subcategory/{subcat_id}',response_model= _schemas.SubCatBase)
def update_subcategory(subcat_id:int,subcat:_schemas.SubsategoriesCreate,db: Session=Depends(get_db)):
    return _services.update_subcat(db=db,subcat=subcat,subcat_id=subcat_id)

@app.delete('/subcategory/{subcat_id}')
def delete_subcategory(subcat_id:int, db:Session=Depends(get_db)):
    _services.delete_subcat(db=db,subcat_id=subcat_id)
    return {"message": f"successfully deleted Category with id: {subcat_id}"}

#Product
@app.post("/product/",response_model=_schemas.ProductBase)
def create_data(product:_schemas.ProductCreate,db: Session=Depends(get_db)):
    return _services.create_product(db=db,product=product)

@app.get('/product/',response_model=list[_schemas.ProductBase])
def read_data(db: Session=Depends(get_db)):
    subcat = _services.get_product(db)
    return subcat

@app.get('/product/{product_id}',response_model=_schemas.ProductBase)
def read_product_id(product_id:int,db: Session=Depends(get_db)):
    return _services.get_product_id(db=db,product_id=product_id)

@app.put('/product/{product_id}',response_model= _schemas.ProductBase)
def update_product(product_id:int,product:_schemas.ProductCreate,db: Session=Depends(get_db)):
    return _services.update_subcat(db=db,product=product,product_id=product_id)

@app.delete('/product/{product_id}')
def delete_subcategory(product_id:int, db:Session=Depends(get_db)):
    _services.delete_product(db=db,product_id=product_id)
    return {"message": f"successfully deleted Category with id: {product_id}"}

@app.get('/category/{cat_id}',response_model=list[_schemas.ProductBase])
def read_category_id(cat_id:int,db: Session=Depends(get_db)):
    return _services.get_cat_id(db=db,cat_id=cat_id)

@app.get('/subcategory/{subcat_id}',response_model=list[_schemas.ProductBase])
def read_subcategory_id(subcat_id:int,db: Session=Depends(get_db)):
    return _services.get_subcat_id(db=db,subcat_id=subcat_id)


