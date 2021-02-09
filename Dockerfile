ARG DISTRO=alpine:3
FROM $DISTRO

RUN \
  apk add --no-cache tzdata avahi avahi-tools && \
  rm -f /etc/avahi/services/*

COPY root/ /

CMD /run.sh

