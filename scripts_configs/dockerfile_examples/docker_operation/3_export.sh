#!/bin/sh


if [ $# -lt 1 ] ; then
    echo 'Usage: '..$0..'<container_id>'
    exit
fi

docker export $1 > ./my_tcp_server.tar

