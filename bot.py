import requests
import random

BOT_TOKEN = "import requests
import random

BOT_TOKEN = "8614697948:AAGO-GfpZ6ScnbqLtew3zrExrI_ZfOvp454/getupdates"
CHAT_ID = "6202469595"

messages = [
    "💕 صباح النور يا ضوء عيوني، كل يوم بزيد حبك في قلبي زيادة ما ليها حد!",
    "🌹 يا زول، والله ما في كلام يوصف قديش أنتِ غالية عندي، قلبي ملكك وخلاص!",
    "💖 يا حبيبتي، لو الدنيا كلها اتقلبت، أنا ثابت ليكِ زي النجمة الما بتغيب!",
    "🌸 والله يا روحي، لمتك بفكر فيكِ وابتسم لوحدي، الناس فاكاني مجنون! 😂💝",
    "💝 يا أجمل واحدة، حبك ساكن في قلبي زي الأصيل، ما بمشي ولا بروح!",
    "🦋 يا نور عيوني، كل صبح بصحى وأول حاجة بتجي في بالي هي أنتِ!",
    "💗 يا ستي، والله الحياة من غيرك ما طعمها حلو، أنتِ السكر والعسل كلو!",
    "🌙 يا قمري، حتى النجوم بتحسدني عليكِ، لأني الزول الأحظ في الدنيا!",
    "💫 يا حبة عيني، كلامك العسل ده بدفيني وإن كان البرد قارس!",
    "🌺 يا ريحة الفل، وجودك في حياتي نعمة ما بستاهلها، بس ربنا كريم!",
]

songs = [
    "🎵 APT. - Rose & Bruno Mars\nhttps://youtu.be/ekr2nIex040",
    "🎵 Die With A Smile - Lady Gaga & Bruno Mars\nhttps://youtu.be/kPa7bsKwL-c",
    "🎵 Espresso - Sabrina Carpenter\nhttps://youtu.be/eVli-tstM5E",
    "🎵 Please Please Please - Sabrina Carpenter\nhttps://youtu.be/YPaFbCTSIdo",
    "🎵 Beautiful Things - Benson Boone\nhttps://youtu.be/mNG0PFRQqC8",
    "🎵 Stick Season - Noah Kahan\nhttps://youtu.be/9nBFC_KyFMU",
    "🎵 Too Sweet - Hozier\nhttps://youtu.be/IgqkTbJFQcg",
    "🎵 Cruel Summer - Taylor Swift\nhttps://youtu.be/ic8j13piAhQ",
]

def send_message():
    msg = random.choice(messages)
    song = random.choice(songs)
    
    text = f"{msg}\n\n🎶 أغنية اليوم ليكِ:\n{song}"
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": text})

send_message()
"
CHAT_ID = "6202469595"

messages = [
    "💕 صباح النور يا ضوء عيوني، كل يوم بزيد حبك في قلبي زيادة ما ليها حد!",
    "🌹 يا زول، والله ما في كلام يوصف قديش أنتِ غالية عندي، قلبي ملكك وخلاص!",
    "💖 يا حبيبتي، لو الدنيا كلها اتقلبت، أنا ثابت ليكِ زي النجمة الما بتغيب!",
    "🌸 والله يا روحي، لمتك بفكر فيكِ وابتسم لوحدي، الناس فاكاني مجنون! 😂💝",
    "💝 يا أجمل واحدة، حبك ساكن في قلبي زي الأصيل، ما بمشي ولا بروح!",
    "🦋 يا نور عيوني، كل صبح بصحى وأول حاجة بتجي في بالي هي أنتِ!",
    "💗 يا ستي، والله الحياة من غيرك ما طعمها حلو، أنتِ السكر والعسل كلو!",
    "🌙 يا قمري، حتى النجوم بتحسدني عليكِ، لأني الزول الأحظ في الدنيا!",
    "💫 يا حبة عيني، كلامك العسل ده بدفيني وإن كان البرد قارس!",
    "🌺 يا ريحة الفل، وجودك في حياتي نعمة ما بستاهلها، بس ربنا كريم!",
]

songs = [
    "🎵 APT. - Rose & Bruno Mars\nhttps://youtu.be/ekr2nIex040",
    "🎵 Die With A Smile - Lady Gaga & Bruno Mars\nhttps://youtu.be/kPa7bsKwL-c",
    "🎵 Espresso - Sabrina Carpenter\nhttps://youtu.be/eVli-tstM5E",
    "🎵 Please Please Please - Sabrina Carpenter\nhttps://youtu.be/YPaFbCTSIdo",
    "🎵 Beautiful Things - Benson Boone\nhttps://youtu.be/mNG0PFRQqC8",
    "🎵 Stick Season - Noah Kahan\nhttps://youtu.be/9nBFC_KyFMU",
    "🎵 Too Sweet - Hozier\nhttps://youtu.be/IgqkTbJFQcg",
    "🎵 Cruel Summer - Taylor Swift\nhttps://youtu.be/ic8j13piAhQ",
]

def send_message():
    msg = random.choice(messages)
    song = random.choice(songs)
    
    text = f"{msg}\n\n🎶 أغنية اليوم ليكِ:\n{song}"
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": text})

send_message()
