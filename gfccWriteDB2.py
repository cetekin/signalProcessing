import numpy as np
import sqlite3
import essentia
import essentia.standard as es

db_conn = sqlite3.connect("data.db")
db_cursor = db_conn.cursor()


names = ['blues','classical','country','disco','hiphop','jazz','metal','pop','reggae','rock']


for name in names:

    for i in range(10):
        song_name = name + '.' + '0000' + str(i) + '.wav'
        print(song_name)
        # Compute all features, aggregate only 'mean' and 'stdev' statistics for all low-level, rhythm and tonal frame features
        features, features_frames = es.MusicExtractor(lowlevelStats=['mean', 'stdev'],
                                                      rhythmStats=['mean', 'stdev'],
                                                      tonalStats=['mean', 'stdev'])("genres_new/"+name+"/"+song_name)




        for i in range(1,14):
            sql = "UPDATE songs SET avg_gfcc_" + str(i) + "=? WHERE song_name=?"
            db_cursor.execute(sql,(float(features["lowlevel.gfcc.mean"][i-1]),song_name))
            db_conn.commit()







    for i in range(10,100):
        song_name = name + '.' + '000' + str(i) + '.wav'
        print(song_name)
        # Compute all features, aggregate only 'mean' and 'stdev' statistics for all low-level, rhythm and tonal frame features
        features, features_frames = es.MusicExtractor(lowlevelStats=['mean', 'stdev'],
                                                      rhythmStats=['mean', 'stdev'],
                                                      tonalStats=['mean', 'stdev'])("genres_new/"+name+"/"+song_name)



        for i in range(1,14):
            sql = "UPDATE songs SET avg_gfcc_" + str(i) + "=? WHERE song_name=?"
            db_cursor.execute(sql,(float(features["lowlevel.gfcc.mean"][i-1]),song_name))
            db_conn.commit()




db_conn.close()
