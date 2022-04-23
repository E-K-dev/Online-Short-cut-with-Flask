from flask import (
	Flask,
	render_template,
	request
);

import pyshorteners
from pyshorteners import *

import os 
from os import *

from clean_function import clean # Importamos la funcion de clean.

app = Flask(__name__);

port = int('5000');

@app.route('/' , methods=['get' , 'post'])
def main():
	return render_template(
		'homepage.html',
		Document_Title = 'Online Shortcuter'
	);

@app.route('/information' , methods=['post'])
def info():
	url = request.form.get('url'); # Obtenemos la data.
	
	short = pyshorteners.Shortener(); # Funcion para obtener los enlaces
	
	tinyurl = short.tinyurl.short(f'{url}');
	isgd = short.isgd.short(f'{url}');
	osdb = short.osdb.short(f'{url}');

	return render_template(
		'acortado.html',
		tinyurl=tinyurl,
		isgd=isgd,
		osdb=osdb
	);

def run():
	clean();
	app.run(
		port=port,
		debug=True
	);
	pass

run(); # Corremos la app.