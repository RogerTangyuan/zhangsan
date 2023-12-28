import pymysql

db = pymysql.connect(host="192.168.3.12",user="",password="",db="mysql")
cur = db.cursor()
try:
    cur.execute("select * from t_class;")
    res = cur.fetchall()
    print(res)
except:
    pritn("sql语句错误")