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