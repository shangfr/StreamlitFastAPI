# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 14:18:06 2023

@author: shangfr
"""
import uvicorn
import asyncio
from asgiref.sync import sync_to_async
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from myemb import EmbModel

# 加载模型
model = EmbModel.from_pretrained('./model')
# 启动app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "Hello EmbModel"}

async def doc2stn(doc, seg='。'):
    """
    文本转语句的接口，
    :param doc: 文本字符串
    :return: 语句
    """
    sentences = doc.split(seg)
    sentences = [line.strip() for line in sentences if line]
    return {'number': len(sentences), 'sentences': sentences}

@app.get('/doc2vector')
async def doc2vct(doc, seg='。'):
    """
    文本转向量的接口，
    :param sentence: 文本字符串
    :return: 文本向量
    """
    sentences = await doc2stn(doc, seg)
    emb_vector = await sync_to_async(model.get_embedding)(sentences['sentences'])
    return {'sentences': sentences, 'vector': emb_vector.tolist()}


if __name__ == '__main__':
    uvicorn.run(app='api:app', host="0.0.0.0", port=8000, reload=True)
