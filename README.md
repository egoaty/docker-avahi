# egoaty/avahi
Container with simple Avahi mDNS/DNS-SD to publish own address and hostname

## Running the container

Docker compose example:

```
version: "2"

services:
  avahi:
    image: egoaty/avahi
    environment:
      - TZ=Europe/Vienna
    hostname: myhostname
    networks:
      network_lan:
        ipv4_address: 192.168.1.100
    restart: unless-stopped
```

