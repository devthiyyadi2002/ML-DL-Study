from flask import Flask, render_template,request

app = Flask(__name__) 

@app.route("/")
def welcome():
    return "Welcome to this flask notes made by Dev" 

@app.route("/index",methods=['GET']) # by default it is a get request 
def index():
    return render_template("index.html") 

@app.route('/about')
def about():
    return render_template('about.html') 

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello {name}"
    return render_template('form.html')


if __name__ =="__main__":
    app.run(debug = True) 