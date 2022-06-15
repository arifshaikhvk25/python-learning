# ## getter setter 

class Programmer :
    salary = 10
    salary_bonous = 5

    @property
    def total_salary (self):
        return self.salary + self.salary_bonous

    @total_salary.setter
    def total_salary (self, salary_value):
        self.salary_bonous = salary_value - self.salary

p = Programmer()
print(p.salary)
print(p.salary_bonous)

p.total_salary = 15
print(p.salary_bonous)


class Employee :
    salary = 25
    salary_increment = 5

    @property
    def salary_After_Increment (self):
        print(f"{self.salary} * {self.salary_increment}")    
        return self.salary * self.salary_increment
        # print(f"{self.salary} * {self.salary_increment}")    
    
    @salary_After_Increment .setter
    def salary_After_Increment (self,incrementOfSalary):
        self.salary_increment = incrementOfSalary / self.salary
        print(f"{self.salary_increment} = {self.salary_After_Increment} / {self.salary}")
    


e = Employee()
print(e.salary)
print(e.salary_increment)

e.salary_After_Increment = 30
print(e.salary)
print(e.salary_increment)
