#!/usr/bin/env bash

set -e

cat << EOF > getFilters.xml
<?xml version="1.0"?>
<getFilters>
    <profile name="tbcheck"/>
    <filter>
        <number>3295</number>
    </filter>
</getFilters>
EOF

curl -X POST -k --header "X-SMS-API-KEY: $(cat api_key.txt)" --form name=@getFilters.xml https://192.168.184.102/ipsProfileMgmt/getFilters