FROM python:3.7
ENV PYTHONBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip3 install -r requirements.txt
ADD . /code/

WORKDIR /code/
CMD ["gunicorn", "-b", "0.0.0.0:8000", "hello:app", "-w", "4", "-k", "uvicorn.workers.UvicornWorker"]
