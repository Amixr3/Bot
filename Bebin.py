from rubpy import Client, Message, handlers
import asyncio, random, requests
#سازنده محرز
# گوید گپی که میخواین ربات توش ران کنید
group_guid = "g0DIu530e6cded1ee15715a17b47e89f"

#آموزش در چنل میزاریم @MohrazBot

def ChatGPT_tap30(prompt: str) -> dict:
    requests.session().cookies.clear()
    options_url = "https://api.tapsi.cab/api/v1/chat-gpt/chat/completion"
    headers = {
        "Access-Control-Request-Method": "POST",
        "Access-Control-Request-Headers": "content-type,x-agent",
        "Origin": "https://chatgpt.tapsi.cab",
    }
    requests.options(options_url, headers=headers)
    ip_address = "5.121.39.59"
    ip_parts = ip_address.split(".")
    random.shuffle(ip_parts)
    new_ip = ".".join(ip_parts)
    webkit_version = f"{random.randint(500, 600)}.{random.randint(0, 99)}"
    major_version = random.randint(100, 200)
    minor_version = random.randint(0, 9)
    build_version = random.randint(0, 9999)
    safari_version = f"{random.randint(500, 600)}.{random.randint(0, 99)}"
    user_agent = f"Mozilla/5.0 (Linux; Android 10; STK-L21) AppleWebKit/{webkit_version} (KHTML, like Gecko) Chrome/{major_version}.0.{minor_version}.{build_version} Mobile Safari/{safari_version}"
    post_url = "https://api.tapsi.cab/api/v1/chat-gpt/chat/completion"
    headers = {
        "Content-Type": "application/json",
        "X-Agent": user_agent,
        "X-Forwarded-For": new_ip,
        "Origin": "https://chatgpt.tapsi.cab",
    }
    data = {"messages": [{"role": "user", "content": prompt}]}
    try:
        return requests.post(post_url, headers=headers, json=data).json()
    except:
        return dict(result=False)


async def SendResultChatGPT(text: str, message: Message) -> None:
    await asyncio.sleep(2)
    result = ChatGPT_tap30(text)
    if result["result"] != None:
        await message.reply(result["data"]["message"]["content"])
    else:
        await message.reply("خطا، لطفا مجدد امتحان کنید.")


async def SendResultCreatePhoto(text: str, message: Message, app: Client) -> None:
    await asyncio.sleep(2)
    try:
        result = requests.get("https://haji-api.ir/prompts/?text=" + text).json()
        photo = requests.get(random.choice(result["result"]))
        await app.send_photo(
            object_guid=message.object_guid,
            photo=photo.content,
            file_name="created.jpg",
            caption="عکس شما ساخته شد.",
            reply_to_message_id=message.message_id,
        )
    except:
        await message.reply("خطا، لطفا مجدد امتحان کنید.")


async def main():
    async with Client(session="bot") as app:
        await app.send_message(group_guid, 
        "ربات هوش مصنوعی محرز با موفقیت فعال شد"
)
        @app.on(handlers.MessageUpdates())
        async def update_group(message: Message):
            if message.object_guid == group_guid:
                if message.raw_text != None:
                    if message.raw_text.startswith("//"):
                        text: str = message.raw_text.strip().replace("// ", "")
                        await message.reply(
                            "درخواست شما با موفقیت ثبت شد. لطفا چند لحظه صبر کنید . . ."
                        )
                        asyncio.create_task(SendResultChatGPT(text, message))

                    elif message.raw_text.startswith("/p"):
                        text: str = message.raw_text.strip().replace("/p ", "")
                        await message.reply(
                            "درخواست شما با موفقیت ثبت شد. لطفا چند لحظه صبر کنید . . ."
                        )
                        asyncio.create_task(SendResultCreatePhoto(text, message, app))
                    elif message.raw_text == "راهنما":
                        await message.reply(
                            "دستورات ربات : \n\n 1 - ( //سوال شما ) \n2 - ( /اسم عکس )"
                        
                        
                       )
                                                      
                        asyncio.create_task(SendResultCreatePhoto(text, message, app))
                    elif message.raw_text == "سازنده":
                        await message.reply(
                        "@Pv_Mahrez"
                        )      
                        
                        asyncio.create_task(SendResultCreatePhoto(text, message, app))
                    elif message.raw_text == "محرز":
                        await message.reply(
                        "@MohrazBot"
                        )
                        
                        asyncio.create_task(SendResultCreatePhoto(text, message, app))
                    elif message.raw_text == "محرز بات":
                        await message.reply(
                        "@MohrazBot"
                        )                                                                                   
                        asyncio.create_task(SendResultCreatePhoto(text, message, app))
                    elif message.raw_text == "سازندت کیه":
                        await message.reply(
                        "@Pv_Mahrez"
                        )

                        asyncio.create_task(SendResultCreatePhoto(text, message, app))
                    elif message.raw_text == "سازندت کیه؟":
                        await message.reply(
                        "@Pv_Mahrez"
                        )

                        asyncio.create_task(SendResultCreatePhoto(text, message, app))
                    elif message.raw_text == "ساخت ربات":
                        await message.reply(
                       "جهت ساخت ربات به کانال زیر مراجعه کنید"                             
                        "                        @MohrazBot"
                        )

        await app.run_until_disconnected()


asyncio.run(main())

#دست به سورس نزنید سورس دستکاری کنین ایپی تون مسدود میشع نمیتونید دیگه از ربات استفادع کنید
