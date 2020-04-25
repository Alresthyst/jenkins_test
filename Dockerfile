FROM kwk1602/ubuntu-python:v2

ENV server_mode=release

RUN mkdir /work_space
WORKDIR /work_space
COPY . .

RUN chmod +x init_parser.sh

CMD ./init_parser.sh --mode=$server_mode







