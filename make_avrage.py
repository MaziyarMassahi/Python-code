import pandas
import numpy
from constants import TimeFrame
def make_avrage( part, accepted = True , _time = False):
    df_0 = pandas.read_csv( 'extra/agv_0.csv' )
    df_1 = pandas.read_csv( 'extra/agv_1.csv' )
    df_2 = pandas.read_csv( 'extra/agv_2.csv' )

    if accepted == True:
        temp_0 = df_0.query( f'part == "{part}" & accepted == True ' )
        temp_1 = df_1.query( f'part == "{part}" & accepted == True ' )
        temp_2 = df_2.query( f'part == "{part}" & accepted == True ' )
    else:
        temp_0 = df_0.query( f'part == "{part}" & accepted == False ' )
        temp_1 = df_1.query( f'part == "{part}" & accepted == False ' )
        temp_2 = df_2.query( f'part == "{part}" & accepted == False ' )

    ttf = []
    buffer = []
    time = []

    last_time = 0
    ttf_ = []
    buffer_ = []
    time_ = []
    for row in temp_0.iterrows():
        row = row[1]

        if row[0] >= last_time :
            
            ttf_.append( int( row[ 5 ] ) )
            buffer_.append( int( row[ 3 ] ) )
            last_time = row[0]
            time_.append(int(row[0]))
        else:

            ttf.append( ttf_ )
            buffer.append( buffer_ )
            time.append( time_ )
            ttf_ = []
            buffer_ = []
            last_time = 0

    
    last_time = 0
    ttf_ = []
    buffer_ = []
    time_ = []
    for row in temp_1.iterrows():
        row = row[1]

        if row[0] >= last_time :
            
            ttf_.append( int( row[ 5 ] ) )
            buffer_.append( int( row[ 3 ] ) )
            last_time = row[0]
            time_.append(int(row[0]))
        else:

            ttf.append( ttf_ )
            buffer.append( buffer_ )
            time.append( time_ )
            ttf_ = []
            buffer_ = []
            last_time = 0

    last_time = 0
    ttf_ = []
    buffer_ = []
    time_ = []
    for row in temp_2.iterrows():
        row = row[1]

        if row[0] >= last_time :
            
            ttf_.append( int( row[ 5 ] ) )
            buffer_.append( int( row[ 3 ] ) )
            last_time = row[0]
            time_.append(int(row[0]))
        else:

            ttf.append( ttf_ )
            buffer.append( buffer_ )
            time.append( time_ )
            ttf_ = []
            buffer_ = []
            last_time = 0
    av_ttf = []
    av_buf = []
    av_time = []
    for episode1, episode2 in zip( ttf, buffer ):
        av_ttf.append( numpy.mean( episode1 ) / TimeFrame.HOUR )
        av_buf.append( numpy.mean( episode2 ) )
        av_time.append( numpy.mean(episode1) /  TimeFrame.HOUR)
    if not _time:
        return numpy.sort( av_ttf)[::-1], av_buf
    else:
        return av_ttf, av_buf, av_time
    # return av_ttf, av_buf


def get_last_episode( file_path ):
    
    df = pandas.read_csv( file_path )
    time = 10e10
    li = None

    for index, row in df.iloc[:: -1].iterrows():
        if row['time'] <= time:
            time = row['time']

        else:
            li =  index
            break
    print('=-------------------------- last index ------------------------------')
    print(li)
    return df.iloc[ li + 1 ::]



