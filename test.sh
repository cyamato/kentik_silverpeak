#!/bin/bash
# echo
baseURL='https://msp-us-orch.core.kronos.com:443/gms/rest'

echo
echo Testing Silver Peak Auth
curl -k -L -H "Content-Type: application/json" -X POST -d '{"user":"kentik","password":"Kronos@78"}' $baseURL/authentication/login

sleep 5

echo
echo Testing Silvver Peak Tunnel Status
curl -k -L -X GET $baseURL/stats/aggregate/tunnel