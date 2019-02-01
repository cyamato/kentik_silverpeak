#!/bin/bash

echo Testing Silver Peak Auth
curl -i -k -X POST -d "{user:Kentik,password:Kronos@97}" https://msp-us-orch.core.kronos.com
