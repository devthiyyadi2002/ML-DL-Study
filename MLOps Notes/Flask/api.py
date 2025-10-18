### Put and Delete -- HTTP Verbs
### working with API's --JSON

from flask import Flask,jsonify,request

app = Flask(__name__)

# initial data in my to-do list 

items = [
    {'id':1,'name':'Item 1','description':"This is item 1"},
    {'id':2,'name':'Item 2','description':"This is item 2"}
]

@app.route('/')
def home():
    return 'welcome to th sample to-do list app'

## Get : Retrieve all the items 

@app.route('/items',methods = ["GET"])
def get_items():
    return jsonify(items)

## get : retrieve a spcific item by id

if __name__ == "__main__":
    app.run(debug=True)
    