import pymysql
try:
    connection = pymysql.connect(host='37.140.192.80',
                                 user='u0823922_hakaton',
                                 password='tB4nG4fN9sqG1vJ9',
                                 cursorclass=pymysql.cursors.DictCursor,
                                 database="u0823922_hakaton")
    print("successfully...")
except Exception as ex:
    print(ex)

def Register_Finish(encoded_jwt, name, surname, last_name, sex, born):
    try:
        with connection.cursor() as cursor:
            insert_query = f"INSERT INTO `users` (`jwt`, `name`, `surname`, `last_name`, `sex`, `born`) " \
                        f"VALUES ('{encoded_jwt}', '{name}', '{surname}', '{last_name}', '{sex}', '{born}')"
            cursor.execute(insert_query)
            connection.commit()
    except Exception as ex:
        print(1)
        print(ex)

def Admin_Register_Finish(login):
    try:
        with connection.cursor() as cursor:
            zero = ""
            insert_query = f"INSERT INTO `admin_login` (`jwt_token`, `login`) " \
                        f"VALUES ('{zero}', '{login}')"
            cursor.execute(insert_query)
            connection.commit()
    except Exception as ex:
        print(1)
        print(ex)

def Point_Add(point):
    try:
        with connection.cursor() as cursor:
            insert_query = f"INSERT INTO `points` (`Adress`, `tables`) " \
                        f"VALUES ('{point}', '0, 0, 0, 0')"
            cursor.execute(insert_query)
            connection.commit()
    except Exception as ex:
        print(1)
        print(ex)

def Point_Remove(point):
    try:
        with connection.cursor() as cursor:
            remove_query = f"DELETE FROM `points`" \
                           f"WHERE `Adress` = '{point}'"
            cursor.execute(remove_query)
            connection.commit()
    except Exception as ex:
        print(1)
        print(ex)
def User_Remove(user):
    try:
        with connection.cursor() as cursor:
            remove_query = f"DELETE FROM `admin_login`" \
                        f"WHERE `login` = '{user}'"
            cursor.execute(remove_query)
            connection.commit()
    except Exception as ex:
        print(1)
        print(ex)

def Dish_Add(dish_name, dish_price, dish_link):
    try:
        with connection.cursor() as cursor:
            insert_query = f"INSERT INTO `menu` (`dish`, `price`, `image`) " \
                        f"VALUES ('{dish_name}', '{dish_price}', {dish_link})"
            cursor.execute(insert_query)
            connection.commit()
    except Exception as ex:
        print(1)
        print(ex)

def Dish_Remove(dish):
    try:
        with connection.cursor() as cursor:
            remove_query = f"DELETE FROM `menu`" \
                           f"WHERE `dish` = '{dish}'"
            cursor.execute(remove_query)
            connection.commit()
    except Exception as ex:
        print(1)
        print(ex)
def Image_Switch(dish):
    try:
        with connection.cursor() as cursor:
            find_query = f"SELECT * FROM `menu` WHERE `dish` = '{dish}'"
            cursor.execute(find_query)
            return cursor.fetchall()[0]["image"]
    except Exception as ex:
        print(ex, 1)