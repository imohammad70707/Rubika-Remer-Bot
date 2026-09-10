import asyncio
from maxrubika import Bot


async def main():
    bot = Bot()

    print("در حال دریافت Update خام...")
    print("یک کاربر را وارد گروه کن.\n")

    offset = None

    while True:
        result = await bot.get_updates(offset_id=offset, limit=100)

        print("\n========== RAW RESPONSE ==========")
        print(result)
        print("==================================")

        # تلاش برای پیدا کردن offset بعدی
        if isinstance(result, dict):
            offset = result.get("next_offset_id") or offset

        await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())
