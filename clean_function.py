import os 
from os import *
def clean():
	if os.name == 'nt' or os.name == 'msdos':
		os.system('cls');
		pass
	else:
		os.system('clear');
		pass
	pass

if __name__ == '__main__':
	clean(); # Exportamos la funcion clean.