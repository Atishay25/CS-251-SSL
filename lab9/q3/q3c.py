import sqlite3
import csv

connection = sqlite3.connect('ipl.db')
cursor = connection.cursor()
runs_scored = cursor.execute('''SELECT player.player_id, player.player_name, SUM(balls.runs_scored)
                                FROM PLAYER player, BALL_BY_BALL balls
                                WHERE balls.striker = player.player_id
                                GROUP BY player.player_id
                                ORDER BY SUM(balls.runs_scored) DESC;''').fetchall()
print(runs_scored[:20])
connection.commit()
connection.close()