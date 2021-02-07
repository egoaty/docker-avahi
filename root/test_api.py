#!/usr/bin/env python3

import docker
import socket

def get_networks_for_container(id):
  return api_client.inspect_container(id)['NetworkSettings']['Networks']

def get_my_networks():
  return get_networks_for_container(socket.gethostname())

def get_ip_for_container(id, network):
  container_networks = get_networks_for_container(id)
  if network in container_networks:
    print(get_networks_for_container(id)[network])
    ipam_config = get_networks_for_container(id)[network]['IPAMConfig']
    if 'IPv4Address' in ipam_config:
      return ipam_config['IPv4Address']

client = docker.from_env()
api_client = docker.APIClient(base_url='unix://var/run/docker.sock')

for my_network in get_my_networks():
  network = client.networks.get(my_network)
  for container in network.containers:
    print(get_ip_for_container(container.id, my_network))
