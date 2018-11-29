import librosa
import numpy as np
import sqlite3

db_conn = sqlite3.connect("data.db")
db_cursor = db_conn.cursor()


names = ['blues','classical','country','disco','hiphop','jazz','metal','pop','reggae','rock']


for name in names:

    for i in range(10):
        song_name = name + '.' + '0000' + str(i) + '.au'
        y,sr=librosa.load("genres\\"+name+'\\'+song_name)

        med1 = np.median(librosa.feature.zero_crossing_rate(y))
        db_cursor.execute('''UPDATE songs SET med_zero_crs_rate=? WHERE song_name=?''',(med1,song_name))
        db_conn.commit()

        med2 = np.median(librosa.feature.spectral_centroid(y,sr))
        db_cursor.execute('''UPDATE songs SET med_spec_centroid=? WHERE song_name=?''',(med2,song_name))
        db_conn.commit()

        med3 = np.median(librosa.feature.spectral_bandwidth(y,sr))
        db_cursor.execute('''UPDATE songs SET med_spec_bandwidth=? WHERE song_name=?''',(med3,song_name))
        db_conn.commit()

        med4 = np.median(librosa.feature.spectral_contrast(y,sr))
        db_cursor.execute('''UPDATE songs SET med_spec_contrast=? WHERE song_name=?''',(med4,song_name))
        db_conn.commit()

        med5 = np.median(librosa.feature.spectral_rolloff(y,sr))
        db_cursor.execute('''UPDATE songs SET med_spec_rolloff=? WHERE song_name=?''',(med5,song_name))
        db_conn.commit()


        med6 = np.median(librosa.feature.rmse(y))
        db_cursor.execute('''UPDATE songs SET med_rmse=? WHERE song_name=?''',(float(med6),song_name))
        db_conn.commit()


    for i in range(10,100):
        song_name = name + '.' + '000' + str(i) + '.au'
        y,sr=librosa.load("genres\\"+name+"\\"+song_name)

        med1 = np.median(librosa.feature.zero_crossing_rate(y))
        db_cursor.execute('''UPDATE songs SET med_zero_crs_rate=? WHERE song_name=?''',(med1,song_name))
        db_conn.commit()

        med2 = np.median(librosa.feature.spectral_centroid(y,sr))
        db_cursor.execute('''UPDATE songs SET med_spec_centroid=? WHERE song_name=?''',(med2,song_name))
        db_conn.commit()

        med3 = np.median(librosa.feature.spectral_bandwidth(y,sr))
        db_cursor.execute('''UPDATE songs SET med_spec_bandwidth=? WHERE song_name=?''',(med3,song_name))
        db_conn.commit()

        med4 = np.median(librosa.feature.spectral_contrast(y,sr))
        db_cursor.execute('''UPDATE songs SET med_spec_contrast=? WHERE song_name=?''',(med4,song_name))
        db_conn.commit()

        med5 = np.median(librosa.feature.spectral_rolloff(y,sr))
        db_cursor.execute('''UPDATE songs SET med_spec_rolloff=? WHERE song_name=?''',(med5,song_name))
        db_conn.commit()

        med6 = np.median(librosa.feature.rmse(y))
        db_cursor.execute('''UPDATE songs SET med_rmse=? WHERE song_name=?''',(float(med6),song_name))
        db_conn.commit()




db_conn.close()
