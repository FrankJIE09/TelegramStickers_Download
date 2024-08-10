import asyncio
import os
import requests
from telegram import Bot

# 替换为你的Bot Token
bot = Bot(token='5640863500:AAGgnofomUMC1zn9c8CmW5CnfJQhBtX7LUk')

# 替换为你要下载的Sticker Set名称
sticker_set_name = 'niubiuniu_by_WuMingv2Bot'


async def download_stickers():
    # 获取Sticker Set
    sticker_set = await bot.get_sticker_set(name=sticker_set_name)

    # 创建一个文件夹来保存Sticker
    if not os.path.exists(sticker_set_name):
        os.makedirs(sticker_set_name)

    # 下载每一个Sticker
    for sticker in sticker_set.stickers:
        file_id = sticker.file_id
        file = await bot.get_file(file_id)
        file_path = os.path.join(sticker_set_name, f'{sticker.file_unique_id}.webp')

        # 下载文件
        file_url = file.file_path
        response = requests.get(file_url)

        # 将文件保存到本地
        with open(file_path, 'wb') as f:
            f.write(response.content)

    print(f"Stickers from '{sticker_set_name}' have been downloaded successfully.")


# 执行异步任务
asyncio.run(download_stickers())
