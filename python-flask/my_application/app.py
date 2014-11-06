from flask import Flask
from flask import request
import os, sys
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
  
# 2 programs for lab 5
@app.route("/intro")
def introduction():
    return "Hello, I am Smurf!!"
  

@app.route("/sumIs")
def sumIs():
    a = 2
    b = 5
    sum1 = a + b
    return sum1

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('./uploads/'+f.filename)
    return '',201
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

#Code to get the list of files from a directory and return it.
@app.route("/files")
def list_files():
     path = "./uploads/"
     dirs = os.listdir(path)
     files = ""
     for file in dirs:
	files = str(files + file + ", \n")
     return files
 
#Euler 1 and 2 Lab7 functions:
@app.route("/euler1")
def euler1():
     sum1 = 0
     for i in range (1, 1000):
	if i%3 or i%5:
	   sum1 = sum1 + i
     return str(sum1)

@app.route("/euler2")
def euler2():
     term1 = 1
     term2 = 2
     sum1 = 0

     for i in range (0, 4000000):
	sum1 = term1 + term2
	term1 = term2
	term2 = sum1
	answer = "Fibinacci up to 4000000 is " + str(sum1)
     return answer
