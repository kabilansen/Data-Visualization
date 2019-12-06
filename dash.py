from os import listdir
from os.path import isfile, join
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Dataset_Count = 1
DATADIR = "P:\Python\Project\Data_Viz\data"
LIST_RACE = []
# LIST_RACE = ["# Asian","# Black","# White","# Hispanic","# Multiple Race Categories Not Represented"]
# LIST_RACE = ["Grade 2","Grade 1"]
# LIST_RACE = ["# Female", "# Male"]

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
    
    def searchForColumns(self, columnName, list_of_data_frames):
        with open("common_columns.txt", "r") as f:
             line_in_file =  [line.rstrip() for line in f]
        columns = [line.split(",") for line in line_in_file]
        for index, entry in enumerate(columns):
            columns[index] = [int(entry[0]), int(entry[1]), entry[2]]
        result = [column for column in columns if columnName in column]
        uniqueFileIndex = [id for elements in result for id in elements] 
        print("Column \""+ columnName + "\" is found in: ", [item for item in set(uniqueFileIndex) if isinstance(item, int)])      
        return [item for item in set(uniqueFileIndex) if isinstance(item, int)]

        

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
    def calculateSum(self,type_of_chart,LIST_RACE,dataframe):
        total_sum = 0
        dict_sum_race = dict()
        for race in LIST_RACE:
            _sum = dataframe[race].sum()
            dict_sum_race[race] = _sum
            total_sum+=_sum
        if(type_of_chart == 'pie'):return self.calculatePercentage(total_sum,dict_sum_race)
        print(dict_sum_race)
        return dict_sum_race
        

      
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
      def drawHistogram(self, sum_dict):
        global Dataset_Count
        objects = sum_dict.keys()
        y_pos = np.arange(len(objects))
        performance = sum_dict.values()

        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Count')
        plt.title("Dataset: "+str(Dataset_Count))
        Dataset_Count+=1
        plt.show()

def doMain(type_of_chart):
    if(type_of_chart == 'pie'):
        list_of_input_dataframes = []
        all_columns = dfo.getUniqueColumnsAcrossFrames(list_of_data_frames)
        for index in result:
            list_of_input_dataframes.append(list_of_data_frames[index])
        list_dict_pie = list()  
        for df in list_of_input_dataframes:
            race = Race()
            vis = visualization()
            list_dict_pie.append(race.calculateSum('pie',LIST_RACE,df))
        for _dict in list_dict_pie:
            vis.drawPieChart(_dict)
    elif(type_of_chart == 'bar'):
        list_of_input_dataframes = []
        all_columns = dfo.getUniqueColumnsAcrossFrames(list_of_data_frames)
        for index in result:
            list_of_input_dataframes.append(list_of_data_frames[index])
        list_dict_pie = list()  
        for df in list_of_input_dataframes:
            race = Race()
            vis = visualization()
            list_dict_pie.append(race.calculateSum('bar',LIST_RACE,df))
        for _dict in list_dict_pie:
            vis.drawHistogram(_dict)
    


if __name__ == "__main__":
    result = []
    rf = ReadFiles()
    dfo = DataFrameOperations()
    flag = True
    while(flag):
        column = input("Enter the coulmn name you want to find: ")
        if(column == 'pie'):
            result = list(set.intersection(*map(set, result))) 
            doMain('pie')
        if(column == 'bar'):
            result = list(set.intersection(*map(set, result))) 
            doMain('bar')
        if(column == 'exit'):
            exit()
        print("Searching for: {a}".format(a = column))
        LIST_RACE.append(column)
        

        # print(DATADIR)

        list_of_data_frames = rf.readFilesFromFolder()
        result.append(dfo.searchForColumns(column, list_of_data_frames))

    # exit()
    
    


    