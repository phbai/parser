FROM python:2.7-slim
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip \
	  && pip install -r requirements.txt
EXPOSE 8000
# CMD gunicorn -D -w 2 main:app
CMD ["python", "main.py"]
