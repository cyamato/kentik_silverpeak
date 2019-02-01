#!/bin/bash

echo Testing Silver Peak Auth
curl -i -k -X POST -H "Content-Type: application/json" -d '{"user":"Kentik","password":"Kronos@97"}' https://msp-us-orch.core.kronos.com
