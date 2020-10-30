import logging
import os
from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel
from display import Display

if "DEBUG" in os.environ:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

class DrawEntry(BaseModel):
    x: float
    y: float
    w: float
    h: float
    type: str
    font_size: Optional[int] = 24
    align: Optional[str] = "start" # start | center | end
    justify: Optional[str] = "start" # start | center | end
    content: str


display = Display(os.environ.get('DISPLAY_TYPE'), "ROTATE" in os.environ)
app = FastAPI()

@app.post("/")
def draw(entries: List[DrawEntry]):
    content=map(lambda entry: entry.dict(), entries)
    display.draw(content)
    return 0
