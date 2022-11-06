FROM python:3.9

ADD check.py .

RUN pip install nsepython

CMD ["python","./check.py"]

