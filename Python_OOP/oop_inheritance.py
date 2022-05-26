class Parent:
    def __init__(self, f_name , m_name, property):
        self.father_name = f_name
        self.mother_name = m_name
        self.p_property = property
        
    def parent_properties(self):
        return self.p_property
    
    def parent_info(self):
        return f"Parents name : {self.father_name}, and {self.mother_name} , Their properties: {self.parent_properties()}"

# p1 = Parent("Badsha", "Rahena", "15biga")
# print(p1.parent_info())

class Child(Parent):
    def __init__(self,f_name, m_name, property,  name, education):
        super().__init__(f_name , m_name, property)
        self.c_name = name
        self.c_education = education
        
    def Child_info(self):
        return f"Child name : {self.c_name}, Education: {self.c_education } and {self.parent_info()}"
    
c1 = Child("Badsha", "Rahena", "15biga", "Rana", "BSc")

print(c1.Child_info())
