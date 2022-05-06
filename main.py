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
    for n in range(1, 100000):
        result = sms.get_filters('test', 'number', n)
        name = result.find('filter/name')#/filter/name").text
        if name is None:
            print("Missing name")
            return
        print(name.text)

if __name__ == '__main__':
    main()

