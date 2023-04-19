# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 14:19:08 2023

@author: shangfr
"""

from fastapi import FastAPI
from pydantic import BaseModel
from caculator import calculate


class UserInput(BaseModel):
    operation: str
    x: float
    y: float


app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/calculate")
async def operate(uinput: UserInput):
    result = await calculate(uinput.operation, uinput.x, uinput.y)
    return result
