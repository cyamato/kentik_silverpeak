#!/bin/bash
# echo
baseCurlCmd='curl -i -k -L -H "Content-Type: application/json"'
baseURL='https://msp-us-orch.core.kronos.com:443/gms/rest'
data='{"user":"kentik","password":"Kronos@78"}'
echo "$data"

echo
echo Testing Silver Peak Auth
echo $baseCurlCmd -X POST -d "$data" $baseURL/authentication/login
$baseCurlCmd -d "$data" $baseURL/authentication/login

# echo
# echo Testing Silver Peak Auth Type
# curl -i -k -L -X POST -H "Content-Type: application/json" -d "$data" $baseURL/authentication/userAuthType

echo
echo Testing Silvver Peak Login Status
$baseCurlCmd -X GET $baseURL/authentication/loginStatus