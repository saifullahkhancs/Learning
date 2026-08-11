from http.client import responses
from math import trunc
import logging
from flask import Flask, redirect, url_for , request, render_template
from elasticsearch import Elasticsearch
app = Flask(__name__)
es = Elasticsearch([{'host': 'localhost', 'port': 9200 ,  'scheme': 'http'}],
basic_auth=("elastic", "Sw9FS-lCn=lcRFe2vho4"))

@app.route('/')
def hello_world():
   try:
      responses = es.ping()
      if responses:
         return "Connected to Elasticsearch!"
      else:
         return "Could not connect to Elasticsearch.", 503
   except Exception as e:
      logging.error(f"Elasticsearch health check failed: {e}")
      return f"Elasticsearch error: {str(e)}", 503
@app.route('/hello/<name>')
def hello_name(name):
   return f'Hello {name}'

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest


# The url_for() function is very useful for dynamically building a URL for a specific function. The function accepts
# the name of a function as first argument, and one or more keyword arguments, each corresponding to the variable part
# of URL.

@app.route('/user/<name>')
def user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest', guest=name))



@app.route('/login' , methods= ['GET', 'POST'])
def login():
   if request.method == 'POST':
      user = request.form.get('username')
      if not user:
         return "Username is required", 400
      logging.info(user)
      return redirect(url_for('hello_guest', guest=user))
   else:
      user = request.args.get('username')
      if not user:
         return "Username query parameter is required", 400
      return redirect(url_for('hello_guest', guest=user))



if __name__ == '__main__':
   # app.run(debug=True,  host='0.0.0.0', port=5000,  )

   app.run(debug=True)