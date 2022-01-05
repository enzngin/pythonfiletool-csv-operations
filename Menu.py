import FileTool as ft

class TerminalMenu:



    def showMainMenu(self):
        print("-Press 1 for create a new CSV file \n-Press 2 for work on an already exist CSV file")
        x = input()
        if(x == "1"):
            print("Enter the path and fields.")
            print("Path: ", end = "")
            path = input()
            print("Fields(Arada boşluk bırakarak giriniz!): ", end = "")
            fields = input()
            ftObj = ft.crudCSV(path,fields.split())
            self.operationsMenu(ftObj)
        if (x == "2"):
            print("Enter the path of the existing CSV file")
            print("Path: ", end=" ")
            path = input()
            ftObj = ft.crudCSV(path)
            self.operationsMenu(ftObj)

    def operationsMenu(self,csvObj):
        print("Operation list")
        print("-Press 1 for read the CSV file \n-Press 2 for add row to the CSV file "
              "\n-Press 3 for delete row from the CSV file")
        print("-Press 4 for update row on the CSV file "
              "\n-Press 5 for search on the CSV file  \n-Press 6 for for CSV file convert to JSON format")
        print("-Press 7 for save CSV file as JSON file")
        x = input()
        menu = {
            "1" : self.readMenu(csvObj), "2": self.insertMenu(csvObj), "3": self.deleteMenu(csvObj), "4": self.updateMenu(csvObj),
            "5": self.searchMenu(csvObj), "6": self.jsonFormMenu(csvObj), "7": self.jsonSaveMenu(csvObj)
        }
        menu[x]()

    def readMenu(self,csvObj):
        print(csvObj.getCSV())
        self.escapeMenu(csvObj)

    def insertMenu(self, csvObj):
        print("Enter the data you want to add in the column order, with spaces in between.")
        print("Columns: ", csvObj.getColumns())
        print("Data for add: ", end = "")
        x = input()
        csvObj.addData(x.split())
        self.escapeMenu(csvObj)

    def deleteMenu(self, csvObj):
        print(csvObj.getCSV())
        print("Enter the index number of the record you want to delete.")
        print("Index number :", end = "")
        x = input()
        csvObj.deleteData(int(x))
        self.escapeMenu(csvObj)

    def updateMenu(self, csvObj):
        print(csvObj.getCSV())
        print("Enter the index, column, new data of the record you want to update.")
        print("Index number: ", end = "")
        index = input()
        print("Column : ", end="")
        column = input()
        print("New data: ", end="")
        data = input()
        csvObj.updateByIndex(int(index),column,data)
        self.escapeMenu(csvObj)

    def searchMenu(self, csvObj):
        print("Enter the column you want to search")
        print("Columns: ", csvObj.getColumns())
        print("Column for search: ", end = "")
        column = input()
        print("Enter the key value you want to search by the column")
        print("Value for search: ", end="")
        value = input()
        csvObj.searchData(column,value)
        self.escapeMenu(csvObj)

    def jsonFormMenu(self, csvObj):
        csvObj.convertToJson()
        self.escapeMenu(csvObj)

    def jsonSaveMenu(self, csvObj):
        print("Enter the path.")
        print("Path: ", end="")
        path = input()
        csvObj.exportToJsonFile(path)
        self.escapeMenu(csvObj)

    def escapeMenu(self, csvObj):
        print("Press 1 for to Main Menu \nPress 2 for to Operations Menu \nPress q for quit program")
        x = input()
        if(x == "1"):
            self.showMainMenu()
        elif(x == "2"):
            self.operationsMenu(csvObj)
        elif(x == "q"):
            pass


















