#! /usr/bin/python
# -*- coding: utf-8 -*-
import  os
import  time
import datetime
db_host = '127.0.0.1'
db_user = 'root'
db_password = '123456'
db_port = '3306'
db_database = 'mysql'
backup_dir = '/data/'
datetime = time.strftime('%Y%m%d-%H%M%S')
today_backup_dir = backup_dir + datetime
print("creating backup folder")
if not os.path.exists(today_backup_dir):
    os.mkdir(today_backup_dir)
#print("checking for databases names file")
if os.path.exists(db_database):
    file1 = open(db_database)
    mult = 1
    print("dataabase found")
    print("starting backup database"+ db_database)
else:
    print("database not found ...")
    print("starting backup database" + db_database)
    mult = 0
if mult:
    in_file = open(db_database, "r")
    flength = len(in_file.readline())
    in_file.close()
    p = 1
    dbfile = open(db_database, "r")
    while p <= flength:
        db = dbfile.readline()
        db = db[:-1]
        dumpcmd = "mysqldump -u" + db_user + " -p" + db_password + " -h" + db_host + " " + db_database + " > " + today_backup_dir + "/" + db_database + ".sql"
        print(dumpcmd)
        os.system(dumpcmd)
        p = p + 1
        dbfile.close()
else:
    db = db_database
    dumpcmd = "mysqldump -u" + db_user + " -p" + db_password + " -h" + db_host + " " + db_database + " > " + today_backup_dir + "/" + db_database + ".sql"
    os.system(dumpcmd)
    print("over")
