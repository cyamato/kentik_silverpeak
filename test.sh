#!/bin/bash
# echo
baseURL='http://msp-us-orch.core.kronos.com/gms/rest'
data='{"user":"kentik","password":"Kronos@78"}'
echo "$data"

echo
echo Testing Silver Peak Auth
curl -i -k -L -X POST -H "Content-Type: application/json" -d "$data" $baseURL/authentication/login

# echo
# echo Testing Silver Peak Auth Type
# curl -i -k -L -X POST -H "Content-Type: application/json" -d "$data" $baseURL/authentication/userAuthType

echo
echo Testing Silvver Peak Login Status
curl -i -k -L -X GET $baseURL/authentication/loginStatus