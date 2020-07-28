from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home_page():
    """Renders Homepage"""

    return render_template("homepage.html")

@app.route('/test', methods=['POST'])
def cut_string():
    """Returns the String"""
    string1=request.form["string_to_cut"]
    output=''
    for i in range(2,len(string1),3):
        output += string1[i]
    return ({"return_string":output})

if __name__ == "__main__":
    app.run()