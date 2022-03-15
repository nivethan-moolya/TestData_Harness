import pandas as pd
import traceback
import logging
import string
from utility import random_value, create_dict

def excel_file(filename, sheetsize, rowsize, colsize, type):
    try:
        writer = pd.ExcelWriter(f'{filename}.xlsx')
        
        df = pd.DataFrame()
        #Creates N number of Sheets
        for i in range(0, sheetsize):
            sht_name= f'Sheet_{random_value(string.ascii_uppercase, 4)}'
            df.to_excel(writer, sheet_name=sht_name)

            #Creates Rows & Columns in each sheet
            values = create_dict(rowsize, colsize, type)
            df = pd.DataFrame(values)
            df.to_excel(writer,sheet_name=sht_name, index=False )
            
        writer.save()
    except IOError as er:
        print('File Creation Disrupt: ', er)
        logging.error(traceback.format_exc())

def ask_tester():
    try:
        filename = input('Provide File name: ')
        sheets = int(input('How many sheets: '))
        rows = int(input('How many Rows: '))
        columns = int(input('How many Columns: '))
        print('Provide Datatypes as, Ex: String Integer Date Boolean Float')
        datatypes = [i for i in input('Provide Datatypes in List: ').split()]
        excel_file(filename, sheets, rows, columns,datatypes)
    except ValueError as er:
        print('User Input Disrupt: ', er)
        logging.error(traceback.format_exc())

ask_tester()