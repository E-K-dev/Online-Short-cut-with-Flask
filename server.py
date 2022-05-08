from flask import (
	Flask,
	render_template,
	request,
	redirect,
	send_file
);
import random
import pyshorteners
from pyshorteners import *



from clean_function import (
	clean, # Importamos la funcion de clean.
	os
);

app = Flask(__name__);

port = int('5000');

@app.route('/' , methods=['get' , 'post'])
def main():
	try:
		return render_template(
			'homepage.html',
			Document_Title = 'Online Shortcuter',
			state='No hay Ningun Cambio'
		);
	except:
		exit()

@app.route('/information' , methods=['post'])
def info():
	try:
		result = random.randint(1,99);
		name = str('download-' + str(result) + '.txt')

		url = request.form.get('url'); # Obtenemos la data.
		Document_Title = 'Online Shortcuter'
		short = pyshorteners.Shortener(); # Funcion para obtener los enlaces
		
		tinyurl = short.tinyurl.short(f'{url}');
		isgd = short.isgd.short(f'{url}');
		osdb = short.osdb.short(f'{url}');

		to = open(name , 'wt');

		to.write(f'Acortado by Axel Ezequiel Kampmann Using Python\n\nTinyUrl = {tinyurl}\nIsGd = {isgd}\nOsDb = {osdb}');

		to.close();

		return send_file(f'./{name}', as_attachment=True);
	except:
		return render_template(
		'homepage.html',
		Document_Title = 'Online Shortcuter',
		state='La url no existe'
	);
@app.errorhandler(405)
def base_error_handler(e):
	return redirect('/')

def run():
	clean();
	app.run(
		port=port,
		debug=True
	);
	pass

run(); # Corremos la app.
