import sqlite3
import csv

connection = sqlite3.connect('ipl.db')
cursor = connection.cursor()

connection.execute('''CREATE TABLE POINTS_TABLE(team_id INT PRIMARY KEY, team_name TEXT, points INT DEFAULT 0, nrr REAL DEFAULT 0);''')
connection.execute("INSERT INTO POINTS_TABLE(team_id, team_name) SELECT team_id, team_name FROM TEAM;")

#connection.execute('''UPDATE POINTS_TABLE 
#                    SET points = (
#                        SELECT SUM(CASE
#                                        WHEN MATCH.match_winner = 'NULL' AND POINTS_TABLE.team_id = MATCH.team1 
#                                        THEN 1
#                                        WHEN MATCH.win_type = 'Tie' AND POINTS_TABLE.team_id = MATCH.team1
#                                        THEN 1
#                                        WHEN POINTS_TABLE.team_id = MATCH.match_winner
#                                        THEN 2
#                                        ELSE 0
#                                        END)
#                        FROM MATCH
#                    );''')

# CORRECT EXCPET NO MATCH CASE

#tablepoints = connection.execute('''UPDATE POINTS_TABLE 
#                   SET points = (
#                       SELECT SUM(CASE
#                                       WHEN POINTS_TABLE.team_id = MATCH.match_winner AND MATCH.win_type != 'Tie'
#                                       THEN 2
#                                       WHEN POINTS_TABLE.team_id != MATCH.match_winner AND MATCH.match_winner != 'NULL' AND MATCH.win_type != 'Tie'
#                                       THEN 0
#                                       ELSE 1
#                                       END)
#                       FROM MATCH
#                       WHERE MATCH.team1 = POINTS_TABLE.team_id OR MATCH.team2 = POINTS_TABLE.team_id
#                   );''')
tablepoints = connection.execute('''UPDATE POINTS_TABLE 
                   SET points = (
                       SELECT SUM(CASE
                                    WHEN POINTS_TABLE.team_id != MATCH.team1 AND POINTS_TABLE.team_id != MATCH.team2
                                    THEN 0
                                    WHEN MATCH.team1 = POINTS_TABLE.team_id OR MATCH.team2 = POINTS_TABLE.team_id
                                    THEN
                                      CASE
                                       WHEN POINTS_TABLE.team_id = MATCH.match_winner AND MATCH.win_type != 'Tie'
                                       THEN 2
                                       WHEN POINTS_TABLE.team_id != MATCH.match_winner AND MATCH.match_winner != 'NULL' AND MATCH.win_type != 'Tie'
                                       THEN 0
                                       ELSE 1
                                       END
                                    END)
                       FROM MATCH
                   );''')
#ptTable = connection.execute("SELECT * from POINTS_TABLE").fetchall()
#matches = connection.execute("SELECT * FROM MATCH").fetchall()
#for eachmatch in matches:
connection.execute('''UPDATE POINTS_TABLE SET nrr = (
                            SELECT ROUND(SUM(CASE
                                WHEN POINTS_TABLE.team_id != MATCH.team1 AND POINTS_TABLE.team_id != MATCH.team2
                                THEN 0.00
                                WHEN MATCH.team1 = POINTS_TABLE.team_id OR MATCH.team2 = POINTS_TABLE.team_id
                                THEN
                                CASE
                                WHEN POINTS_TABLE.team_id = MATCH.match_winner AND MATCH.win_type = 'runs'
                                THEN (0.05)*(MATCH.win_margin)
                                WHEN POINTS_TABLE.team_id = MATCH.match_winner AND MATCH.win_type = 'wickets'
                                THEN (0.1)*(MATCH.win_margin)   
                                WHEN POINTS_TABLE.team_id != MATCH.match_winner AND MATCH.win_type = 'runs'
                                THEN (-0.05)*(MATCH.win_margin)
                                WHEN POINTS_TABLE.team_id != MATCH.match_winner AND MATCH.win_type = 'wickets'
                                THEN (-0.1)*(MATCH.win_margin)   
                                ELSE 0.00
                                END 
                            END                           
                            ),2)
                            FROM MATCH
                            );''')
pointscol = cursor.execute("SELECT * from POINTS_TABLE ORDER BY points DESC, nrr DESC").fetchall()

for i in pointscol:
    Points_Table = str(i[0]) + "," + i[1] + ',' + str(i[2]) + ',' + str('%.2f' % i[3])
    print(Points_Table)
#connection.execute('''UPDATE POINTS_TABLE 
#                    SET points = (
#                                SUM(
#                                    CASE 
#                                    WHEN MATCH.team1 != POINTS_TABLE.team_id AND MATCH.team2 = POINTS_TABLE.team_id
#                                    THEN
#                                        CASE
#                                            WHEN POINTS_TABLE.team_id = MATCH.match_winner AND MATCH.win_type != 'Tie'
#                                            THEN 2
#                                            WHEN POINTS_TABLE.team_id != MATCH.match_winner AND MATCH.match_winner != 'NULL' AND MATCH.win_type != 'Tie'
#                                            THEN 0
#                                            ELSE 1
#                                        END
#                                    ELSE 0
#                                    END)
#                                FROM MATCH
#                    );''')

connection.commit()
connection.close()


