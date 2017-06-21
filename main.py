from flask import Flask, request, redirect
import cgi
import os
import jinja2

# this is looking for a folder named tempates in the given path
template_dir = os.path.join(os.path.dirname(__file__),
    'templates')

# this loads files from the dir templates into a jinja2 template
#autoescape provides protection from unwanted html insert
jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True


# this directs jinja templates to the html files
@app.route("/")
def index():
    template = jinja_env.get_template('hello_form.html')
    return template.render()

@app.route("/hello", methods=['POST'])
def hello():
    first_name = request.form['first_name']
    template = jinja_env.get_template('hello_greeting.html')
    return template.render(name=first_name)

@app.route('/validate-time')
#displays the hours and minutes on screen
def display_time_form():
    tempate = jinja_env.get_template('time_form.html')
    return tempate.render()

#checks to see if the hour/minutes are integers
def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

@app.route('/validate-time', methods=['POST'])
#chcecks to see if the time entered are within range 

def validate_time():

    hours = request.form['hours']
    minutes = request.form['minutes']

    hours_error = ''
    minutes_error = ''

    if not is_integer(hours):
        hours_error = 'Not a valid integer'
        hours = ''
    else:
        hours = int(hours)
        if hours > 23 or hours < 0:
            hours_error = 'Hour value out of range (0-23)'
            hours = ''

    if not is_integer(minutes):
        minutes_error = 'Not a valid integer'
        minutes = ''
    else:
        minutes = int(minutes)
        if minutes > 59 or minutes < 0:
            minutes_error = 'Minutes value out of range (0-59)'
            minutes = ''

    if not minutes_error and not hours_error:
        time = str(hours) + ':' + str(minutes)
        return redirect('/valid-time?time={0}'.format(time))
    else:
        template = jinja_env.get_template('time_form.html')
        return template.render(hours_error=hours_error, minutes_error=minutes_error, hours=hours, minutes=minutes)

@app.route('/valid-time')
def valid_time():
    time = request.args.get('time')
    return '<h1>You submitting {0}. Thanks for submitting a valid time!</h1>'.format(time)


app.run()