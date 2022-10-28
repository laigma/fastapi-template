import uvicorn
from config import get_environment_variables

# Definimos variables de entorno
params = get_environment_variables()
environment = params['environment']
host = params['host']
port = int(params['port'])

if environment == 'development':
  reload_option = True
else:
  reload_option = False

# Instanciamos un servidor de uvicorn
if __name__ == "__main__":
  uvicorn.run("main:app", host = host, port = port, reload = reload_option)