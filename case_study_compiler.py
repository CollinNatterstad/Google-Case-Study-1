# os package to parse through directory files
import os
#glob will help parse through the .csv files in conjuction with OS
import glob
#will load .csv files into dataframe which is stored to a singular file. 
import pandas as pd

#uploader contains three parts, read csv, store rows, upload to database. 
def case_study_compiler():
    
    '''#shows file path of current directory
    curdir = os.curdir
    print(curdir)'''

    '''#prints file path of each file within a specific directory
    files_list = []
    for root, directories, files in os.walk(''d:\Google-Case Study 1\Divvy_Trips_Data\*.csv''):
        for name in files:
            files_list.append(os.path.join(root,name))
    print (files_list)'''

    '''#prints file path of each file that matches a SPECIFIC file type within a specific directory using glob method
    file_list = glob.glob('d:\Google - Case Study 1\Divvy Trips Data\*.csv')
    print(file_list)'''

    '''for file in file_list:
        with open(file) as csvf: 
            csvreader= csv.DictReader(csvf)
            for row in csvreader:
                files.append(row)'''


    file_list = glob.glob('d:\Google-Case_Study_1\Divvy_Trips_Data\*.csv')
    files = []

    for filename in file_list:
        df = pd.read_csv(filename)
        files.append(df)
        
    df = pd.concat(files, axis= 0, ignore_index= True)
    df.to_csv('complied_data_actual.csv', sep = ',',header = False, index= False, encoding= 'utf-8')
   
  
if __name__ == '__main__':
    case_study_compiler()