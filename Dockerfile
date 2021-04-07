ARG DISTRO=alpine:3
FROM $DISTRO

RUN \
  apk -U upgrade && \
  apk add -U --no-cache tzdata avahi avahi-tools && \
  rm -rf /var/cache/apk/* && \
  rm -f /etc/avahi/services/*

COPY root/ /

CMD /run.sh

