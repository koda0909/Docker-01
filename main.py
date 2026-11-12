# Docker 설치 방법
wsl --install
wsl 설치후 winget install -e --id Docker.DockerDesktop
# Docker 버젼 확인
docker --version
Docker version 29.9.2, build a82e528
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world 
이렇게뜬다

# Docker 작동 확인
docker run hello-world
Hello from Docker!
This message shows that your installation appears to be working correctly.
이렇게 뜬다

# 이미지 받는법(nginx)
docker pull nginx
# 이미지 확인
docker images
IMAGE                ID             DISK USAGE   CONTENT SIZE   EXTRA
hello-world:latest   c567b231f656       25.9kB         9.49kB   U
nginx:latest         165ddde8751e        243MB         66.8MB
이렇게 뜨는게 정상

# Docker 키고 끄는법
docker run -d --name (이름)
이게 키는법
docker stop (이름)
이게 끄는법

# 이미지와 컨테이너 삭제법
docker rmi (이름)
이미지 삭제법이고
docker stop (이름)
로 컨테이너를 멈추고
docker rm (이름)
으로 삭제후
docker ps -
로 삭제되었는지 체크

docker run -d --name 이름 -p 8080:80 이미지	
뒤에서 켜기, 이름 붙이기, 내 컴퓨터 8080을 컨테이너 80에 잇기

# 컨테이너가 남긴 기록 보기
docker logs (이름)

# 앞에 켜진 컨테이너 끄는법
ctrl + c