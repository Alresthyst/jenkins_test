export mode=develop


docker build -t $mode .
if [ $(docker images -q -f dangling=true) > 0 ]; then
    docker rmi -f $(docker images -q -f dangling=true)
else
  echo "There is no dangling images"
fi

if [ $(docker ps -q -f ancestor=$mode) > 0 ]; then
    docker stop $(docker ps -q -f ancestor=$mode)
else
  echo "There is running old version of server"
fi

docker run -p 8180:8180 -e server_mode=develop -d develop