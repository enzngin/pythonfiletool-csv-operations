import pandas as pd

class crudCSV:
    def __init__(self,path,fields = None):
        if fields is not None: #Yeni bir CSV oluşturacaksak kullanılacak constructor
            self.path = path
            self.fields = fields
            self.createCSV(fields)
        if fields is None: #Varolan CSV üzerinden işlem yapılacaksa kullanılacak constructor
            self.path = path

    def createCSV(self,fields):
        df = pd.DataFrame(columns=fields)
        df.to_csv(self.path, sep=";", encoding='utf-8', columns=fields, header=fields, index=False)
        print(self.path, "Successfully created a CSV file")

    def getCSV(self):
        return pd.read_csv(self.path,sep = ";")

    def addData(self,list): #Column sayısı kadar ve aynı sırayla veri tutan bir liste(tek rowa karşılık gelecek)
        df = self.getCSV()
        addRow = pd.Series(list, index=df.columns)
        df = df.append(addRow,ignore_index = True)
        df.to_csv(self.path, sep=";", encoding='utf-8', index=False)
        print(df)
        print("Successfully added!")

    def deleteData(self,index):
        df = self.getCSV()
        df = df.drop(index)
        df.to_csv(self.path, sep=";", encoding='utf-8', index=False)
        print(df)
        print("Successfully deleted!")

    def updateByIndex(self,index,column,newData):
        df = self.getCSV()
        df.at[index, column] = newData
        df.to_csv(self.path, sep=";", encoding='utf-8', index=False)
        print(df)
        print("Successfully updated!")

    def searchData(self,searchColumn,keyValue):
        df = self.getCSV()
        df = df.loc[df[searchColumn].str.contains(keyValue, case=False)]
        print(df)
        print("Successfully searched!")

    def convertToJson(self):
        df = self.getCSV()
        df = df.reset_index().to_json(orient='records')
        print(df)
        print("Successfully converted to JSON form!")

    def exportToJsonFile(self,path):
        df = self.getCSV()
        df.reset_index().to_json(path, orient='records')
        print("Successfully saved as JSON file!")

    def getColumns(self):
        df = self.getCSV().columns.values
        return df



































