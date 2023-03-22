from src.lessons.lesson_7.lesson_7 import *
# from src.lesson_1 import decker_help

# https://andreyex.ru/linux/komanda-zapuska-docker-s-primerami/

# Docker, сборка образа
# docker build -t hello-world .

# Docker, просмотр образов

# docker images
# docker ps -a
# docker ps -a -q (айдишники)

# Docker, запуск
# docker run --rm --name test_img hello-world
# docker run --rm --name test_img -p 8080:8080 hello-world
# docker run --rm --name test_img -p 8080:8080 -e TZ=Europe/Moscow hello-world
# docker run --rm --name test_img -p 8080:8080 -e TZ=Europe/Moscow -v hello:/usr/src/app/src/ hello-world
# docker run --rm -d --name test_img -p 8080:8080 -e TZ=Europe/Moscow -v hello:/usr/src/app/src/ hello-world
# docker run --name test_img hello-world

# Docker, удаление образа
# docker rm "чтото из параметров"
# docker rm $(docker ps -qa)
# docker rm -vf $(docker ps -a -q)
# docker rmi -f $(docker images -a -q)
# docker rm -f SOMENAME
# $images = docker images -a -q
# foreach ($image in $images) { docker image rm $image -f }

# Остановка
# docker stop $(docker ps -q) -a

# pip
# pip install -r requirements.txt

# volume
# docker volume ls

print(docker_help())
