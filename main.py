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

time_form = """
    <style>
        .error {{ color: red; }}
    </style
    <h1>Validate Time</h1>
    <form method='POST'>
        <label>Hours (24-hour format)
            <input type='text' name='hours' value='{hours}'/>
        </label>
        <p class="error">{hours_error}</p>
        <label>Minutes
            <input type='text'name='minutes' value='{minutes}'/>
        </label>
        <p class="error">{minutes_error}</p>
        <input type="submit" value="validate"/>
    </form>
"""
@app.route('/validate-time')
def display_time_form():
    return time_form.format(hours='',hours_error='', minutes='',minutes_error='')

def is_initger(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

@app.route('/validate-time', methods=['POST'])
def validate_time():

    hours = request.form['hours']
    minutes = request.form['minutes']

    if not is_integer(hours):
        hours_error = 'Not a valid integer'
        hours = ""
    else:
        hours = int(hours)
        if hours > 23 or hours < 0:
            hours_error = 'hours value out of range (0-23)'
            hours = ""

    if not is_integer(minutes):
        minutes_error = 'Not a valid integer'
        minutes = ""
    else:
        minutes = int(minutes)
           if minutes > 59 or minutes < 0:
            minutes_error = 'minutes value out of range (0-59)'
            minutes = ""

    if not minutes_error and not hours_error:
        # success messsage
        return "Success!"
    else:
        return  time_form.format(hours_error=hours_error,
        minutes_error=minutes_error,hours=hours,minutes=minutes)

app.run()