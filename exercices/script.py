#!/usr/bin/python3
import cgitb
import collections
import json

import pymysql
import requests

pymysql.install_as_MySQLdb()

cgitb.enable()
print("Content-Type: text/html; charset=utf-8")
print()
instance = "http://169.254.169.254/latest/meta-data/instance-id"


def instanceId(url):
    instance_id = requests.get(url)
    return instance_id.content

try:
    writedb = pymysql.connect(host="benmysqlinstance.c7p9s8bjlzfz.eu-west-1.rds.amazonaws.com",
                              user="Mythridor",
                              passwd="3141592653589Rr",
                              db="test")

    readdb = pymysql.connect(host="benmysqlinstancereplica.c7p9s8bjlzfz.eu-west-1.rds.amazonaws.com",
                             user="Mythridor",
                             passwd="3141592653589Rr",
                             db="test")
    cur = readdb.cursor()
    writecur = writedb.cursor()
    ctr = 0
    inserted = False
    cur.execute("SELECT * FROM instances")
    for row in cur.fetchall():
        if row[1] == instanceId(instance).decode("utf-8"):
            response = writecur.execute("UPDATE instances SET ctr = ctr + 1 WHERE id = %s", row[0])
            inserted = True
    if inserted == False:
        response = writecur.execute("INSERT INTO instances (instance_id, ctr) VALUE (%s, %s)",
                                    (instanceId(instance).decode("utf-8"), ctr))

    objects_list = []
    cur.execute("SELECT * FROM instances")
    for row in cur.fetchall():
        d = collections.OrderedDict()
        d['instance_id'] = row[1]
        d['ctr'] = row[2]
        objects_list.append(d)
    j = json.dumps(objects_list)
    print("<br />")
    print(j)
    writedb.commit()
finally:
    writedb.close()
    readdb.close()
