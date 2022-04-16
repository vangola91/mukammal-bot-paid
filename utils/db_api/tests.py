from utils.db_api.sqllite import Databaes


def test():
    db = Databaes(path_to_db="test.db")
    db.create_table_users()
    db.add_user(11, "One", "email", "123435")
    db.add_user(12, "olmaim", "aliks@yan.com","12312312")

    users = db.select_all_users()
    print(f"Barcha userlar :{users}")


    user = db.select_users(Name="olmaim", id=12)
    print(f"Bitta user : {user}")



test()