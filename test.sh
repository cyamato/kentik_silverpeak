#!/bin/bash
echo
echo Testing Silver Peak Auth
data='{"user":"KentikBad","password":"Kronos@97"}'
echo "$data"
curl -i -k -X POST -H "Content-Type: application/json" -d "$data" https://msp-us-orch.core.kronos.com/authentication/login

echo
echo Testing Silver Peak Auth Type
data='{"user":"Kentik","password":"Kronos@97"}'
echo "$data"
curl -i -k -X POST -H "Content-Type: application/json" -d "$data" https://msp-us-orch.core.kronos.com/authentication/userAuthType
