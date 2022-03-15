import random
import time
import string
from random_word import RandomWords
import traceback
import logging

def random_value(format, leng):
    try:
        val = ''.join(random.choices(format, k=leng))
        return val
    except IOError as er:
        print('random_value disrupted: ', er)
        logging.error(traceback.format_exc())


def random_date(start, end, time_format, prop):
    try:
        stime = time.mktime(time.strptime(start, time_format))
        etime = time.mktime(time.strptime(end, time_format))
        ptime = stime + prop * (etime - stime)
        return time.strftime(time_format, time.localtime(ptime))
    except IOError as er:
        print('random_date disrupted: ', er)
        logging.error(traceback.format_exc())

def create_dict(rowsize, colsize, datatype):
    try:
        dict = {}
        for j in range(0, colsize):
            datType = random.choice(datatype)
            type = datType.lower()
            if 'string' in type:
                s = [random_value(string.ascii_lowercase, 8) for _ in range(rowsize)] 
                dict[f'Col_{random_value(string.ascii_uppercase,5)}'] = s

            elif 'int' in type:
                n = [random.randint(0,10000) for _ in range(rowsize)]
                dict[f'Col_{random_value(string.ascii_uppercase,5)}'] = n

            elif 'date' in type:
                frmt = '%Y-%m-%d'
                stime = '1990-01-02'
                etime = '2020-01-02'
                d = [random_date(stime, etime, frmt, random.random())  for _ in range(rowsize)]
                dict[f'Col_{random_value(string.ascii_uppercase,5)}'] = d
            elif 'float' in type:
                f = [(round(random.uniform(100,1000),3)) for _ in range(rowsize)]
                dict[f'Col_{random_value(string.ascii_uppercase,5)}'] = f
            elif 'boolean' in type:
                bool = [True, False]
                b = [random.choice(bool) for _ in range(rowsize)]
                dict[f'Col_{random_value(string.ascii_uppercase,5)}'] = b
            else:
                s = RandomWords().get_random_words(includePartOfSpeech="noun,verb", minLength=5, maxLength=10, sortBy="alpha", limit=rowsize)

                dict[f'Col_{random_value(string.ascii_uppercase,5)}'] = s
        #print(dict)
        return dict
    except IOError as er:
        print('create_dict disrupted: ', er)
        logging.error(traceback.format_exc())

