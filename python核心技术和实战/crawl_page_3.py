import asyncio


async def crawl_page_4(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))
    
    
async def main_4(urls):
    tasks = [asyncio.create_task(crawl_page_4(url)) for url in urls]
    await asyncio.gather(*tasks)
    
    
asyncio.run(main_4(['url_1', 'url_2', 'url_3', 'url_4']))