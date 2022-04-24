#!/usr/bin/env python3

from datetime import datetime

from flask import Flask
app = Flask(__name__)

@app.route('/')
def check():
   now = datetime.now() 
   dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
   return( dt_string)	 


if __name__ == '__main__':
    app.run()
