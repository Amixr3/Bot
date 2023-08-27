from rubpy import Client, handlers, models, Message
from asyncio import run, create_task
from bs4 import BeautifulSoup
import aiohttp


async def get_link(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            soup = BeautifulSoup(await response.text(), "html.parser")
            title = (
                soup.find("article", attrs={"class": "posts"})
                .find("header")
                .find("a")["title"]
            )
            musics = soup.find("div", attrs={"class": "boxdownload"})
            if musics != None:
                link = musics.find("a")
                return [link["href"], title]


async def search_music(artist: str):
    async with aiohttp.ClientSession() as session:
        url = f"https://bandmusic.ir/?s={artist}"
        async with session.get(url) as response:
            soup = BeautifulSoup(await response.text(), "html.parser")
            musics = soup.find_all("article", attrs={"class": "posts"})
            if musics != []:
                data = f"response search [ {artist} ]"
                for music in musics:
                    footer_link = music.find("footer", attrs={"class": "flex"})
                    header_res = music.find("h1")
                    if header_res == None:
                        if footer_link != None:
                            a_tag = footer_link.find("a", attrs={"class": "more"})
                            data = f"""{data}
                                
Title: {a_tag["title"]}
Link: {a_tag["href"]}
"""
                    else:
                        return header_res
                return data
            else:
                return f"not found music [ {artist} ] !"


async def download_music(link: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(link) as response:
            return await response.read()


async def send_music(client: Client, link: str, guid: str, message_id: str):
    await client.send_message(guid, "درحال دانلود موزیک صبر کنین لطفا", message_id)
    link_music = await get_link(link)
    music = await download_music(link_music[0])
    await client.send_message(guid, "درحال اپلود موزیک صبر کنید لطفا", message_id)
    await client.send_music(
        guid,
        music,
        file_name=link_music[1] + ".mp3",
        reply_to_message_id=message_id,
        performer="@Music_ClTY",
    )


async def main():
    async with Client("error") as client:

        @client.on(handlers.MessageUpdates(models.is_private))
        async def updates(message: Message):
            if message.raw_text != None and message.action == "New":
                if message.raw_text.startswith("موزیک"):
                    music_name = (
                        message.text.split("موزیک")[-1].replace(" ", "+").strip()
                    )
                    message_id = message.message_id
                    guid = message.author_guid
                    await client.send_message(
                        guid, "در حال سرچ موزیک", message_id
                    )
                    await client.send_message(
                        guid, await search_music(music_name), message_id
                    )
                elif message.text.startswith("دانلود"):
                    music_link = message.text.split("دانلود")[-1].strip()
                    create_task(
                        send_music(
                            client, music_link, message.author_guid, message.message_id
                        )
                    )

        await client.run_until_disconnected()


run(main())
