import asyncio


class Remer:
    def __init__(self, client):
        self.client = client

    async def get_admins(self, group_guid):
        """
        دریافت لیست ادمین‌های گروه
        """
        result = await self.client.get_group_admin_members(
            group_guid=group_guid
        )

        admins = set()

        for member in getattr(result, "in_chat_members", []):
            guid = getattr(member, "member_guid", None)

            if guid:
                admins.add(guid)

        return admins

    async def check_and_remove(self, group_guid, member_guid):
        """
        بررسی کاربر و اخراج در صورت ادمین نبودن
        """

        try:
            admins = await self.get_admins(group_guid)

            # کاربر ادمین است
            if member_guid in admins:
                print(f"✅ {member_guid} is admin")
                return

            print(f"⚠️ {member_guid} is not admin")
            print("⏳ Waiting 3 seconds...")

            await asyncio.sleep(3)

            # دوباره بررسی می‌کنیم؛
            # شاید در این فاصله مدیرش کرده باشند.
            admins = await self.get_admins(group_guid)

            if member_guid in admins:
                print(f"✅ {member_guid} became admin")
                return

            print(f"🚫 Removing {member_guid}")

            await self.client.ban_group_member(
                group_guid=group_guid,
                member_guid=member_guid
            )

            print(f"✅ {member_guid} removed")

        except Exception as e:
            print(f"❌ Error: {e}")
