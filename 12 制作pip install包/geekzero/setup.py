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
