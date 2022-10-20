import sqlite3  # import sqlite
conn = sqlite3.connect('spotify_artist_data')  # connecting our dataset to python
print("Opened database successfully")  # print this when database is opened successfully

# cur = conn.cursor()  # creating table for our data spotify
# cur.execute(''' CREATE TABLE spotify_artists
# (  ID INT PRIMARY KEY           NOT NULL,
#     ARTIST_NAME      TEXT        NOT NULL,
#     LEAD_STREAMS     INT         NOT NULL,
#     FEAT             INT         NOT NULL,
#     TRACKS           INT         NOT NULL,
#     STREAM_100       INT         NOT NULL);''')
# print("Table created successfully")

# inserting the spotify data from the Excel spreadsheet
'''
conn.execute("INSERT INTO spotify_artists (ID,ARTIST_NAME,LEAD_STREAMS,FEAT,TRACKS,STREAM_100) \
   VALUES (1, 'Drake', 50162292808, 19246513666, 262, 130 )");
conn.execute("INSERT INTO spotify_artists (ID,ARTIST_NAME,LEAD_STREAMS,FEAT,TRACKS,STREAM_100) \
   VALUES (2, 'Bad Bunny', 44369032140, 5391990975, 163, 118 )");
conn.execute("INSERT INTO spotify_artists (ID,ARTIST_NAME,LEAD_STREAMS,FEAT,TRACKS,STREAM_100) \
   VALUES (3, 'Ed Sheeran', 38153682361, 2791278201, 240, 62 )");
conn.execute("INSERT INTO spotify_artists (ID,ARTIST_NAME,LEAD_STREAMS,FEAT,TRACKS,STREAM_100) \
  VALUES (4, 'The Weekend', 34767779741, 4288903657, 186, 72 )");
conn.execute("INSERT INTO spotify_artists (ID,ARTIST_NAME,LEAD_STREAMS,FEAT,TRACKS,STREAM_100) \
 VALUES (5, 'Taylor Swift', 32596728109, 424053296, 323, 96 )");
conn.execute("INSERT INTO spotify_artists (ID,ARTIST_NAME,LEAD_STREAMS,FEAT,TRACKS,STREAM_100) \
    VALUES (6, 'Justin Bieber', 32465998885, 10816202075, 225, 58 )");
conn.commit()
print("Records created successfully");
conn.close() '''


cursor = conn.execute("SELECT * FROM spotify_artists;")  # selecting every column from the spotify dataset
for row in cursor:
    print("ID =", row[0])
    print("ARTIST_NAME = ", row[1])
    print("LEAD_STREAMS", row[2])
    print("FEAT", row[3])
    print("TRACKS", row[4])
    print("STREAMS", row[5], "\n")

print("Operation done successfully")
conn.close()
