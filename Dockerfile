FROM python:2.7-alpine
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip \
	  && pip install -r requirements.txt
# CMD gunicorn -D -w 2 main:app
CMD ["python", "main.py"]