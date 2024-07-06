import asyncio

from tiktok_api.api.hashtag_async import HashtagaSync


async def get_hashtag_videos():
    async with HashtagaSync() as api:
        await api.create_playwright_instance()
        await api.create_playwright_session()
        tag = api.hashtag(name="funny")
        async for video in tag.videos(count=30):
            print(video)

        api.close()


if __name__ == "__main__":
    asyncio.run(get_hashtag_videos())
