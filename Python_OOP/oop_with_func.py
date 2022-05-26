class People:
    def __init__(self, first_name, last_name , age, height):
        self.people_first_name = first_name
        self.people_last_name = last_name
        self.people_age = age
        self.people_height = height

    def get_name(self):
        return self.people_first_name + " "+ self.people_last_name
    
    def set_name(self, new_name):
        self.people_first_name = new_name
        
    def all_info(self):
        return f"Full Name : {self.get_name()} Age: {self.people_age} , People Height : {self.people_height}"
    #   return "Full Name : {} Age: {} , People Height : {}".format(self.get_name(),self.people_age, self.people_height )
    
people_1 = People("Rahima","Uddin", "27", "59")

print(people_1.all_info())

people_1.set_name("Rahim")

print(people_1.all_info())



people_2 = People("Karim","Hasan", "37", "56")

print(people_2.get_name())
print(people_2.people_age)
print(people_2.people_height)


    


