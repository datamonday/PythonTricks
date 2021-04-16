```python
pip install 模块名字
```



![image-20210416161454790](C:\Users\34123\AppData\Roaming\Typora\typora-user-images\image-20210416161454790.png)

模块开发者需要做的三件事：

- 1）编写模块
- 2）将模块打包
- 3）上传到PyPI
  - 注册PyPI账号
  - 安装上传工具
  - 基于工具进行上传

---

# 1. 项目文件夹

假设要构建一个名为 `geekzero` 的包：

首先，根据要求创建以下文件：

![image-20210416170743135](C:\Users\34123\AppData\Roaming\Typora\typora-user-images\image-20210416170743135.png)

---

## 1.1 LICENCE.md

LICENSE为开源模块的许可证，用来声明模块的版权和用途。一般开源的软件会选择相对宽泛许可证 MIT，即：作者保留版权，无其他任何限制。

```python
The MIT License (MIT)

Copyright (c) 2021 datamonday

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```



更多其他许可证参见：https://choosealicense.com/

---

## 1.2 README.md

模块的描述信息，使用markdown格式编写。如：

```python
# geekzero

This is an test open source package named geekzero.

> Contributer: datamonday
> Github Repo: https://github.com/datamonday/PythonTricks
```



---

## 1.3 demos文件夹

编写模块的用例。

---

## 1.4 setup.py

`setup.py` 表示配置文件，用于给setuptools提供开源模块的相关信息，以在安装时进行匹配。如：

```python
import setuptools
with open("README.md", "r") as rd:
    long_description = rd.read()
setuptools.setup(
    name="geekzero",  # 模块名称
    version="1.0",  # 当前版本
    author="datamonday",  # 作者
    author_email="mondaycyb@gmail.com",  # 作者邮箱
    description="geek life",  # 模块简介
    long_description=long_description,  # 模块详细介绍
    long_description_content_type="text/markdown",  # 模块详细介绍格式
    # url="https://github.com/datamonday/PythonTricks",  # 模块github地址
    packages=setuptools.find_packages(),  # 自动找到项目中导入的模块
    # 模块相关的元数据
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # 依赖模块
    install_requires=[
        'pillow',
    ],
    python_requires='>=3',
)
```

---

## 1.5 geekzero目录

开源模块的相关代码保存在此文件夹中，如 `geek.py`

```python
def info():
    print("The word geek is a slang term originally used to describe eccentric or non-mainstream people; \
          in current use, the word typically connotes an expert or enthusiast obsessed with a hobby or intellectual pursuit,\
          with a general pejorative meaning of a peculiar person, especially one who is perceived to be overly intellectual, unfashionable, boring, or socially awkward."
          )
    # Reference:https://en.wikipedia.org/wiki/Geek
```

---

# 2. 打包上传

上述步骤中将文件夹和代码编写好之后，就需要对代码进行打包处理。

## 2.1 安装打包工具

打包代码需先安装setuptools和wheel两个工具，可以单独安装，也可以安装pip，从而自动安装这两个工具。

- Securely Download [get-pip.py](https://bootstrap.pypa.io/get-pip.py) [[1\]](https://packaging.python.org/tutorials/installing-packages/#id7)
- Run `python get-pip.py`. [[2\]](https://packaging.python.org/tutorials/installing-packages/#id8) This will install or upgrade pip. Additionally, it will install [setuptools](https://packaging.python.org/key_projects/#setuptools) and [wheel](https://packaging.python.org/key_projects/#wheel) if they’re not installed already.
  详见：https://packaging.python.org/tutorials/installing-packages/

注意：已安装用户，如要更新setuptools和wheel两个工具，可通过如下命令：

```
python -m pip install --upgrade setuptools wheel
```

![image-20210416170455557](C:\Users\34123\AppData\Roaming\Typora\typora-user-images\image-20210416170455557.png)

## 2.2 打包代码

```
python setup.py sdist bdist_wheel
```

![image-20210416171008168](C:\Users\34123\AppData\Roaming\Typora\typora-user-images\image-20210416171008168.png)

打包完之后的文件目录：

![image-20210416171057426](C:\Users\34123\AppData\Roaming\Typora\typora-user-images\image-20210416171057426.png)

---

## 2.3 发布模块（上传）

文件打包完毕后，需要将打包之后的文件上传到PyPI（需要先去 https://pypi.org/ 注册）。

- 安装用于发布模块的工具：twine 【已安装无需重复安装】

  ```shell
  python -m pip install --upgrade twine或pip install --upgrade twine
  # python -m 的作用是 run library module as a script (terminates option list)
  ```

- 发布（上传）

  ```shell
  python -m twine upload --repository-url https://upload.pypi.org/legacy/  dist/*或twine upload --repository-url https://upload.pypi.org/legacy/  dist/*
  ```

  上传时，提示需要输入PyPI的用户名和密码.

# 3.安装使用

## 3.1 安装

```
pip install geekzero
```

## 3.2 应用

```
from geekzero import geek.info()
```



---

Reference：https://pythonav.com/wiki/detail/6/95/

