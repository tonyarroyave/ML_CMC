import crypto_history as ch
import os

the_path = os.path.dirname(os.path.abspath(__file__))
data_dir = str(os.path.abspath(os.path.join(the_path, os.pardir))) + "/data/"
start_date = '20180101'
end_date = '20180702'

c_names = ch.CoinNames()
counter = 1
for coin in c_names:
    print('Getting data of: {0}, \nwhich is the {1} out of {2}'.format(
        coin, counter, len(c_names)))
    headers, historicaldata = ch.gather(start_date, end_date, [coin])
    ch.Save(headers, historicaldata, coin, data_dir)
    counter += 1
