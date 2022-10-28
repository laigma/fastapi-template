<img src="https://www.python.org/static/community_logos/python-logo.png" alt="python" height="60"/>
<img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="fastapi" height="60"/>
<img src="https://pipenv-es.readthedocs.io/es/latest/_static/pipenv.png" alt="pipenv" height="60"/>

# FastApi template

## Requisitos
- Python 3.6 o superior
- Pip
- Pipenv

## 1. Configurar variables (.env)
- DEVELOPMENT_HOST
- DEVELOPMENT_PORT
- INTEGRATION_HOST
- INTEGRATION_PORT
- PRODUCTION_HOST
- PRODUCTION_PORT

## 2. Instalar entorno de ejecución
```
pipenv install
```

## 3. Ejecutar scripts

### Linux shell
Entorno development
```
pipenv run dev
```

Entorno integration
```
pipenv run int
```

Entorno production
```
pipenv run prod
```

### Win cmd
Entorno development
```
pipenv run wdev
```

Entorno integration
```
pipenv run wint
```

Entorno production
```
pipenv run wprod
```

## 4. Despliegue (Docker)

### Entorno integration
```
docker-compose -f ./docker.compose.int.yml up --build -d
```

### Entorno producción
```
docker-compose up --build -d  (producción)
```
