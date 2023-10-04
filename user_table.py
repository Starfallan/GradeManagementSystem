# 创建 user_table 并从excel中取值插入数据库
# 定义一些操作

import pymysql
import xlrd

conn_user = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    db="student_db",
    charset="utf8mb4",
)


def commit():
    conn_user.commit()


def close():
    conn_user.close()


def rollback():
    conn_user.rollback()


def ExistUser(name, password):
    with conn_user.cursor() as cursor:
        exist_sql = "select * from user_table where user_id = %s and user_password = %s"
        cursor.execute(exist_sql, (name, password))
    b = cursor.fetchall()
    print(b)
    if b == ():
        return False
    else:
        return True


# 修改密码
def Update(ID, pw):
    try:
        with conn_user.cursor() as cursor:
            update_sql = "update user_table set user_password = %s where user_id = %s"
            cursor.execute(update_sql, (pw, ID))
    except:
        rollback()
        return False
    finally:
        commit()
        return True


"""
create table user_table(
user_id char(12) primary key,
user_password varchar(12),
user_name varchar(6));
"""
