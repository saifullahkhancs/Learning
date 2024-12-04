FROM python:3.12.5
RUN apt update
WORKDIR /app
ADD requirements.txt /app
RUN pip3 install -r /app/requirements.txt

RUN groupadd -g 999 appuser && useradd -r -u 999 -g appuser appuser && chown -R appuser /app
USER appuser

ADD ./src /app

ENTRYPOINT ["python"]
CMD ["main.py"]