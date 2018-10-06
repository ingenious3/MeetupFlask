from flask import Flask, make_response
from flask import url_for
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'this is a Flask'

@app.route('/string/')
def return_string():
    return 'Hello Flask App String'

@app.route('/object/')
def return_object():
    headers = {'Content-Type':'text/plain'}
    return make_response('Hello Flask App Object', status = 200, headers = headers)

@app.route('/tuple/')
def return_tuple():
    return 'Hello Flask App Tuple', 200, {'Content-Type':'text/plain'}


@app.route('/appointments/')
def appointent_list():
    return 'list of all available apointment'

@app.route('/appointments/<int:appointment_id>')
def appointment_detail(appointment_id):
    return 'Detail o appointment  #{}.'.format(appointment_id)
   # edit_url = url_for('appointment_edit', appointment_id = appointment_id)
    #return edit_url

@app.route('/appointments/<int:appointment_id>/edit/', methods = ['GET', 'POST'])
def appointmant_edit(appointment_id):
    return 'Form to edit appointment #.'.format(appointment_id)

@app.route('/appointments/create/', methods = ['GET','POST'])
def appointment_create():
    return 'Form to create new appointment.'

@app.route('/appointments/<int:appointment_id>/delete/', methods  = ['DELETE'])
def appointment_delete(appointment_id):
    raise NotImplementedError('DELETE')

if __name__ == '__main__':
    app.run(debug=True)



# app.run('0.0.0.0:8000', debug=True)