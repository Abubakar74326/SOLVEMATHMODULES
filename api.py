# from typing import Optional
# from fastapi import FastAPI

#from flask import Flask, request
#import Flask, redirect, url_for, request

from flask import Flask
import modulefunction

app = Flask(__name__)


'''@app.route('/read_root' ,methods = ['POST'])
def read_root():
    data = {
            "NAME emoployee" ,request.form['NAME'] ,
            "company", request.form['revolve'] ,
            "designation", request.form['engineer']
               }
    return {data}'''


@app.route("/function/<int:num>/") #math/
def read_item(num: int): #math_func
    object=modulefunction.Mathematics(int(num))
    results={"number": int(num),
             "factorial": object.factorial(),
             "square": object.square(),
             "cube": object.cube(),
             }

    return str(results)