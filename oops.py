# class fruits:
#     a="apple"
# obj=fruits()
# print(obj.a)

# class animal:
#     def __init__(self,color,type):
#         self.color=color
#         self.type=type
#     def sound(self):
#         print("the color of the animal is",self.color,"the animal is a",self.type)
# obj=animal("yellow","wild")
# obj.sound()


class animal:
    def __init__(self,color,type):
        self.color=color
        self.type=type
    def sound(self):
        print("the color of the animal is",self.color,"the animal is a",self.type)
    
class lion(animal):
    pass
obj=lion("orange","wild")
obj.sound()

print("new content")