import crypto_history as ch
import os

the_path = os.path.dirname(os.path.abspath(__file__))
data_dir = str(os.path.abspath(os.path.join(the_path, os.pardir))) + "/data/"
start_date = '20130429'
end_date = '20180702'

coin = 'bitcoin'

print('Getting data of: {0}\n'.format(
    coin))
headers, historicaldata = ch.gather(start_date, end_date, [coin])
ch.Save(headers, historicaldata, coin + '_all', data_dir)
