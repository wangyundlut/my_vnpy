#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
提供配置文件的统一接口
不同的项目地址需要修改这个地址
"""

import configparser
import os
from config import Project_path
# 不同的本机地址需要修改这个东西
file_cwd = os.path.join(Project_path, 'config')


def config_api(content):
    # 提供需要的接口文字，返回接口
    config = configparser.ConfigParser()

    if content == 'constant':
        file_name = os.path.join(file_cwd, 'constant.ini')
    elif content == 'text':
        file_name = os.path.join(file_cwd, 'text.ini')
    elif content == 'global_setting':
        file_name = os.path.join(file_cwd, 'global_setting.ini')
    elif content == 'event_type':
        file_name = os.path.join(file_cwd, 'event_type.ini')
    elif content == 'ctaBase':
        file_name = os.path.join(file_cwd, 'ctaBase.ini')
    config.read(file_name, encoding='utf-8')

    return config


