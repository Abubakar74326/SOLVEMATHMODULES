# from typing import Optional
# from fastapi import FastAPI

'''from flask import Flask, request
#import Flask, redirect, url_for, request'''

from flask import Flask
import modulefunction

app = Flask(__name__)


@app.get("/")
def read_root():
    return {"MATH_PROJECT"}


'''@app.route("/read_root/", methods=['POST'])
def read_root():
    data = {
            "name emoployee", request.form['NAME'] ,
            "employee company", request.form['COMPANY'] ,
            "engineer", request.form['ENGINEER']
               }
    return {data}'''


@app.route("/math/<int:num>/") #math/
def math_func(num: int): #math_func
    object=modulefunction.Mathematics(int(num))
    results={"number": int(num),
             "factorial": object.factorial(),
             "square": object.square(),
             "cube": object.cube(),
             }

    return str(results)