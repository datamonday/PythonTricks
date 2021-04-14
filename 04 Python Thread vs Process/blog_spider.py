import requests
from bs4 import BeautifulSoup


urls = [
    # f"https://www.cnblogs.com/#p{page}"
    f"https://www.cnblogs.com/sitehome/p/{page}"
    for page in range(1, 10 + 1)
]


def craw(url):
    """
    爬取网页函数
    :param url: 被爬取的网页链接
    :return: 爬取的文本
    """
    r = requests.get(url)
    # r.text 以文本形式获取网页源码
    return r.text


def parse(html):
    """
    解析网页源码
    :param html: craw函数返回的网页源码
    :return: 返回网页标题和网址
    """
    # BeautifulSoup通过解析文档提供需要抓取的数据
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a", class_="post-item-title")

    return [(link["href"], link.get_text()) for link in links]


if __name__ == "__main__":
    for result in parse(craw(urls[2])):
        print(result)
