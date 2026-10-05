from flask import Flask, render_template

import os

app = Flask(__name__)

names=[os.environ["FIRST_NAME_IN_LIST"]]

#wait psycopg.connect("dbname=test user=postgres") as conn:

@app.route("/") 
def hello_world(): 
    global names
    return render_template("guestbook.html", names=names)

@app.route("/catch", methods=["POST"])
def catch():
    #flask uses magic globals to get the data
    global names
    if request.form.get("nameInput"):
        names.append(request.form.get("nameInput"))
    return render_template("guestbook.html", names=names)
     
#uv add psycopg[binary]
# or 
#uv add pyschopg[c]
#uv add pyschopg