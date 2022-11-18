from flask import *
from flask import Flask, render_template
app=Flask(__name__,template_folder='templates')
@app.route('/')
def setcookie():
    res = make_response("cookie is inserted")
    res.set_cookie('Flask','framework')
    return res

if __name__ =='__main__':
    app.run(debug=True)
    
