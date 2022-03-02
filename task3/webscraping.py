import aiohttp
import asyncio
from bs4 import BeautifulSoup

class WebScraper(object):
    def __init__(self, urls):
        self.urls = urls
        self.all_data  = []

        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(self.main())

    async def fetch(self, session, url):
        try:
            async with session.get(url) as response:

                text = await response.text()

                return text,url
        except Exception as e:
            print(str(e))
            
    def print_data(self, html):
        try:
            soup = BeautifulSoup(html, 'html.parser')
            print('Product: '+soup.title.text.split()[1])
            container = soup.find_all('h2',{'class':'a-size-mini a-spacing-none a-color-base s-line-clamp-2'})
            price = soup.find_all('span',{'class':'a-offscreen'})
            for i,j in zip(container,price):
                print(i.a.span.text.strip(),j.text.strip())
            print('<------------------------------------------------------------------------------>')

        except Exception as e:
            print(str(e))

    async def main(self):
        tasks = []
        headers = {
            "user-agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}
        async with aiohttp.ClientSession(headers=headers) as session:
            for url in self.urls:
                tasks.append(self.fetch(session, url))

            htmls = await asyncio.gather(*tasks)
            self.all_data.extend(htmls)

            for html in htmls:
                if html is not None:
                    html = html[0]
                    self.print_data(html=html)
                else:
                    continue

urls = [ ]
n = int(input('no of products: '))
for _ in range(n):
    urls.append('https://www.amazon.in/s?k=' + input('name of the product: '))
scraper = WebScraper(urls = urls)
