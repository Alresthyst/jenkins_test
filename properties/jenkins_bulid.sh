#! /bin/bash

docker build -t develop .
if [ $(docker images -q -f dangling=true) > 0 ]; then
    docker rmi -f $(docker images -q -f dangling=true)
else
  echo "There is no dangling images"
fi
docker run -p 8180:8180 -e server_mode=develop develop