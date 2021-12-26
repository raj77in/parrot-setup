#/bin/bash
ip -4 -o -c=never -br -p a s dev eth0 |awk '{print $3}'
