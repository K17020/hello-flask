from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True
 
form = """
<!doctype html>
<html>
    <body>
    <!--This sends the text from the input to the hello fuction below-->    
        <form action="/hello" method="post">
            <label for="first-name">First Name</label>
            <!--This creates the text field for you to input the text-->    
            <input id="first-name" type="text" name="first_name" />
            <!--This creates the button to submit text-->   
            <input type="submit"/>
        </form>
    </body>
</html>

"""

@app.route("/")
def index():
    return form

@app.route("/hello",methods=['POST'])
def hello():
    first_name = request.form['first_name']
    return '<h1>Hello, '+ first_name + '</h1>'
app.run()