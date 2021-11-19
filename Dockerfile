FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /opt/yijunx/code

COPY './requirements.txt' .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["bash", "start.sh"]


