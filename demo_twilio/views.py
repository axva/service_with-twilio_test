# Download the twilio-python library from http://twilio.com/docs/libraries
from flask import Flask, request, redirect, url_for, render_template
from twilio.rest import Client
import os
from .services.twilio_service import TwilioService
from demo_twilio import app
# import json

# app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/notifications', methods = ['POST'])
def create():
    name = request.form['name']
    phone = request.form['phone']
    message = request.form['message']

    twilio_service = TwilioService()

    formatted_message = build_message(name, phone, message)
    try:
        twilio_service.send_message(formatted_message)
        flash('Listo, mensaje enviado', 'success')
    except TwilioRestException as e:
        print(e)
        flash('Oops! Hubo un error, intenta de nuevo.', 'danger')

    return redirect('/')

def build_message(name, phone, message):
    template = 'Mensaje nuevo recibido de {} a las {}. Mensaje: {}'
    return template.format(name, phone, message)


if __name__ == '__main__':
    app.run(debug = True)
