print("hello")
print("we have been waiting for you for a long time")
x=6
print(x)
y = x *7

name = input('Enter file: ')
handle = open(name, 'r')
counts = dict()

for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in list(counts.items()):
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)#example code from p4e 
#https://notebooks.latis.umn.edu/user/zhan8462/lab/tree/Untitled.ipynb
#Chapter 2 
print(4)
type('Hello, World!')#type告诉你value是什么形式的 （str) 
type(17)#'int' 
type(3.2)
type('17')

#
#Goal: I want to save data parameters for different users, and then I want to use a simple logic command to pull the information, and print the information out in my command. 
#### coding practice 
Alaina = 19, 169, 60, "CHN"
Bob = 22, 188, 80, "USA"
Cath = 21, 166, 57, "KRA"
#print (f'This is {
#    if Name = bob:
 #       print Bob [1]
  #  else:
   #     print Cath[1] } ')
#first attempt was rough. I realized I cannot really call out the variable like I wanted to. 
users_data = [
    {"name": "Alaina", "age": 19, "height": 169, "weight": 60, "nationality": "CHN"},
    {"name": "Bob", "age": 22, "height": 188, "weight": 80, "nationality": "USA"},
    {"name": "Cath", "age": 21, "height": 166, "weight": 57, "nationality": "KRA"}
]

# Function to print user information
def print_user_info(name):
    user = next((user for user in users_data if user["name"] == name), None)
    if user:
        print(f"{name}'s information:")
        print(f"Age: {user['age']}")
        print(f"Height: {user['height']}")
        print(f"Weight: {user['weight']}")
        print(f"Nationality: {user['nationality']}")
    else:
        print(f"User {name} not found.")

# Example usage
user_to_print = "Alaina"
print_user_info(user_to_print)




def greeting(first, last): 



import random
def random_greeting ():#this is an idea from class, wanted to write the random generator 
    greetings = [
        "it was a pleasure too meet you",
        "you are so inspiring",
        "this was amazing meeting you", 
        "looking forward to see you soon"
    ]

    select_greet = random.randint(0, len(greetings)-1)
    return greetings [select_greet]
   # print_greet = greetings[select_greet]
    print(random_greeting)

random_greeting()#calls out the program that is defined above 

#create a user pool 
person1 = ("Ben", "Kainer", 19, "Paris")
person2 = ("Alice", "Johnson", 21, "New York")
person3 = ("Mark", "Smith", 20, "London")
#creating a separate list 
class_roster = [person1,person2,person3]

#test out the code 
print(person1)

#create city coordinates
city_coordinates = {
    "Paris": (48.8566, 2.3522),
    "New York": (40.7128, -74.0060),
    "London": (51.5074, -0.1278)
}

#I want to associate the people with their city coordinates
class_roster_with_geo = []
for person in class_roster:
    name, last_name, age, city = person
    lat, lon = city_coordinates[city]
    class_roster_with_geo.append((name, last_name, age, city, lat, lon))

#now I want to combine the euclid_distance tool from earlier 
import math
minneapolis_coords = (44.9778,-93.2650) 
def euclid_dis(cord1, cord2):
  return math.sqrt(sum((x - y) ** 2 for x, y in zip(coord1, coord2)))

#write program to greet with distance info
def greet_calc_dist (person_name, class_roster, city_coordinates, minneapolis_coords):
   for person in class_roster:
      if person [0] == person_name: 
         city = person[3]
         person_coords = city_coordinates[city]
         distance = euclid_dis(person_coords, minneapolis_coords)

        #random greeting
         greeting = random_greeting()

         print (f'{person_name}, {greeting}, you came a long way from {distance:.2f} kilometers away to meet here.')
         return
    print (f'Person named {person_name} not found in class roster')
   
import random
def random_greeting ():#this is an idea from class, wanted to write the random generator 
    greetings = [
        "it was a pleasure too meet you",
        "you are so inspiring",
        "this was amazing meeting you", 
        "looking forward to see you soon"
    ]

    select_greet = random.randint(0, len(greetings)-1)
    return greetings [select_greet]
   # print_greet = greetings[select_greet]
    print(random_greeting)

random_greeting()#calls out the program that is defined above 

#create a user pool 
person1 = ("Ben", "Kainer", 19, "Paris")
person2 = ("Alice", "Johnson", 21, "New York")
person3 = ("Mark", "Smith", 20, "London")
#creating a separate list 
class_roster = [person1,person2,person3]

#test out the code 
print(person1)

#create city coordinates
city_coordinates = {
    "Paris": (48.8566, 2.3522),
    "New York": (40.7128, -74.0060),
    "London": (51.5074, -0.1278)
}

#I want to associate the people with their city coordinates
class_roster_with_geo = []
for person in class_roster:
    name, last_name, age, city = person
    lat, lon = city_coordinates[city]
    class_roster_with_geo.append((name, last_name, age, city, lat, lon))

#now I want to combine the euclid_distance tool from earlier 
import math
minneapolis_coords = (44.9778,-93.2650) 
def euclid_dis(cord1, cord2):
  return math.sqrt(sum((x - y) ** 2 for x, y in zip(coord1, coord2)))

#write program to greet with distance info
def greet_calc_dist (person_name, class_roster, city_coordinates, minneapolis_coords):
   for person in class_roster:
      if person [0] == person_name: 
         city = person[3]
         person_coords = city_coordinates[city]
         distance = euclid_dis(person_coords, minneapolis_coords)

        #random greeting
         greeting = random_greeting()

         print (f'{person_name}, {greeting}, you came a long way from {distance:.2f} kilometers away to meet here.')
         return
      

