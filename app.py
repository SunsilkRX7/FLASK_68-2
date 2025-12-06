from flask import Flask,jsonify, render_template

app = Flask(__name__)

@app.route('/home', methods=['GET'])
def home():
    name = "Anya"
    age = 7
    my_dict = {
        "name": "yor",
        "age" : 26
    }
    return render_template('Home.html', name=name, age=age, my_dict=my_dict)  
@app.route('/create', methods=['GET'])
def create():
    return render_template('create.html') 

if __name__ == '__main__':
    # app.run()# production mode
    app.run(debug=True)  # development mode