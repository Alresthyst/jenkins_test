docker build -t develop .
docker rmi -f $(docker images -q -f dangling=true)
docker run -p 8180:8180 -e server_mode=develop develop