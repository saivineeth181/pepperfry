from typing import List
from unicodedata import name
from pydantic import BaseModel

class CategoriesCreate(BaseModel):
    name: str

class CategoriesBase(CategoriesCreate):
    id: int
    class Config:
        orm_mode = True

class SubsategoriesCreate(BaseModel):
    category_id: int
    name: str

class SubCatBase(SubsategoriesCreate):
    id: int
    class Config:
        orm_mode = True

class ProductCreate(BaseModel):
    category_id: int
    subcategory_id: int
    name: str
    price: int
    size:str

class ProductBase(ProductCreate):
    id: int
    class Config:
        orm_mode = True