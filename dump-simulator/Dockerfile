
# Usage:  docker build -t dump-simulator .

FROM python:2.7.14-jessie
MAINTAINER Derek C. Ashmore

ENV DUMP_SIZE_IN_KB=10
ENV CRASH_MESSAGE=crashed
ENV INTERNAL_DUMP_DIR=/tmp/coredumps

RUN mkdir /app
RUN mkdir $INTERNAL_DUMP_DIR
RUN wget -O /app/dump_simulator.py https://raw.githubusercontent.com/Derek-Ashmore/python-samples/master/dump-simulator/dump_simulator.py
RUN wget -O /app/requirements.txt https://raw.githubusercontent.com/Derek-Ashmore/python-samples/master/dump-simulator/requirements.txt
RUN cat /app/requirements.txt
RUN pip install -r /app/requirements.txt

WORKDIR /app

RUN groupadd python
RUN useradd -ms /bin/bash -g python pythonuser
RUN chown pythonuser:python -R /app
RUN chmod -R 700 /app
USER pythonuser

CMD ["python", "dump-simulator.py", "--size", "$DUMP_SIZE_IN_KB", , "--out", "$INTERNAL_DUMP_DIR/test.dump", , "--message", "$CRASH_MESSAGE"]
