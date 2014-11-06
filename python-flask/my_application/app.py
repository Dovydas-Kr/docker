from flask import Flask
from flask import request
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
