#insertion-sort
#author Chengxi Li

class insert_sort():
    def __init__(self,data) -> None:
        self.data=data
    def sort_up(self):
        '''升序排列'''
        for j in range(1,len(self.data)):
            key=self.data[j]
            i=j-1
            while i>=0 and self.data[i]>key:
                self.data[i+1]=self.data[i]
                i=i-1
            self.data[i+1]=key
        print(self.data)
    def sort_down(self):
        '''降序排列'''
        for j in range(1,len(self.data)):
            key=self.data[j]
            i=j-1
            while i>=0 and self.data[i]<key:
                self.data[i+1]=self.data[i]
                i=i-1
            self.data[i+1]=key
        print(self.data)
data=[31,41,59,26,41,58]
insert=insert_sort(data)
insert.sort_up()
insert.sort_down()