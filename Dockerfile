FROM python:3.10.7
WORKDIR /testing_app
COPY . /testing_app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python ./app.py