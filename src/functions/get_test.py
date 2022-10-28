from services.dbConnection import execute_query

def get_test():
  try:
    sql = "SELECT * FROM contenedores"
    return execute_query(sql)

  except:
    return 'Error al ejecutar la sentencia SQL'