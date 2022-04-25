# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 13:39:27 2021

@author: Devya Singh
"""
import logging
from flask import Flask
import notion
import comprehend
import mongo

app = Flask(__name__)
logger = logging.getLogger(__name__)
logging.basicConfig(filename='myapp.log', level=logging.INFO)
@app.route("/page/<page_id>")
def get_page_content(page_id):
    
    # send request to notion API
    content = notion.getPageContent(page_id)
    if not content:
        return "page not found/permission not given"
    
    logger.info("content fetched from notion API " + content)
    tags = comprehend.get_NER_tags(content)
    logger.info("NER info fetched from AWS API " + str(tags))
    mongo.store_page(page_id, tags)

    
    return str(tags)