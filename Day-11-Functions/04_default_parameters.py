# Day 11 - Default Parameters

def greetings(name="Guest"):
    return name + ", welcome to Python!"

def generate_full_name(first_name="Python", last_name="Learner"):
    return first_name + " " + last_name

def calculate_age(birth_year, current_year=2026):
    return current_year - birth_year

def weight_of_object(mass, gravity=9.81):
    return mass * gravity

print(greetings())
print(greetings("Snehankur"))
print(generate_full_name())
print(generate_full_name("John", "Doe"))
print("Age:", calculate_age(2002))
print("Age in 2030:", calculate_age(2002, 2030))
print("Weight on Earth:", weight_of_object(100), "N")
print("Weight on Moon:", weight_of_object(100, 1.62), "N")
