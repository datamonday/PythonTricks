import blog_spider
import  threading
import time


def single_thread():
    print("single thread begin···\n")
    for url in blog_spider.urls:
        blog_spider.craw(url)
    print("single thread end!\n")


def multi_thread():
    print("multi thread begin···\n")
    threads = []
    for url in blog_spider.urls:
        threads.append(
            threading.Thread(target=blog_spider.craw,
                             args=(url,))
        )

    for thread in threads:
        # 线程转换为RUNNABLE状态
        thread.start()

    for thread in threads:
        # 让父线程等待子线程结束之后才能继续运行
        thread.join()

    print("multi thread end!\n")


if __name__ == "__main__":
    start = time.time()
    single_thread()
    end = time.time()
    print("single thread cost:", end - start, "seconds")

    start = time.time()
    multi_thread()
    end = time.time()
    print("multi thread cost:", end - start, "seconds")