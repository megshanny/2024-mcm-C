# 导入必要的库
import numpy as np
import pandas as pd
import json
import time
import sys
import os
import warnings
import builtins

# 定义文件和日志路径
file_path = './file/'
log_path = './log/'

# 获取当前时间的格式化字符串
start_time = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))

# 检查路径是否存在的函数
def test_path(file_path):
    return os.path.exists(file_path)

# 将数据保存到JSON文件的函数
def save(output_data, file_name=''):
    # 将某些数据类型转换为可JSON序列化的格式
    for key, value in output_data.items():
        if isinstance(value, np.ndarray):
            output_data[key] = value.tolist()
        elif isinstance(value, pd.core.series.Series):
            output_data[key] = value.tolist()
        elif isinstance(value, pd.core.frame.DataFrame):
            output_data[key] = value.to_dict(orient='records')
        else:
            pass
    # 获取当前时间用于文件名
    now_time = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
    # 如果未提供文件名，则设置默认文件名
    if file_name == '':
        file_name = 'save' + now_time + '.json'
    else:
        file_name = file_name + '-save-' + now_time + '.json'
    # 检查指定的文件路径是否存在，否则发出警告
    if test_path(file_path):
        file_name = file_path + file_name
    else:
        warnings.warn('文件路径不存在，保存文件在当前路径', category=UserWarning, stacklevel=0)
    # 将数据保存到JSON文件
    with open(file_name, 'w') as f:
        json.dump(output_data, f)

# 从JSON文件加载数据的函数
def load(file_name):
    try:
        with open(file_name, 'r') as f:
            data = json.load(f)
    except:
        warnings.warn('无法打开文件', category=UserWarning, stacklevel=0)
        data = {}
    return data

# 将警告重定向到日志文件的函数
def no_warn():
    # 根据启动时间创建日志文件名
    file_name = 'warn-' + start_time + '.log'
    # 检查指定的日志路径是否存在，否则发出警告
    if test_path(log_path):
        file_name = log_path + file_name
    else:
        warnings.warn('日志路径不存在，保存日志在当前路径', category=UserWarning, stacklevel=0)
    # 将标准错误重定向到日志文件
    sys.stderr = open(file_name, 'w') 

# 在控制台和日志文件中打印的函数
def print(*args, **kwargs):
    # 根据启动时间创建日志文件名
    file_name = 'print-' + start_time + '.log'
    # 检查指定的日志路径是否存在，否则发出警告
    if test_path(log_path):
        file_name = log_path + file_name
    else:
        warnings.warn('日志路径不存在，保存日志在当前路径', category=UserWarning, stacklevel=0)
    # 将打印语句附加到日志文件
    with open(file_name, 'a') as f:
        builtins.print(*args, file=f, **kwargs)
    # 在控制台打印
    builtins.print(*args, **kwargs)
