FROM python:3.10

COPY . .
RUN pip install pipenv
RUN pipenv install
EXPOSE 8081
CMD ["pipenv", "run", "prod"]

# COPY requirements.txt .
# COPY .env .env
# RUN pip install -r requirements.txt
# EXPOSE 80
# COPY ./src /src
# ENV APIENV production
# CMD ["python", "src/run.py"]