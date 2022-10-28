import os

# En función del comando que ejecuta, propagamos las variables del archivo .env
def get_environment_variables():
  try:
    environment = os.environ['APIENV']
    if (environment == 'development'):      
      host = os.environ['DEVELOPMENT_HOST']
      port = os.environ['DEVELOPMENT_PORT']
      db_credentials = os.environ['DEVELOPMENT_DB']

    elif (environment == 'integration'):
      host = os.environ['INTEGRATION_HOST']
      port = os.environ['INTEGRATION_PORT']
      db_credentials = os.environ['INTEGRATION_DB']
    
    elif (environment == 'production'):
      host = os.environ['PRODUCTION_HOST']
      port = os.environ['PRODUCTION_PORT']
      db_credentials = os.environ['PRODUCTION_DB']
    
    else:
      host = None
      port = None
      db_credentials = None

  except:
    print('No se ha definido la variable APIENV')

  return({ 
    'environment': environment,
    'host': host,
    'port': port,
    'db_credentials': db_credentials
  })