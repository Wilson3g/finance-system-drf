FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /finance
WORKDIR /finance
ADD requirements.txt /finance/
RUN pip install --upgrade pip  && pip install -r requirements.txt
ADD . /finance