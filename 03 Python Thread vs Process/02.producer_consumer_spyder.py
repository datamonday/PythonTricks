import queue, time, random, threading, os
import blog_spider


def do_craw(url_queue: queue.Queue, html_queue: queue.Queue):
    """
    Queue.get(block=True, timeout=None)
        - 从队列中移除并返回一个对象
    Queue.put(item)
        - 写入队列，timeout等待时间
    Queue.join()
        - 等到队列为空，再执行别的操作
    :param url_queue: url队列
    :param html_queue: 解析完成的网页源码队列
    :return: None
    """
    while True:
        url = url_queue.get()
        html = blog_spider.craw(url)
        html_queue.put(html)
        print(threading.current_thread().name, f"craw: {url}",
              "url_queue.size=", url_queue.qsize())

        time.sleep(random.randint(1, 2))


def do_parse(html_queue: queue.Queue, file_out):
    """
    在Python中，队列是最常用的线程间的通信方法，因为它是线程安全的，自带锁。
    生产者模块产生数据，放入缓冲区；消费者模块从缓冲区取出数据并进行处理。

    :param html_queue: 网页源码队列
    :param file_out: 保存的文件名
    :return: 将解析的网页内容报错到输出文件
    """
    while True:
        html = html_queue.get()
        results = blog_spider.parse(html)
        for result in results:
            file_out.write(str(result) + "\n")

        print(threading.current_thread().name, f"results.size", len(results),
              "html_queue.size=", html_queue.qsize())

        time.sleep(random.randint(1, 2))


if __name__ == "__main__":
    url_queue = queue.Queue()
    html_queue = queue.Queue()
    for url in blog_spider.urls:
        url_queue.put(url)

    n_thread_pro = 3
    for idx in range(n_thread_pro):
        t_pro = threading.Thread(target=do_craw,
                                 args=(url_queue, html_queue),
                                 name=f"craw_{idx}")
        t_pro.start()  # 启动线程

    try:
        file_out = open("02.pro_con_output_results.txt", "w")

    except IOError:
        print("This file is not found！")
        os.mkfifo()

    else:
        file_out = open("02.pro_con_output_results.txt", "w")
        n_thread_con = 2
        for idx in range(n_thread_con):
            t_con = threading.Thread(target=do_parse,
                                     args=(html_queue, file_out),
                                     name=f"parse_{idx}")
            t_con.start()
