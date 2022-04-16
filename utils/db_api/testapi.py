import asyncio

from utils.db_api.postgresql import Database


async def test_2():
    db = Database()
    await db.create()

    print("Users jadvalini yaratamiz...")
    await db.create_table_users()
    print("Yaratildi")

    print("Foydalanuchilarini qoshish")

    await db.add_user("Anver", "Mamadaliyo", 1233454356)
    await db.add_user("Mexel", "aliksandriov", 1234452345)
    await db.add_user("1", "1", 12334324)
    print("Qoshildi")

    users = await db.select_all_users()
    print(f"Barcha userlar: {users}")

    user = await db.select_user(id=2)
    print(f"User : {user}")


asyncio.run(test_2())
