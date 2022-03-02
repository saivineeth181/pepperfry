FROM python:3.9.5
ENV PYTHONBUFFRED=1

WORKDIR /task2
ADD . /task2
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY  . /task2/
CMD ["uvicorn", "main:app","--reload","--host", "0.0.0.0", "--port", "5000"]

