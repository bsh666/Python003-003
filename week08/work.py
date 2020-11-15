# -*- coding:utf-8 -*-

## 作业一：
### 容器序列
# - list
# - tuple
# - deque

### 扁平序列
# - str

### 可变序列
# - list
# - deque

### 不可变序列
# - str
# - tuple

## 作业二：
# 自定义一个 python 函数，实现 map() 函数的功能。

list(map(lambda x: print(x), [{"a": {"b": "c"}}, 1]))


def my_map(callback, iter_):
    return (callback(i) for i in iter_)


list(my_map(lambda x: print(x), [{"a": {"b": "c"}}, 1]))

## 作业三：
# 实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。
import time
import logging
from functools import wraps

logging.basicConfig(
    format='%(message)s',
    level=logging.INFO)


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        logging.info(time.time() - start)
        return result

    return wrapper


@timer
def test(arg1, arg2, kwarg1=None, kwarg2=None):
    print(arg1, arg2)
    print(kwarg1, kwarg2)
    time.sleep(2)


if __name__ == '__main__':
    test("arg1", "arg2", kwarg1=1)
