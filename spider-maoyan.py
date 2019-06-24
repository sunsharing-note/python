"""
抓取猫眼电影TOP100
"""

import re
import time
import requests

from bs4 import BeautifulSoup


class SpiderMaoyan(object):

    def __init__(self):
        # 通过分析URL可以发现, 猫眼电影TOP100页面是通过 offset + 10 来分页的
        self.url = "http://maoyan.com/board/4?offset={0}"
        # 设置一下UA, 否则有可能提示你访问被禁止了
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/66.0.3359.139 Safari/537.36"
        }
        # 定义需要提取的内容字段
        self.fields = ("id", "name", "movieUrl", "imgUrl", "star", "releaseTime", "score")

    def handler(self, offset=0):

        while offset < 100:
            response = requests.get(self.url.format(offset), headers=self.headers)
            if response.status_code == 200:
                print("INFO -> Current URL: <%s>" % response.url)
                # 编码处理一下, 不然有可能中文显示乱码
                r_html = response.text.encode(response.encoding).decode("utf-8")
                # 构建一个 BeautifulSoup 对象, 用于后续的标签、内容提取
                soup = BeautifulSoup(r_html, "html5lib")
                # 继续分析网页源代码, 发现每部影片都存在 <dd></dd> 标签中
                tags = soup.select("dd")
                # 提取内容
                for tag in tags:
                    # id、name、movieUrl
                    obj = tag.find("p", class_="name").select_one("a")
                    _id = re.search(r"movieId:(\d+)", obj.get("data-val")).group(1)
                    _name = obj.string
                    _movieUrl = "http://maoyan.com" + obj.get("href")
                    # img
                    # Tips: 可以将图片地址后面的分辨率去掉, 保存高清大图地址 .split("@")[0]
                    _imgUrl = tag.find("img", class_="board-img").get("data-src")
                    # star
                    # Tips: 中文标点
                    _star = tag.find("p", class_="star").string.strip().split("：")[-1]
                    # releaseTime
                    # Tips: 中文标点
                    _releaseTime = tag.find("p", class_="releasetime").string.split("：")[-1]
                    # score
                    _score = tag.find("p", class_="score").get_text()

                    # 接下来就可以将数据写入存储了
                    # Tips: 这种 SQL 生成方式有必要验证 key/val 是否成对出现
                    print(
                        "INSERT INTO TABLE_NAME (%s) VALUE %s;" % (
                            ", ".join(self.fields), tuple([_id, _name, _movieUrl, _imgUrl, _star, _releaseTime, _score])
                        )
                    )

                # 偏移量自增
                offset += 10
                # 有必要停顿一下
                time.sleep(.9)
            else:
                print(response.reason)
                exit(999)


if __name__ == "__main__":

    spider = SpiderMaoyan()
    spider.handler()
