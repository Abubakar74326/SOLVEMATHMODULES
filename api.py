# from typing import Optional
# from fastapi import FastAPI
#from flask import Flask, request

from flask import Flask
""" By importing modulefunction developer access the Mathematics class in this file """
import modulefunction

app = Flask(__name__)

"""
‘/’ URL is bound with read_root() function
"""
@app.route("/mathoperation/<int:num>/")
def math_func(num: int):
    object=modulefunction.Mathematics(int(num))
    results={"number": int(num),
             "factorial": object.factorial(),
             "square": object.square(),
             "cube": object.cube(),
             }

    return str(results)

# i have try my best effort but no vail
'''app.route("/data/", methods=['POST'])
 def read_root():
     data = {
            "name emoployee", request.form['name'],
             "employee desig", request.form['desig'],
             "company", request.form['comp']
             }
                return {data}
'''