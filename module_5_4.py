class House:
    houses_history=[]

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        # print(cls.houses_history)
        return

    def __init__(self,name ,number_of_floors):
        self.name = args[0]
        self.number_of_floors = args[1]




    def go_to(self,new_floor):
        if new_floor > self.number_of_floors or new_floor <1:
            print('"Такого этажа не существует"')
        else:

            for i in range(new_floor):
                print (i+1)

    def __len__(self):
        s=self.number_of_floors
        return s
    def __str__(self):
        s='Название: '+ str(self.name) + ", кол-во этажей: "+str(self.number_of_floors)
        return s  # 'Название: ',self.name, ", кол-во этажей: ", self.number_of_floors

    def __eq__(self, other):

        if isinstance(other, House):
            if self.number_of_floors == other.number_of_floors:
                return True
            else:
                return False
        elif isinstance(other, int):
            if self.number_of_floors == other:
                return True
            else:
                return False

    def __ne__(self, other):
        if isinstance(other, House):
            if self.number_of_floors != other.number_of_floors:
                return True
            else:
                return False
        elif isinstance(other, int):
            if self.number_of_floors != other:
                return True
            else:
                return False
    def __lt__(self, other):
        if isinstance(other, House):
            if self.number_of_floors < other.number_of_floors:
                return True
            else:
                return False
        elif isinstance(other, int):
            if self.number_of_floors < other:
                return True
            else:
                return False
    def __le__(self, other):
        if isinstance(other, House):
            if self.number_of_floors <= other.number_of_floors:
                return True
            else:
                return False
        #
    def __gt__(self, other):
        if isinstance(other, House):
            if self.number_of_floors > other.number_of_floors:
                return True
            else:
                return False
        elif isinstance(other, int):
            if self.number_of_floors > other:
                return True
            else:
                return False
    def __ge__(self, other):
        if isinstance(other, House):
            if self.number_of_floors >= other.number_of_floors:
                return True
            else:
                return False
        elif isinstance(other, int):
            if self.number_of_floors >= other:
                return True
            else:
                return False

    def __add__(self, value):
        if isinstance(value,int):

            self.number_of_floors +=  value

        return self

    def __iadd__(self, value):
        if isinstance(value,int):
            self.number_of_floors += value
            return self

    def __radd__(self, value):
        if isinstance(value,int):
            self.number_of_floors = value + self.number_of_floors
            return self

    def __del__(self):
        print(  " снесён, но он останется в истории")
        return self

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)