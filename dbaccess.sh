#!/usr/bin/env bash


echo curl -k --header "X-SMS-API-KEY: $(cat api_key.txt)" "https://192.168.184.102/dbAccess/tptDBServlet?method=DataDictionary&table=ACTIONSET"
curl -k --header "X-SMS-API-KEY: $(cat api_key.txt)" "https://192.168.184.102/dbAccess/tptDBServlet?method=DataDictionary&table=ACTIONSET"
