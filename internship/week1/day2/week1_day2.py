class vehicles:
    def __init__(self,name,model,year): #constructor
        self.name = name
        self.model = model
        self.year = year
    
    def display(self): #display method
         print("Name: " + self.name + ", Model: " + self.model + ", Year: " + str(self.year))
    
    def set_year(self, year): #setter method
        self.year = year
        print(self.name +" " + self.model +" " + "Model year updated to: " + str(self.year))
        
        
car = vehicles("Toyota", "Camry", 2020) #object instance of the class
suv = vehicles("Honda", "CR-V", 2021) #object instance of the class

car.display()
suv.display()

suv.set_year(2022) #updating the year of the suv object
