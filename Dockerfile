FROM python:3.7.0-stretch
WORKDIR /src
ADD requirements.txt /src/requirements.txt
RUN pip install -r /src/requirements.txt
ADD . /src
EXPOSE 8000
CMD python api.py