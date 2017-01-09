FROM debian:latest
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get -y upgrade
RUN apt-get -y --no-install-recommends install python

ENTRYPOINT ["python", "-m", "SimpleHTTPServer"]
