FROM python:3.12
EXPOSE 5000
WORKDIR /app
RUN pip install flask
COPY . .
CMD ["python","-m","flask", "run", "--host", "0.0.0.0"]