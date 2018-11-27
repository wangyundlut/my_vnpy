#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config.config_api import config_api

def main():
    constant = config_api('constant')
    EMPTY_FLOAT = constant.getfloat('constant', 'EMPTY_FLOAT')
    EMPTY_INT = constant.getint('constant', 'EMPTY_INT')
    EMPTY_STRING = constant.get('constant', 'EMPTY_STRING')
    STATUS_UNKNOWN = constant.get('constant', 'STATUS_UNKNOWN')
    print(constant.get('constant', 'EMPTY_NONE'))


if __name__ == '__main__':
    main()