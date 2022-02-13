# Core Pkgs

from fastapi import FastAPI,Request
import uvicorn

# utils
import json

with open("data/netflix_titles.json", encoding = "utf8") as f:
    movielist = json.load(f)

#Init App
api = FastAPI()


# API routes/Endpoints
# https://127.0.0.1:8000/api/v1/titles
# https://127.0.0.1:8000/api/v1/titles/?limit=10 ::: QueryParam
# https://127.0.0.1:8000/api/v1/titles/key
# https://127.0.0.1:8000/api/v1/titles/{show_id}
# https://127.0.0.1:8000/api/v1/predict/{searchterm}

# API routes/Endpoints
# https://127.0.0.1:8000/api/v1/titles
@api.get("/")
async def root_app():
    return {'text': 'Hello Netflix FastAPI'}

# https://127.0.0.1:8000/api/v1/titles
# Query Param
@api.get("/api/v1/titles")
async def read_all_titles(limit:int = 10):
    return {"data":movielist[:limit]}

# https://127.0.0.1:8000/api/v1/titles/{name}
# Path Param
@api.get("/api/v1/titles/{name}")
async def read_title(name:str):
    current_title = [ item for item in movielist if item['title'] == name.title()]
    return {"data":current_title}





if __name__ == '__main__':
    uvicorn.run(api, host='127.0.0.1',port=8000)

