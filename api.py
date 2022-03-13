# from typing import Optional
# from fastapi import FastAPI

from flask import Flask, request

from flask import Flask
import modulefunction

app = Flask(__name__)


'''@app.get("/")
def read_root():
    return {"MATH_PROJECT"}'''

@app.route("/data/", methods=['POST'])
def read_root():
    data = {
            "name emoployee", request.form['NAME'],
            "employee company", request.form['COMPANY'],
            "engineer", request.form['ENGINEER']
               }
    return {data}


@app.route("/mathoperation/<int:num>/")
def math_func(num: int):
    object=modulefunction.Mathematics(int(num))
    results={
             "your entered number": int(num),

             "factorial": object.factorial(),

             "square": object.square(),

             "cube": object.cube(),

             }

    return str(results)