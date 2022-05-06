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
    action_name = result.find('filter/actionset')
    if filter_name is None or action_name is None:
        #print(result)
        #continue
        pass
    actionset_name = action_name.attrib['name']
    print(filter_name.text, action_name.attrib['name'])
    for action_from, action_to in settings.profile.action_sets:
        if action_from == actionset_name:
            print("change to", action_to)
            result = sms.set_filters_action_set(settings.profile.name, n, action_to)
            print(result)

if __name__ == '__main__':
    main()

