# import pymysql
# try:
#     connection = pymysql.connect(host='37.140.192.80',
#                                  user='u0823922_codolo1',
#                                  password='codologia1',
#                                  cursorclass=pymysql.cursors.DictCursor,
#                                  database="u0823922_test")
#     print("successfully...")
# except Exception as ex:
#     print(ex)
#
# def Register_Finish(encoded_jwt, name, surname, last_name):
#     try:
#         with connection.cursor() as cursor:
#             insert_query = f"INSERT INTO `users` (`encoded_jwt`, `name`, `surname`, `last_name`) " \
#                         f"VALUES ({encoded_jwt}, {name}, {surname}, {last_name})"
#             cursor.execute(insert_query)
#             connection.commit()
#             print("1")
#     except Exception as ex:
#         print(ex)