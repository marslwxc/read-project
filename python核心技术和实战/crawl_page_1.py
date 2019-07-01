import asyncio


async def crawl_page_1(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))
    
    
async def main_1(urls):
    for url in urls:
        await crawl_page_1(url)
        
asyncio.run(main_1(['url_1', 'url_2', 'url_3', 'url_4']))