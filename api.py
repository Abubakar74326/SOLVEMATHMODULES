# from typing import Optional
# from fastapi import FastAPI
#from flask import Flask, request

from flask import Flask
""" by importing modulefunction developer access the Mathematics class in this file """
import modulefunction

app = Flask(__name__)


@app.get("/")
"""
‘/’ URL is bound with read_root() function
"""

def read_root():
   """Retrun message eill display """
    return {"MATH_PROJECT}
            
'''@app.route("/read/", methods=['POST'])
def read_root():
    data = {
            "name emoployee", request.form['NAME'],
            "employee company", request.form['COMPANY'],
            "engineer", request.form['ENGINEER']
               }
    return {data}'''


@app.route("/function/<int:num>/") #math/
def read_item(num: int): #math_func
    object=allfunctions.Mathematics(int(num))
    results={"number": int(num),
             "factorial": object.factorial(),
             "square": object.square(),
             "cube": object.cube(),
             }

    return str(results)