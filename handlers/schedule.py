import datetime

from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.date import DateTrigger

from database.bot_db import sql_command_all
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
from config import bot, ADMINS




async def go_to_sleep(bot: Bot):
    user_ids = await sql_command_all()
    for user_id in user_ids:
        await bot.send_message(user_id[0], "Иди спать")


async def wake_up(bot: Bot):
    video = open('media/videoss.mp4', "rb")
    await bot.send_video(ADMINS[0], video=video)

async def send_message_date(bot: Bot):
    await bot.send_message(ADMINS[0], "DATE TRIGGER!")

async def set_scheduler():
    scheduler = AsyncIOScheduler(timezone='US/Central')
    # scheduler.add_job(
    #     go_to_sleep,
    #     trigger=CronTrigger(
    #         hour=datetime.datetime.now().hour,
    #         minute=datetime.datetime.now().minute + 1,
    #         start_date=datetime.datetime.now()
    #     ),
    #     kwargs={"bot": bot}
    # )
    # scheduler.add_job(
    #     wake_up,
    #     trigger=IntervalTrigger(
    #         seconds=60
    #     ),
    #     kwargs={"bot": bot},
    # )
    # scheduler.start()


    # scheduler.add_job(
    #     wake_up,
    #     trigger=DateTrigger(
    #         # run_date=datetime.datetime(year=2023, month=6, hour=22, minute=24)
    #         run_date=datetime.datetime.now() + datetime.timedelta(minutes=1)
    #     ),
    #     kwargs={"bot": bot},
    # )
    # scheduler.start()