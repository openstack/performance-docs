FROM debian:latest
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get -y upgrade
RUN apt-get -y --no-install-recommends install python

ADD minion.py /opt/minion/minion
RUN chmod 0777 /opt/minion/minion

ENTRYPOINT ["/opt/minion/minion"]
