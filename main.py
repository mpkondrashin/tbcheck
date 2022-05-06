#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# TBCheck (c) 2022 by Michael Kondrashin (mkondrashin@gmail.com)
#

from config import settings
from sms import SMS


def main():
    try:
        settings.sms.api_key = open('api_key.txt').read()
    except IOError as e:
        pass
    print(settings.sms.api_key)
    print(settings.sms.url)
    print(settings.sms.skip_tls_verify)
    sms = SMS(settings.sms.url, settings.sms.api_key).set_insecure_skip_verify(True)
    count_missing = 0
    #for n in range(1, 100000):
    n = 51
    result = sms.get_filter(settings.profile.name, 'number', n)
    filter_name = result.find('filter/name')#/filter/name").text
    action_name = result.find('filter/actionset').name#/filter/name").text
    if filter_name is None or action_name is None:
        #print(result)
        #continue
        pass
    print(filter_name.text, action_name.text)

if __name__ == '__main__':
    main()

