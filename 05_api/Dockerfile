FROM tiangolo/uvicorn-gunicorn:python3.7

RUN apt-get update
RUN apt-get install python

WORKDIR /home/project/app

COPY requirements.txt /home/project/app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /home/project/app

ENTRYPOINT ["uvicorn"]
CMD ["app.main:app", "--debug", "--host", "0.0.0.0","--port", "5000"]
