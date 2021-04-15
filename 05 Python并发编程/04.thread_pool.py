import blog_spider
import concurrent.futures


with concurrent.futures.ThreadPoolExecutor() as pool:
    htmls = pool.map(blog_spider.craw, blog_spider.urls)
    htmls = list(zip(blog_spider.urls, htmls))
    for url, html in htmls:
        print(url, len(html))

print("craw over")

# parse
with concurrent.futures.ThreadPoolExecutor() as pool:
    futures = {}
    for url, html in htmls:
        future = pool.submit(blog_spider.parse, html)
        futures[future] = url

    # # 方式1：等待全部完成后再返回
    # for future, url in futures.items():
    #     print(url, future.result())

    # 方式2：逐次返回
    for future in concurrent.futures.as_completed(futures):
        url = futures[future]
        print(url, future.result())
