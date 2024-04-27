from nonebot import get_plugin_config, logger, get_driver
from nonebot.plugin import PluginMetadata, on_command
from nonebot.adapters.onebot.v11 import Bot, Event, MessageSegment
from nonebot.rule import to_me
from httpx import AsyncClient
from .config import Config

config = get_driver().config
ip = config.yuapi_ip
prefix_ = list(config.command_start)
prefix = str(prefix_[0])

__plugin_meta__ = PluginMetadata(
    name="nonebot_plugin_ncheck",
    description="适配YUAPI的B站N查插件，需安装httpx驱动器，需在.env.prod中添加新项 YUAPI_IP="" ",
    usage="发送{prefix}YUAPI帮助查看所有指令",
    config=Config,
    supported_adapters={"~onebot.v11"},
)

config = get_plugin_config(Config)


config = get_driver().config
ip = config.yuapi_ip
prefix_ = list(config.command_start)
prefix = str(prefix_[0])
YUAPI状态 = on_command("YUAPI状态",  priority=1)
查直播 = on_command("查直播",  priority=1)
查场次 = on_command("查场次",  priority=1)
查成分 = on_command("查成分",  priority=1)
查藏品 = on_command("查藏品",  priority=1)
查视频 = on_command("查视频",  priority=1)
查充电 = on_command("查充电",  priority=1)
查房管 = on_command("查房管",  priority=1)
查关注 = on_command("查关注",  priority=1)
查航海 = on_command("查航海",  priority=1)
查牌子 = on_command("查牌子",  priority=1)
查uid牌子 = on_command("查uid牌子",  priority=1)
查装扮 = on_command("查装扮",  priority=1)
查粉丝团 = on_command("查粉丝团",  priority=1)
查房间状态 = on_command("查房间状态",  priority=1)
直播列表 = on_command("直播列表",  priority=1)
YUAPI帮助 = on_command("YUAPI帮助",  priority=1)


async def fetch(url: str):
    async with AsyncClient() as client:
        response = await client.get(url, timeout=30)
        return response.content


@YUAPI状态.handle()
async def YUAPI状态_handler(bot: Bot, event: Event):
    qq = str(event.self_id)
    url = "http://"+ip+":5187/api/SystemInfo/GetSystemInfo?apikey=Ayu&botqq=" + qq
    image_bytes = await fetch(url)
    await bot.send(event, MessageSegment.image(image_bytes))
    # await bot.send(event, message = "成功？")


@查直播.handle()
async def 查直播_handler(bot: Bot, event: Event):
    args = str(str(event.get_message()).strip().replace(
        "查直播", "").strip(prefix).strip(' '))
    url = "http://"+ip+":5187/api/BiliLive/BiliLiveCharts?sign="+args
    image_bytes = await fetch(url)
    await bot.send(event, MessageSegment.image(image_bytes))


@查场次.handle()
async def 查场次_handler(bot: Bot, event: Event):
    args = str(str(event.get_message()).strip().replace(
        "查场次", "").strip(prefix).strip(' '))
    url = "http://"+ip+":5187/api/BiliLive/BiliLiveList?sign="+args
    image_bytes = await fetch(url)
    await bot.send(event, MessageSegment.image(image_bytes))


@查成分.handle()
async def 查成分_handler(bot: Bot, event: Event):
    args = str(str(event.get_message()).strip().replace(
        "查成分", "").strip(prefix).strip(' '))
    url = "http://"+ip+":5187/api/Bili/BiliComponent?sign="+args
    image_bytes = await fetch(url)
    await bot.send(event, MessageSegment.image(image_bytes))


@查藏品.handle()
async def 查藏品_handler(bot: Bot, event: Event):
    args = str(str(event.get_message()).strip().replace(
        "查藏品", "").strip(prefix).strip(' '))
    url = "http://"+ip+":5187/api/Bili/BiliCollection?sign="+args
    image_bytes = await fetch(url)
    await bot.send(event, MessageSegment.image(image_bytes))


@查视频.handle()
async def 查视频_handler(bot: Bot, event: Event):
    args = str(str(event.get_message()).strip().replace(
        "查视频", "").strip(prefix).strip(' '))
    url = "http://"+ip+":5187/api/Bili/BiliSpacevideo?sign="+args
    image_bytes = await fetch(url)
    await bot.send(event, MessageSegment.image(image_bytes))


