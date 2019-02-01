#!/bin/bash
echo
data='{"user":"kentik","password":"Kronos@78"}'
echo "$data"
echo
echo Testing Silver Peak Auth
curl -i -k -X POST -H "Content-Type: application/json" -d "$data" https://msp-us-orch.core.kronos.com/8.5.2.40320/rest/json/authentication/login

echo
echo Testing Silver Peak Auth Type
curl -i -k -X POST -H "Content-Type: application/json" -d "$data" https://msp-us-orch.core.kronos.com/8.5.2.40320/rest/json/authentication/userAuthType

echo
echo Testing Silvver Peak Login Status
curl -i -k -X GET https://msp-us-orch.core.kronos.com/8.5.2.40320/rest/json/authentication/loginStatus