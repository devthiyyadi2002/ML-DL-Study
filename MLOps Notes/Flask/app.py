from flask import Flask

'''It creates an instance of the flask class
which will be your WSGI ( Web Server Gateway Interface )'''

app = Flask(__name__) 

@app.route("/") # entry point to home page
def welcome():
    return "Welcome to this flask notes made by Dev" # when you run the program it will display this message in the webpage

@app.route("/index")
def index():
    return "Welcome to the index page" # when the url loads go to the top search bar and also give /index to view this message in the index page


# writing the basic entry point of the application
if __name__ =="__main__":
    app.run(debug = True) # use debug = true for real time updation 

