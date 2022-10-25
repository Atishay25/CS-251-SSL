import sqlite3
import csv

connection = sqlite3.connect('ipl.db')
cursor = connection.cursor()

connection.execute('''CREATE TABLE POINTS_TABLE(team_id INT PRIMARY KEY, team_name TEXT, points INT DEFAULT 0, nrr REAL DEFAULT 0);''')
connection.execute("INSERT INTO POINTS_TABLE(team_id, team_name) SELECT team_id, team_name FROM TEAM;")
#connection.execute('''UPDATE POINTS_TABLE SET points = SUM(CASE
#                                                            WHEN t.team_id = m.match_winner
#                                                            THEN 2
#                                                            ELSE 0
#                                                            END)
#                                                    FROM MATCH m, TEAM t
#                                                    WHERE team_id = 12;
#                                                        ''')
connection.execute('''UPDATE POINTS_TABLE 
                    SET points = (
                        SELECT SUM(CASE
                                        WHEN POINTS_TABLE.team_id = MATCH.match_winner
                                        THEN 2
                                        ELSE 0
                                        END)
                        FROM MATCH
                        WHERE MATCH.team1 = POINTS_TABLE.team_id OR MATCH.team2 = POINTS_TABLE.team_id
                        GROUP BY POINTS_TABLE.team_id
                    );''')
connection.commit()
connection.close()


