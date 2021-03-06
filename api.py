# from typing import Optional
# from fastapi import FastAPI
from flask import Flask, request

#from flask import Flask
""" By importing modulefunction developer access the Mathematics class in this file """
import modulefunction

app = Flask(__name__)

"""
  ‘/’ URL is bound with math_func() function
"""
@app.route("/mathoperation/<int:num>/")
def math_func(num: int):
 """
    function take integer number as an arguments return result in jason format.
     :param num: number
     :return:results
 """
 object=modulefunction.Mathematics(int(num))
 results={"YOUR ENTERED NUMBER": int(num),
             "factoriaL": object.factorial(),
             "square": object.square,
             "cube": object.cube(),
         }
 return str(results)

@app.route("/data/", methods=['POST'])
def post_method():
    """

    :return: data
    """
    data = {
            "name emoployee": request.form['name'],
             "employee desig": request.form['desig'],
             "company": request.form['comp']
             }
    return data