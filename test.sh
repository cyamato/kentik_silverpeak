#!/bin/bash
echo
echo Testing Silver Peak Auth
$1 = '{"user":"KentikBad","password":"Kronos@97"}'
echo $1
curl -i -k -X POST -H "Content-Type: application/json" -d "$1" https://msp-us-orch.core.kronos.com/authentication/login
