FROM python:3.6
RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

copy . /usr/src/app/

CMD ["python", "docker_lesson.py"]
