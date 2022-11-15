import sqlite3
import csv

connection = sqlite3.connect('ipl.db')
cursor = connection.cursor()

match_runs = cursor.execute('''SELECT d.venue_name, ROUND(1.0*(SUM(e.runs_scored)+SUM(e.extra_runs))/COUNT(DISTINCT d.match_id),2)
                FROM BALL_BY_BALL e, MATCH d
                WHERE e.match_id = d.match_id
                GROUP BY d.venue_name
                ORDER BY (SUM(e.runs_scored)+SUM(e.extra_runs))/COUNT(DISTINCT d.match_id) DESC;''').fetchall()

for i in match_runs:
    avg = (i[0]+','+str('%.2f' % i[1]))
    print(avg)
    
connection.commit()
connection.close()
