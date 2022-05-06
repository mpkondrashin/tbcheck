#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# TBCheck (c) 2022 by Michael Kondrashin (mkondrashin@gmail.com)
#

import sys

from config import settings
from sms import SMS


def get_refids(sms):
    # [item for sublist in a for item in sublist]
    action_sets = set([item for a in settings.profile.action_sets for item in a])
    print(action_sets)
    result = dict()
    for action in action_sets:
        action_set_refid = sms.action_set_refid(action)
        if action_set_refid == None:
            print("action not found: ", action)
            sys.exit(1)
        result[action] = action_set_refid
    return result


def main():
    try:
        settings.sms.api_key = open('api_key.txt').read()
    except IOError as e:
        pass
    print(settings.sms.api_key)
    print(settings.sms.url)
    print(settings.sms.skip_tls_verify)
    sms = SMS(settings.sms.url, settings.sms.api_key).set_insecure_skip_verify(True)
    refids = get_refids(sms)
    print(refids)
    action_set_refid = sms.action_set_refid(settings.profile.action_sets[0][1])
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
        print('Compare', action_from, actionset_name)
        if action_from == actionset_name:
            print("change to", action_to)
            refid = refids[action_to]
            result = sms.set_filters_action_set(settings.profile.name, n, refid)
            print(result)



if __name__ == '__main__':
    main()

