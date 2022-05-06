#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# TBCheck (c) 2022 by Michael Kondrashin (mkondrashin@gmail.com)
#

from config import settings
from sms import SMS


def main():
    print(settings.sms.api_key)
    print(settings.sms.url)
    print(settings.sms.skip_tls_verify)
    sms = SMS(settings.sms.url, settings.sms.api_key).set_insecure_skip_verify(True)
    result = sms.get_filters('test', 'number', 51)
    print(result)

if __name__ == '__main__':
    main()

