import asyncio


async def crawl_page_2(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))
    
    
async def main_2(urls):
    tasks = [asyncio.create_task(crawl_page_2(url)) for url in urls]
    for task in tasks:
        await task
        
asyncio.run(main_2(['url_1', 'url_2', 'url_3', 'url_4']))