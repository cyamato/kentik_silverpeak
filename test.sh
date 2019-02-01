#!/bin/bash
echo
echo Testing Silver Peak Auth
curl -i -k -X POST -H "Content-Type: application/json" -d '{"user":"KentikBad","password":"Kronos@97"}' https://msp-us-orch.core.kronos.com/authentication/login
