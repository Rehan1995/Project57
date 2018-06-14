My_list = list(range(1,10))

def funtionOne(listValue):
    total = 0
    element = 0
    while element< len(listValue):
        if listValue[element]%5 ==0:
            total += listValue[element]
        element += 1
    print(total)


funtionOne(My_list)

def funtionTwo():
    total_Value =0
    position_Value =0
    Number_List = [1,2,3,-5,-3,-4,-10]
    while position_Value < len(Number_List) and Number_List[position_Value]<-10:
        total_Value += Number_List[position_Value]
        position_Value +=1
    print(total_Value)

funtionTwo()


class pyClassOne:
    def __init__(self,name,age,phoneNumber):
        self.myName = name
        self.myAge = age
        self.myPhoneNumber = phoneNumber
        print("my name is :"+ self.myName)
        print("my age  is :"+ self.myAge)
        print("my phoneNumber is :"+ self.myPhoneNumber)


ClassOneObject = pyClassOne("rehan",22,716)

print(ClassOneObject)