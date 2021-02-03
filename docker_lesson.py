import src.lessons.lesson_1.lesson_1 as ls_1
import src.lessons.lesson_2.lesson_2 as ls_2
# from src.lesson_1 import decker_help

# https://andreyex.ru/linux/komanda-zapuska-docker-s-primerami/

# Docker, сборка образа
# docker build -t hello-world .

# Docker, просмотр образов:

# docker images
# docker ps -a
# docker ps -a -q (айдишники)

# Docker, запуск:
# docker run -t -i --rm --name test_img hello-world                             Запуск в интерактивном режиме с консолью
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

def start():
    print(ls_1.docker_help())
    print(ls_2.docker_help())
