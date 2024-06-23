from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import pymongo
app = FastAPI()

@app.get("/")
def root():
    return {"message":"Hello, world!"}


#path parameters
@app.get("/path_parameter/{item}")
def path_parameter(item:str):
    return {"item":item}

#query parameters
@app.get("/query_parameter/")
def query_parameter(item:str,price:int):
    return {"item":item,'price':price}



class Item(BaseModel):
    name:str
    description:str
    price:int



client = pymongo.MongoClient("mongodb+srv://sohamchandratre2000:qStGIY9vSJPCFSCz@cluster0.tu94qx4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.database
product_collection=db.product

# add api
@app.post("/submit_item/")
def store_item(item:Item):
    item_dict = item.dict()
    result = product_collection.insert_one(item_dict)
    return ("sucess")

# get all products api
@app.get("/get_all_item")
def get_all_items():
    allProducts = []
    for product in product_collection.find():
        product['_id']=str(product['_id'])
        allProducts.append(product)
    return {"product":allProducts}

from bson import ObjectId

#get product by id api
@app.get("/get_item_by_id")
def get_all_items(product_id:str):
    product = product_collection.find_one({"_id":ObjectId(product_id)})
    if product:
        product['_id']=str(product['_id'])
        return product
    else:
        raise HTTPException(status_code= 404 ,detail="Product is not found")
    


# update api
@app.put("/updateProduct")
def update_product_by_id(product_id:str,item:Item):
    product = product_collection.find_one({"_id":ObjectId(product_id)})
    if product:
        update_values={key:value for key,value in item.dict().items()}
        product_collection.update_one({"_id":ObjectId(product_id)},{"$set":update_values})
        return {"message":"product is updated successfully"}



#delete api 
@app.delete("/deleteProduct")
def delete(product_id:str):
    deleted_product=product_collection.delete_many({"_id":ObjectId(product_id)})
    if deleted_product.deleted_count == 1:
        return{"message":"product is deleted successfully"}
    else:
        return {"message":"product is not deleted successfully"}
    
