# baidu_img_ajax_pyppeteer
百度异步加载图片下载（pyppeteer,asynico,xpath,urlretrive,base64）
1、项目描述
下载百度ajaj加载的图片，实现页面自动下滑，一次性爬取多页的百度的ajax图片。asynico使程序可并发运行，提高速度。asynico协程的个人理解：轻量级的多线程，是不同程序之间的平发运行，而多线程是调度计算机资源的并发或并行运行。
2、技术难点
（1）百度反爬严格，采用谷歌chrome官方无头框架puppeteer的python版本pyppeteer，用pyppeteer实现滑动条自动下拉；（2）asynico使程序可并发运行，提高速度；（3）百度图片有异步加载链接模式和base64编码模式，因此使用两种模型对应的函数urlretrieve,base64保存；（3）模拟用户下拉滑动条，需要爬取多次页面，则执行几次js.
