from os import listdir
from os.path import isfile, join
import pandas as pd


DATADIR = "P:\Python\Project\Data_Viz\data"

class ReadFiles:
    def readFilesFromFolder(self):
        #read all files in the folder and store the names in an array
        data_files = [_file for _file in listdir(DATADIR) if isfile(join(DATADIR, _file))]
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
        # print("Total number of columns",len(all_columns))
        unique_list = (list(list_set)) 
        # print("Total number of unique columns", len(unique_list))
        # print(unique_list)
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
                            content = str(str(i) + " " + str(k) + " "+ column + "\n")
                            f.write(content)
        
        f.close()
                        

rf = ReadFiles()
dfo = DataFrameOperations()

list_of_data_frames = rf.readFilesFromFolder()
all_columns = dfo.getUniqueColumnsAcrossFrames(list_of_data_frames)


# print(list_of_data_frames)
    


