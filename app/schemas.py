from pydantic import BaseModel
from typing import Optional

# -------- Categories --------
class CategoryBase(BaseModel):
    title: str

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int

    class Config:
        orm_mode = True


# -------- Books --------
class BookBase(BaseModel):
    title: str
    description: Optional[str]
    price: float
    url: Optional[str]
    category_id: int

class BookCreate(BookBase):
    pass

class BookResponse(BookBase):
    id: int

    class Config:
        orm_mode = True
