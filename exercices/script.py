#!/usr/bin/python3
import cgitb

import pymysql
import requests

pymysql.install_as_MySQLdb()

cgitb.enable()
print("Content-Type: text/plain")
print()
instance = "http://169.254.169.254/latest/meta-data/instance-id"


def instanceId(url):
    instance_id = requests.get(url)
    return instance_id.content


print(instanceId(instance).decode("utf-8"))
try:
    db = pymysql.connect(host="benmysqlinstance.c7p9s8bjlzfz.eu-west-1.rds.amazonaws.com",
                         # your host, usually localhost
                         user="Mythridor",  # your username
                         passwd="3141592653589Rr",  # your password
                         db="test")  # name of the data base

    cur = db.cursor()
    cur.execute("SELECT * FROM instances")
    ctr = 0
    inserted = False
    for row in cur.fetchall():
        print(row)
        if row[1] == instanceId(instance).decode("utf-8"):
            response = cur.execute("UPDATE instances SET ctr = ctr + 1 WHERE id = %s", row[0])
            inserted = True
    if inserted == False:
        response = cur.execute("INSERT INTO instances (instance_id, ctr) VALUE (%s, %s)",
                               (instanceId(instance).decode("utf-8"), ctr))
        print(response)
    db.commit()
    db.close()
except:
    print("error")
