#!/bin/bash
echo
data='{"user":"kentik","password":"Kronos@78"}'
echo "$data"
echo
echo Testing Silver Peak Auth
curl -i -k -L -X POST -H "Content-Type: application/json" -d "$data" https://msp-us-orch.core.kronos.com/rest/authentication/login

echo
echo Testing Silver Peak Auth Type
curl -i -k -L -X POST -H "Content-Type: application/json" -d "$data" https://msp-us-orch.core.kronos.com/rest/authentication/userAuthType

echo
echo Testing Silvver Peak Login Status
curl -i -k -L -X GET https://msp-us-orch.core.kronos.com/rest/authentication/loginStatus