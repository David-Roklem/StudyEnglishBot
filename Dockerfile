FROM python:3.10

COPY . .

WORKDIR .

RUN python -m pip install -r requirements.txt

EXPOSE 8000

CMD [ "python", "./main.py" ]