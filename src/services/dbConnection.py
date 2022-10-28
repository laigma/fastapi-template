from sqlalchemy import create_engine
from config import get_environment_variables

# Definimos variables de entorno
params = get_environment_variables()
db_credentials = params['db_credentials']

print('Entorno de bbdd: ', db_credentials)

def execute_query(sql):
  engine = create_engine(db_credentials)
  con = engine.connect()  
  response = con.execute(sql)
  res = response.fetchall()
  con.close ()
  engine.dispose()
  return res        