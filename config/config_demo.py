#!/usr/bin/env python
# -*- coding: utf-8 -*-


from config.config_api import config_api


def main():
    config = config_api('constant')
    # 获取部分
    section_list = config.sections()
    print(section_list)
    # 获取所有constant的options
    option_list = config.options('constant')
    print(option_list)
    # 获取所有items以字典的形式
    item_list = config.items('constant')
    print(item_list)
    # 获取具体内容
    offset = config.get('constant', 'EMPTY_STRING')
    print(offset)
    # 获取int
    int_test = config.getint('constant', 'EMPTY_INT')
    print(int_test)
    # 获取float
    float_test = config.getfloat('constant', 'EMPTY_FLOAT')
    config.getfloat('constant', 'EMPTY_FLOAT')
    print(float_test)

def main2():
    from config.config_api import config_api
    constant = config_api('constant')
    EMPTY_FLOAT = constant.getfloat('constant','EMPTY_FLOAT')
    EMPTY_INT = constant.getint('constant','EMPTY_INT')
    EMPTY_STRING = constant.get('constant','EMPTY_STRING')
    STATUS_UNKNOWN = constant.get('constant','STATUS_UNKNOWN')


if __name__ == '__main__':
    main2()
    print('begin?')
    main()