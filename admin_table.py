# 创建 admin_table
# 定义一些操作

import pymysql

conn_admin = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    db="student_db",
    charset="utf8mb4",
)


def commit():
    conn_admin.commit()


def close():
    conn_admin.close()


def rollback():
    conn_admin.rollback()


# 创建管理员账号
def InsertAdmin(name, password):
    try:
        with conn_admin.cursor() as cursor:
            insert_sql = (
                "insert into admin_table (admin_id, admin_password) value (%s, %s)"
            )
            cursor.execute(insert_sql, (name, password))
    except:
        rollback()
    finally:
        commit()


# 查询是否存在该管理员，登陆时调用
def ExistAdmin(name, password):
    with conn_admin.cursor() as cursor:
        exist_sql = (
            "select * from admin_table where admin_id = %s and admin_password = %s"
        )
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
        with conn_admin.cursor() as cursor:
            update_sql = (
                "update admin_table set admin_password = %s where admin_id = %s"
            )
            cursor.execute(update_sql, (pw, ID))
    except:
        rollback()
        return False
    finally:
        commit()
        return True
