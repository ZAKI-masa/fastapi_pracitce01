from fastapi import FastAPI, Body
from contents import menu
from typing import Optional
from conf import cors

            
app = FastAPI()

cors.set_up(app)


@app.get("/")
async def root():
    return {"message": "Cafe APIへようこそ"}

@app.get("/menus")
async def get_menus(max_price : Optional[int] = None,category : Optional[str] = None):
    
    if category is not None:
        return menu.find_menu_filter_by_category(category)
    if max_price is not None:
        return menu.find_menu_filter_by_maxprice(max_price)
    
    return menu.get_allmenus()


@app.get("/menus/{menu_id}")
async def get_target_menu(menu_id: int):
    return menu.get_target_menu(menu_id)


@app.post("/menus")
async def create(new_menu_info = Body(
    { "id": 0, "name": "", "category": "", "price": 0, "description": "", "image": "" }
)):
    return menu.create(new_menu_info)

@app.put("/menus/{id}")
async def update(id: int,menu_update = Body(
    { "id": 0, "name": "", "category": "", "price": 0, "description": "", "image": "" }
)):
    return menu.update(id,menu_update)

@app.delete("/menus/{id}")
async def delete(id: int):
    return menu.delete(id)