@查充电.handle()
async def 查充电_handler(bot: Bot, event: Event):
    args = str(str(event.get_message()).strip().replace(
        "查充电", "").strip(prefix).strip(' '))
    url = "http://"+ip+":5187/api/Bili/BiliBattery?sign="+args
    image_bytes = await fetch(url)
    await bot.send(event, MessageSegment.image(image_bytes))


@查房管.handle()
async def 查房管_handler(bot: Bot, event: Event):
    args = str(str(event.get_message()).strip().replace(
        "查房管", "").strip(prefix).strip(' '))
    url = "http://"+ip+":5187/api/Bili/BiliAnchor?sign="+args
    image_bytes = await fetch(url)
    await bot.send(event, MessageSegment.image(image_bytes))


@查关注.handle()
async def 查关注_handler(bot: Bot, event: Event):
    args = str(str(event.get_message()).strip().replace(
        "查关注", "").strip(prefix).strip(' '))
    url = "http://"+ip+":5187/api/Bili/BiliFollow?sign="+args
    image_bytes = await fetch(url)
    await bot.send(event, MessageSegment.image(image_bytes))


@查航海.handle()
async def 查航海_handler(bot: Bot, event: Event):
    args = str(str(event.get_message()).strip().replace(
        "查航海", "").strip(prefix).strip(' '))
    url = "http://"+ip+":5187/api/Bili/BiliCap?sign="+args
    image_bytes = await fetch(url)
    await bot.send(event, MessageSegment.image(image_bytes))


@查牌子.handle()
async def 查牌子_handler(bot: Bot, event: Event):
    args = str(str(event.get_message()).strip().replace(
        "查牌子", "").strip(prefix).strip(' '))
    url = "http://"+ip+":5187/api/Bili/BiliFanscard?type=1&sign="+args
    print(args)
    image_bytes = await fetch(url)
    # await bot.send(event, message = args)
    await bot.send(event, MessageSegment.image(image_bytes))


@查uid牌子.handle()
async def 查uid牌子_handler(bot: Bot, event: Event):
    args = str(str(event.get_message()).strip().replace(
        "查uid牌子", "").strip(prefix).strip(' '))
    url = "http://"+ip+":5187/api/Bili/BiliFanscard?type=0&sign="+args
    image_bytes = await fetch(url)
    await bot.send(event, MessageSegment.image(image_bytes))


@查装扮.handle()
async def 查装扮_handler(bot: Bot, event: Event):
    args = str(str(event.get_message()).strip().replace(
        "查装扮", "").strip(prefix).strip(' '))
    url = "http://"+ip+":5187/api/Bili/BiliDress?sign="+args
    image_bytes = await fetch(url)
    await bot.send(event, MessageSegment.image(image_bytes))


@查粉丝团.handle()
async def 查粉丝团_handler(bot: Bot, event: Event):
    args = str(str(event.get_message()).strip().replace(
        "查粉丝团", "").strip(prefix).strip(' '))
    url = "http://"+ip+":5187/api/Bili/BiliFan?sign="+args
    image_bytes = await fetch(url)
    await bot.send(event, MessageSegment.image(image_bytes))


@查房间状态.handle()
async def 查房间状态_handler(bot: Bot, event: Event):
    args = str(str(event.get_message()).strip().replace(
        "查房间状态", "").strip(prefix).strip(' '))
    url = "http://"+ip+":5187/api/Bili/BiliRoomState?sign="+args
    image_bytes = await fetch(url)
    await bot.send(event, MessageSegment.image(image_bytes))


@直播列表.handle()
async def 直播列表_handler(bot: Bot, event: Event):
    url = "http://"+ip+":5187/api/BiliLive/GetLiveState"
    image_bytes = await fetch(url)
    await bot.send(event, MessageSegment.image(image_bytes))


@YUAPI帮助.handle()
async def YUAPI帮助_handler(bot: Bot, event: Event):
    url = "http://"+ip+":5187/api/Menu/MenuList"
    image_bytes = await fetch(url)
    await bot.send(event, MessageSegment.image(image_bytes))
