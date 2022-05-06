#!/usr/bin/env bash


curl -k --header "X-SMS-API-KEY: $(cat api_key.txt)" "https://192.168.194.102/dbAccess/tptDBServlet?method=DataDictionary&table=ACTIONSET"
