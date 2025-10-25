### building url dynamically 
# jinja 2 template 
# variable rule 

### Jinja 2 template engine 
'''
these are to read the data source from the back end in the html page 
-> {{ }} expressions to print output in html 
-> {%....%} conditions, for loops 
-> {#...#} write single line comment this way 
'''

from flask import Flask, render_template,request,redirect,url_for

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

'''@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello {name}"
    return render_template('form.html')'''

# variable rule
@app.route("/success/<int:score>") # <score> is the value to be passed int : ensures the value is an integrer 

def success(score):
    res = ""
    if score>=50:
        res = "PASSED"
    else:
        res="FAILED"
    return render_template("results.html",results=res)

@app.route("/successres/<int:score>")
def successres(score):
    res = ""
    if score>=50:
        res = "PASSED"
    else:
        res="FAILED"
    exp = {'score':score,"res":res}
    
    return render_template("result1.html",results=exp)

@app.route("/successslf/<int:score>") # <score> is the value to be passed int : ensures the value is an integrer 
def successslf(score):
    return render_template("results.html",results=score)

@app.route('/submit',methods=["GET","POST"])
def submit():
    total_score = 0 
    if request.method=='POST':
        science = float(request.form["Science"])
        maths = float(request.form['Maths'])
        c = float(request.form['C'])
        datascience = float(request.form['Datascience'])
        
        total_score = (science+maths+c+datascience)/4
    else:
        return render_template('getresult.html')
    return  redirect(url_for('successres',score=total_score)) # redirect function can take your data to another page 
        

if __name__ =="__main__":
    app.run(debug = True) 
 