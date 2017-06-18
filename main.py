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

time_form = """
    <style>
        .error {{ color: red; }}
    </style
    <h1>Validate Time</h1>
    <form method='POST'>
        <label>Hours (24-hour format)
            <input name="hours" type="text" value="{hours}/>
        </label>
        <p class="error">{hours_error}</p>
        <label>Minutes
            <input name="Minutes" type="text" value="{minutes}/>
        </label>
        <p class="error">{minutes_error}</p>
        <input type="submit" value="validate"/>
    </form>
"""

@app.route("/")
def index():
    return form

@app.route("/hello",methods=['POST'])
def hello():
    first_name = request.form['first_name']
    return '<h1>Hello, '+ first_name + '</h1>'

time_form = """
    <style>
        .error {{ color: red; }}
    </style
    <h1>Validate Time</h1>
    <form method='POST'>
        <label>Hours (24-hour format)
            <input name="hours" type="text" value="{hours}/>
        </label>
        <p class="error">{hours_error}</p>
        <label>Minutes
            <input name="Minutes" type="text" value="{minutes}/>
        </label>
        <p class="error">{minutes_error}</p>
        <input type="submit" value="validate"/>
    </form>
"""

app.run()