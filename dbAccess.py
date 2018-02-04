# Find entries from sqlite db in python

import sqlite3

def queryTableByKeywords(conn, keyword1, keyword2, table):
	cur = conn.cursor()
	query = "SELECT A.argument FROM (select *  from " + table + " where argument like '%" + keyword1 + "%') A INNER JOIN (SELECT  * from " + table + " where argument like '%" + keyword2 + "%') B on A.id = B.id;"
	cur.execute(query)
	rows = cur.fetchall()
	results = []
	for row in rows:
		row = row[0].encode('utf-8')
		#print row
		results.append(row)
	return results

def queryTableByKeyword(conn, keyword, table):
	cur = conn.cursor()
	query = "select argument from " + table + " where argument like '%" + keyword + "%'"
	cur.execute(query)
	rows = cur.fetchall()
	results = []
	for row in rows:
		row = row[0].encode('utf-8')
		results.append(row)
	return results

def getAnyString(conn, table):
	query = "SELECT argument FROM " + table + " ORDER BY RANDOM() LIMIT 1;"
	cur = conn.cursor()
	cur.execute(query)
	row = cur.fetchone()[0]
	row = row.encode('utf-8')
	return row

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

def mainTest():
	conn = create_connection("ShouldWeGoVegan.db")
	getAnyString(conn, "Against")
mainTest()
