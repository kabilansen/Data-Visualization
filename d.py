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


        print(len(all_columns))
        unique_list = (list(list_set)) 
        print(len(unique_list))
        



rf = ReadFiles()
dfo = DataFrameOperations()

list_of_data_frames = rf.readFilesFromFolder()
all_columns = dfo.getUniqueColumnsAcrossFrames(list_of_data_frames)


# print(list_of_data_frames)
    


