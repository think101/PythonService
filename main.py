from fastapi import FastAPI
import uvicorn
from mylib.logic import search_wiki
from mylib.logic import wiki as wikilogic
from mylib.logic import phrase as phraselogic


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Wikipedia API. Call /search or /wiki"}

@app.get("/search/{value}")
async def search(value: str):
    """Search wikipedia for value"""

    result = search_wiki(value)
    return {"result": result}

@app.get("/wiki/{name}")
async def wiki(name: str):
    """Retrieve wikipedia page"""

    result = wikilogic(name)
    return {"result": result}

@app.get("/phrase/{name}")
async def phrase(name: str):
    """Retrieve wikipedia page and analyze for phrases"""

    result = phraselogic(name)
    return {"result": result}

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
