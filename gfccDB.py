import numpy as np
import sqlite3
import essentia.streaming as ess
import essentia

db_conn = sqlite3.connect("data.db")
db_cursor = db_conn.cursor()


names = ['blues','classical','country','disco','hiphop','jazz','metal','pop','reggae','rock']


for name in names:

    for i in range(10):
        song_name = name + '.' + '0000' + str(i) + '.au'
        print(song_name)
        loader = ess.MonoLoader(filename="genres/"+name+"/"+song_name)
        framecutter = ess.FrameCutter(frameSize=4096, hopSize=2048, silentFrames='noise')
        windowing = ess.Windowing(type='blackmanharris62')
        spectrum = ess.Spectrum()
        spectralpeaks = ess.SpectralPeaks(orderBy='magnitude',
                                          magnitudeThreshold=0.00001,
                                          minFrequency=20,
                                          maxFrequency=3500,
                                          maxPeaks=60)



        # Use default HPCP parameters
        hpcp = ess.HPCP()

        # Use pool to store data
        pool = essentia.Pool()

        # Connect streaming algorithms
        loader.audio >> framecutter.signal
        framecutter.frame >> windowing.frame >> spectrum.frame
        spectrum.spectrum >> spectralpeaks.spectrum
        spectralpeaks.magnitudes >> hpcp.magnitudes
        spectralpeaks.frequencies >> hpcp.frequencies
        hpcp.hpcp >> (pool, 'tonal.hpcp')

        # Run streaming network
        essentia.run(loader)


        arr = np.array(pool['tonal.hpcp'])
        hpcp_profile = np.average(arr,axis=0)


        db_cursor.execute('''UPDATE songs SET avg_hpcp_1=? WHERE song_name=?''',(float(hpcp_profile[0]),song_name))
        db_conn.commit()

        db_cursor.execute('''UPDATE songs SET avg_hpcp_2=? WHERE song_name=?''',(float(hpcp_profile[1]),song_name))
        db_conn.commit()

        db_cursor.execute('''UPDATE songs SET avg_hpcp_3=? WHERE song_name=?''',(float(hpcp_profile[2]),song_name))
        db_conn.commit()

        db_cursor.execute('''UPDATE songs SET avg_hpcp_4=? WHERE song_name=?''',(float(hpcp_profile[3]),song_name))
        db_conn.commit()

        db_cursor.execute('''UPDATE songs SET avg_hpcp_5=? WHERE song_name=?''',(float(hpcp_profile[4]),song_name))
        db_conn.commit()

        db_cursor.execute('''UPDATE songs SET avg_hpcp_6=? WHERE song_name=?''',(float(hpcp_profile[5]),song_name))
        db_conn.commit()

        db_cursor.execute('''UPDATE songs SET avg_hpcp_7=? WHERE song_name=?''',(float(hpcp_profile[6]),song_name))
        db_conn.commit()

        db_cursor.execute('''UPDATE songs SET avg_hpcp_8=? WHERE song_name=?''',(float(hpcp_profile[7]),song_name))
        db_conn.commit()

        db_cursor.execute('''UPDATE songs SET avg_hpcp_9=? WHERE song_name=?''',(float(hpcp_profile[8]),song_name))
        db_conn.commit()

        db_cursor.execute('''UPDATE songs SET avg_hpcp_10=? WHERE song_name=?''',(float(hpcp_profile[9]),song_name))
        db_conn.commit()

        db_cursor.execute('''UPDATE songs SET avg_hpcp_11=? WHERE song_name=?''',(float(hpcp_profile[10]),song_name))
        db_conn.commit()

        db_cursor.execute('''UPDATE songs SET avg_hpcp_12=? WHERE song_name=?''',(float(hpcp_profile[11]),song_name))
        db_conn.commit()

    for i in range(10,100):
        song_name = name + '.' + '000' + str(i) + '.au'
        print(song_name)
        loader = ess.MonoLoader(filename="genres/"+name+"/"+song_name)
        framecutter = ess.FrameCutter(frameSize=4096, hopSize=2048, silentFrames='noise')
        windowing = ess.Windowing(type='blackmanharris62')
        spectrum = ess.Spectrum()
        spectralpeaks = ess.SpectralPeaks(orderBy='magnitude',
                                          magnitudeThreshold=0.00001,
                                          minFrequency=20,
                                          maxFrequency=3500,
                                          maxPeaks=60)



        # Use default HPCP parameters
        hpcp = ess.HPCP()

        # Use pool to store data
        pool = essentia.Pool()

        # Connect streaming algorithms
        loader.audio >> framecutter.signal
        framecutter.frame >> windowing.frame >> spectrum.frame
        spectrum.spectrum >> spectralpeaks.spectrum
        spectralpeaks.magnitudes >> hpcp.magnitudes
        spectralpeaks.frequencies >> hpcp.frequencies
        hpcp.hpcp >> (pool, 'tonal.hpcp')

        # Run streaming network
        essentia.run(loader)


        arr = np.array(pool['tonal.hpcp'])
        hpcp_profile = np.average(arr,axis=0)


        db_cursor.execute('''UPDATE songs SET avg_hpcp_1=? WHERE song_name=?''',(float(hpcp_profile[0]),song_name))
        db_conn.commit()

        db_cursor.execute('''UPDATE songs SET avg_hpcp_2=? WHERE song_name=?''',(float(hpcp_profile[1]),song_name))
        db_conn.commit()

        db_cursor.execute('''UPDATE songs SET avg_hpcp_3=? WHERE song_name=?''',(float(hpcp_profile[2]),song_name))
        db_conn.commit()

        db_cursor.execute('''UPDATE songs SET avg_hpcp_4=? WHERE song_name=?''',(float(hpcp_profile[3]),song_name))
        db_conn.commit()

        db_cursor.execute('''UPDATE songs SET avg_hpcp_5=? WHERE song_name=?''',(float(hpcp_profile[4]),song_name))
        db_conn.commit()

        db_cursor.execute('''UPDATE songs SET avg_hpcp_6=? WHERE song_name=?''',(float(hpcp_profile[5]),song_name))
        db_conn.commit()

        db_cursor.execute('''UPDATE songs SET avg_hpcp_7=? WHERE song_name=?''',(float(hpcp_profile[6]),song_name))
        db_conn.commit()

        db_cursor.execute('''UPDATE songs SET avg_hpcp_8=? WHERE song_name=?''',(float(hpcp_profile[7]),song_name))
        db_conn.commit()

        db_cursor.execute('''UPDATE songs SET avg_hpcp_9=? WHERE song_name=?''',(float(hpcp_profile[8]),song_name))
        db_conn.commit()

        db_cursor.execute('''UPDATE songs SET avg_hpcp_10=? WHERE song_name=?''',(float(hpcp_profile[9]),song_name))
        db_conn.commit()

        db_cursor.execute('''UPDATE songs SET avg_hpcp_11=? WHERE song_name=?''',(float(hpcp_profile[10]),song_name))
        db_conn.commit()

        db_cursor.execute('''UPDATE songs SET avg_hpcp_12=? WHERE song_name=?''',(float(hpcp_profile[11]),song_name))
        db_conn.commit()





db_conn.close()
