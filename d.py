from os import listdir
from os.path import isfile, join
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


DATADIR = "P:\Python\Project\Data_Viz\data"
LIST_RACE = ["# Asian","# Black","# White","# Hispanic","# Multiple Race Categories Not Represented"]
LIST_RACE = ["Grade 2","Grade 1"]
LIST_RACE = ["# Female", "# Male"]

class ReadFiles:
    def readFilesFromFolder(self):
        #read all files in the folder and store the names in an array
        data_files = [_file for _file in listdir(DATADIR) if isfile(join(DATADIR, _file))]
        f= open("index_filename.txt", "w")
        for index, value in enumerate(data_files):
            f.write(str(index) + "," + value + "\n")
        f.close()
        return self.createDataFramesFromFileList(data_files)

    def createDataFramesFromFileList(self, csv_file_list):
        data_frame = [pd.read_csv(DATADIR+"\\"+frame) for frame in csv_file_list]
        return data_frame

class DataFrameOperations:
    def getCommonColumnsAcrossFrames(self, list_of_data_frames):
        pass
    def getUniqueColumnsAcrossFrames(self, list_of_data_frames):
        list_of_all_columns = []
        for frame in list_of_data_frames:
            list_of_all_columns.append(frame.columns)
        all_columns = []
        for col_list in list_of_all_columns:
            for col in col_list:
                all_columns.append(col)
        list_set = set(all_columns)
        unique_list = (list(list_set)) 
        self.createMatrixofCommonColumns(list_of_all_columns)

    def createMatrixofCommonColumns(self, list_of_all_columns):
        skipper = 0
        f = open("common_columns.txt", "a")
        
        for i, list_columns_in_frame in enumerate(list_of_all_columns):
            for j, column in enumerate(list_columns_in_frame):
                for k, list_columns_in_frame in enumerate(list_of_all_columns):
                    for l, column in enumerate(list_columns_in_frame):
                        if(i == k):
                            continue
                        if(list_of_all_columns[i][j] == list_of_all_columns[k][l]):
                            content = str(str(i) + "," + str(k) + ","+ column + "\n")
                            # content = str(str(i) + " " + str(k) + "\n")
                            f.write(content)
        
        f.close()



class Race:
    def calculateSum(self,LIST_RACE,dataframe):
        total_sum = 0
        dict_sum_race = dict()
        for race in LIST_RACE:
            _sum = dataframe[race].sum()
            dict_sum_race[race] = _sum
            total_sum+=_sum
        return self.calculatePercentage(total_sum,dict_sum_race)

      
    def calculatePercentage(self,total_sum,dict_sum_race):
        for key,value in dict_sum_race.items():
            dict_sum_race[key] = (value/total_sum)*100
        dataset_1 = list(dict_sum_race.values())

        return dict_sum_race
        

    def calculateStdDev(self):
        stddev_dataset_1 = np.std(dataset_1)     

class visualization:
      def drawPieChart(self,list_dict_pie):
            list_labels = list_dict_pie.keys()
            list_values = list_dict_pie.values()
            fig1, ax1 = plt.subplots()
            ax1.pie(list_values, labels=list_labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
            ax1.axis('equal')
            plt.show()  
      def drawHistogram(self):
         
         std_values = stddev_dataset_1.tolist()
         x = [std_values]
         plt.hist(x)
         plt.show()

rf = ReadFiles()
dfo = DataFrameOperations()

# print(DATADIR)

list_of_data_frames = rf.readFilesFromFolder()
all_columns = dfo.getUniqueColumnsAcrossFrames(list_of_data_frames)

# df1 = pd.read_csv(DATADIR+r"\04_2013_-_2018_Demographic_Snapshot_District.csv",) 
# df2 = pd.read_csv(DATADIR+r"\02_2015_-_2018_Demographic_Snapshot_Pre-_K_For_All.csv") 
df3 = pd.read_csv(DATADIR+r"\03_2013_-_2018_Demographic_Snapshot_Borough.csv") 
df4 = pd.read_csv(DATADIR+r"\04_2013_-_2018_Demographic_Snapshot_District.csv") 
# df5 = pd.read_csv(DATADIR+r"\05_2017_-_2018_Demographic_Snapshot_3-_K_For_All.csv") 
list_dict_pie = list()  
for df in (df3,df4):
    race = Race()
    vis = visualization()
    list_dict_pie.append(race.calculateSum(LIST_RACE,df))
for _dict in list_dict_pie:
    vis.drawPieChart(_dict)
    


