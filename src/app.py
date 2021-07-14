# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 13:39:27 2021

@author: Devya Singh
"""
import logging
from flask import Flask
import notion
import comprehend

app = Flask(__name__)
logger = logging.getLogger(__name__)

@app.route("/page/<page_id>")
def get_page_content(page_id):
    
    # send request to notion API
    content = notion.getPageContent(page_id)
    logger.info("content fetched from notion API " + content)
    tags = comprehend.get_NER_tags(content)
    logger.info("NER info fetched from AWS API " + tags)

    
    return tags