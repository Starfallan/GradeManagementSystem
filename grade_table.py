# 创建 grade_table 并从excel中取值插入数据库
# 定义一些操作

import pymysql
import xlrd
import showUI


# Connect to the database
class table:
    conn_grade = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="123456",
        db="student_db",
        charset="utf8mb4",
    )

    #   def insert(self):

    def show(self):
        with table.conn_grade.cursor() as cursor:
            cursor.execute("select stu_id, stu_name, gpa from grade_table")
            b = cursor.fetchall()  # 获取单条数据
            for i in [*b]:
                # print('%s %s' % (i[0], i[1]))
                print(i)

    def init(self):
        LoadGradeTable(table)

    def deleteall(self):
        try:
            with table.conn_grade.cursor() as cursor:
                delete_sql = "delete from grade_table"
                cursor.execute(delete_sql)
        except:
            table.rollback(table)
        finally:
            table.commit(table)

    def commit(self):
        table.conn_grade.commit()

    def close(self):
        table.conn_grade.close()

    def rollback(self):
        table.conn_grade.rollback()


# 以下是对单条数据进行操作的函数，没有定义在类内部
# Read data from excel and put them into grade_table
def LoadGradeTable(table):
    filepath = "1112.xls"
    workbook = xlrd.open_workbook(filepath)
    sheet = workbook.sheet_by_index(0)

    for row in range(1, sheet.nrows):
        try:
            with table.conn_grade.cursor() as cursor:
                insert_sql = "insert into grade_table (stu_id, stu_name, math, english, software, gpa) \
                values (%s, %s, %s, %s, %s, %s)"
                cursor.execute(
                    insert_sql,
                    (
                        sheet.row(row)[0].value,
                        sheet.row(row)[1].value,
                        int(sheet.row(row)[2].value),
                        int(sheet.row(row)[3].value),
                        int(sheet.row(row)[4].value),
                        float(sheet.row(row)[5].value),
                    ),
                )

        except:
            print("Error")
            table.rollback(table)
        finally:
            table.commit(table)


# 通过 stu_id 删除数据
def Delete(table, stu_id):
    try:
        with table.conn_grade.cursor() as cursor:
            delete_sql = "delete from grade_table where stu_id = %s"
            cursor.execute(delete_sql, (stu_id))
    except:
        table.rollback(table)
    finally:
        table.commit(table)


# 插入学生成绩
# This function inserts a new row into the grade_table with the provided student information.
# Returns True if the insertion was successful, False otherwise.
def Insert(stu_id, stu_name, math, english, software, gpa):
    try:
        with table.conn_grade.cursor() as cursor:
            insert_sql = "insert into grade_table (stu_id, stu_name, math,english,software,gpa) \
            values (%s, %s, %s, %s, %s, %s)"
            cursor.execute(
                insert_sql,
                (
                    stu_id,
                    stu_name,
                    math,
                    english,
                    software,
                    gpa,
                ),
            )
    except:
        print("插入失败")  # Print error message if insertion fails
        table.rollback(table)  # Rollback transaction if insertion fails
        return False
    finally:
        table.commit(table)  # Commit transaction if insertion is successful or failed
        return True


# 查找学生成绩，返回学生成绩字典
def Select(table, ID):
    with table.conn_grade.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
        select_sql = "select * from grade_table where stu_id = %s"
        cursor.execute(select_sql, (ID))
        b = cursor.fetchall()  # 获取单条数据
    return b


# 单科成绩查询
def SelectSingle(g):
    if g == 1:
        with table.conn_grade.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
            sql = "select stu_id, stu_name, math from grade_table"
            cursor.execute(sql)
            b = cursor.fetchall()
        return b
    elif g == 2:
        with table.conn_grade.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
            sql = "select stu_id, stu_name, english from grade_table"
            cursor.execute(sql)
            b = cursor.fetchall()
        return b
    elif g == 3:
        with table.conn_grade.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
            sql = "select stu_id, stu_name, software from grade_table"
            cursor.execute(sql)
            b = cursor.fetchall()
        return b


# 修改学生信息
def Update(stu_id, stu_name, math, english, software, gpa):
    try:
        with table.conn_grade.cursor() as cursor:
            insert_sql = "update grade_table set stu_name = %s, math = %s, english = %s, software = %s, gpa = %s \
            where stu_id = %s"
            cursor.execute(
                insert_sql,
                (
                    stu_name,
                    math,
                    english,
                    software,
                    gpa,
                    stu_id,
                ),
            )
    except:
        table.rollback(table)
    finally:
        table.commit(table)


# 是否存在学号为 stu_id 的学生
def Exist(stu_id):
    with table.conn_grade.cursor() as cursor:
        select_sql = "select * from grade_table where stu_id = %s"
        cursor.execute(select_sql, (stu_id))
        b = cursor.fetchall()
    print(b)
    if b == ():
        return False
    else:
        return True
