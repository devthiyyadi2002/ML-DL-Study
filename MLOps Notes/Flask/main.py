# integrating Html file into this framework 
from flask import Flask,render_template

'''It creates an instance of the flask class
which will be your WSGI ( Web Server Gateway Interface )'''

app = Flask(__name__) 

@app.route("/") # entry point to home page
def welcome():
    return "Welcome to this flask notes made by Dev" # when you run the program it will display this message in the webpage

@app.route("/index")
def index():
    return render_template("index.html") # redirects to index.html file in the templates folder - > render_templates always looks inside the templates folder for html files so make sure to have that.

@app.route('/about')
def about():
    return render_template('about.html') # redirects to the about.html page of the website in the template folder

# writing the basic entry point of the application
if __name__ =="__main__":
    app.run(debug = True) # use debug = true for real time updation 

