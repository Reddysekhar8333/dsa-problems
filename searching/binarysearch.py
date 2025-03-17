class binarysearch:
    """ for the binary search elements should be in sorted order """
    def __init__(self,data):
        self.data=data
    def search(self):
        values=self.data
        element=int(input("enter the element that you need to find:"))
        first=0
        last=len(values)
        mid=int((first+last)/2)
        while first<=last:
            if values[mid]==element:
                print(f"{element} is found at {mid+1} location in the data!")
                return
            elif values[mid]>element:
                last=mid-1
            elif values[mid]<element:
                first=mid+1
            
            mid=int((first+last)/2)
        else:
            print(f"{element} is not found in data !")

elements=[10,20,30,40,50,60,70,80,90,100,110]

find=binarysearch(elements)
find.search()