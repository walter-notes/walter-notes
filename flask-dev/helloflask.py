# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 13:39:27 2021

@author: Devya Singh
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p><a href=\"https://developers.notion.com/reference/\">Visit Notion API documentation!</a></p>"