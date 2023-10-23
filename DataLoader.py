import openpyxl

def change(x):
    if x == 1:
        return 1
    else:
        return -1

class DataLoader:
    def __init__(self, filename="data.xlsx", data_size=(6, 3)):
        wb = openpyxl.load_workbook(filename)
        sh = wb['data']
        maxr = sh.max_row
        fullsize = data_size[0] * data_size[1]
        self.__train_set = [
            [
                1 if sh[chr(i % data_size[1]+ord('A'))+str(i//data_size[1]+1)].value==1 else -1
                for i in range(k*fullsize, (k+1)*fullsize)
            ] for k in range(maxr//data_size[0])
        ]

    def get_data(self):
        set = self.__train_set.copy()
        return set