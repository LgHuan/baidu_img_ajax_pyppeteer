#saynico定义协程，await挂起阻塞的异步程序，对耗时操作挂起
import asyncio
#谷歌chrome官方无头框架puppeteer的python版本pyppeteer
import base64
from io import BytesIO
from urllib import request
from PIL import Image
from pyppeteer import launch
from lxml import etree
i=0
class Pyppeteer():
    async def init(self):
        # 'headless': False如果想要浏览器隐藏更改False为True
        #’--disable-infobars‘：禁用浏览器正在被自动化程序控制的提示
        self.browser=await launch(headless=False, args=['--disable-infobars'])
        self.page = await self.browser.newPage ( )
        self.pages=10

    async def Requests(self):
        await self.page.goto('http://image.baidu.com/')
        await self.page.evaluate (
            '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
        await asyncio.sleep (1)
        await self.page.type('#kw','小狗')
        await self.page.click('.s_search')
        await asyncio.sleep (2)
        while self.pages>0:
            # document.body.scrollHeight滑动条的长度，加1是为了实现鼠标下滑从而网页自动加载
            #需要爬取pages页，即循环需要下滑pages次
            await self.page.evaluate('window.scrollBy(0, document.body.scrollHeight+1)')
            self.pages-=1
            await asyncio.sleep (1)
            print('翻页')
        await asyncio.sleep(5)
        page_text=await self.page.content()
        #print(page_text)
        return page_text

    def parse(self,page_text):
        tree=etree.HTML(page_text)
        div_list=tree.xpath('//img[@class="main_img img-hover"]/@src')
        return div_list

    async def bg_image(self,args):
        global i
        for arg in args:
            #图片是异步加载方式
            if arg[-3:]=='jpg':
                print(arg)
                request.urlretrieve(arg,f'./小狗图片/{i}.jpg')
            #图片是base64编码方式
            else:
                arg=arg.replace('data:image/jpeg;base64,', "")
                bg_image_bytes = base64.b64decode (arg)#解码为unicode
                bg_image = Image.open (BytesIO(bg_image_bytes))#需要rb=read_byte模式
                bg_image.save(f'./小狗图片/{i}.jpg')
            i+=1

    async def close(self):
        await self.browser.close()

    async def run(self):
        await self.init ( )
        page_text = await self.Requests ( )
        img_list = self.parse (page_text)
        await self.bg_image (img_list)

asyncio.get_event_loop().run_until_complete(Pyppeteer().run())