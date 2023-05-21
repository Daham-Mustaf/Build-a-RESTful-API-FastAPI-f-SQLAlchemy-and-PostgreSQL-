from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from typing import Optional,List
from database import SessionLocal
import models

# models.Base.metadata.create_all(bin= engine)

app=FastAPI()

class Item(BaseModel): #serializer
    id:int
    name:str
    description:str
    price:int
    on_offer:bool


    class Config:
        orm_mode=True



db=SessionLocal()

@app.get('/items',response_model=List[Item],status_code=200)
def get_all_items():
    items=db.query(models.Item).all()

    return items

@app.get('/item/{item_id}',response_model=Item,status_code=status.HTTP_200_OK)
def get_an_item(item_id:int):
    item=db.query(models.Item).filter(models.Item.id==item_id).first()
    return item

@app.post('/items',response_model=Item,
        status_code=status.HTTP_201_CREATED)
def create_an_item(item:Item):
    db_item=db.query(models.Item).filter(models.Item.name==item.name).first()

    if db_item is not None:
        raise HTTPException(status_code=400,detail="Item already exists")
    new_item=models.Item(
        # name=item.name,
        # price=item.price,
        # description=item.description,
        # on_offer=item.on_offer
        **item.dict()
    )

    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return new_item

@app.put('/item/{item_id}',response_model=Item,status_code=status.HTTP_200_OK)
def update_an_item(item_id:int, item:Item):
    # item_to_update=db.query(models.Item).filter(models.Item.id==item_id).first()
    # item_to_update.name=item.name
    # item_to_update.price=item.price
    # item_to_update.description=item.description
    # item_to_update.on_offer=item.on_offer
    # db.commit()
    # return item_to_update
    item_query = db.query(models.Item).filter(models.Item.id == item_id)
    item_db = item_query.first()
    if item_db == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                           detail=f" Item with id:{item_id} does not exist!")
    
    item_query.update(item.dict(), synchronize_session=False)      
    db.commit()
    return {"Data": item_query.first()}

@app.delete('/item/{item_id}')
def delete_item(item_id:int):
    item_to_delete=db.query(models.Item).filter(models.Item.id==item_id).first()

    if item_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")
    
    db.delete(item_to_delete)
    db.commit()
    return item_to_delete