import json
import pprint

# ACTIVITY 1
student_list = ['pam', 'rob', 'joe', 'greg', 'bob', 'amy', 'matt']
print(student_list[2:5])
print(student_list[0:3])
print(student_list[5:6])
print(student_list[0:6])
if 'rob' in student_list:
    print("Yes, Rob is in the students list")

# ACTIVITY 2
p1 = {"name": "John", "age": 61, "city": "Eugene"}
p2 = {"name": "Risa", "age": 16, "city": "New York"}
p3 = {"name": "Ryan", "age": 16, "city": "Los Angeles"}
p4 = {"name": "Shekar", "age": 16, "city": "San Francisco"}
# a list of dictionaries
list_of_people = [p1, p2, p3, p4]
# write some code to Print List of people one by one
print(list_of_people[0:3])
# turn list to dictionary of people
dict_people = {'people': list_of_people}
print("List to Dictionary of people")
print(type(dict_people))
print(dict_people)
# write some code to Print People from Dictionary
print(dict_people['people'])
# turn dictionary to JSON
print("** Dumps - Python to JSON String**")
json_people = json.dumps(list_of_people)
print("JSON People #1")
print(type(json_people))
print(json_people)
# write some code to pretty print the JSON dict
pprint.pprint(json_people)
# write some code to unwind JSON using json.loads and print the people
print("** Loads - JSON to Python Dict**")
json_dict = json.loads(json_people)
print(json_dict)
# to list
names = [person['name'] for person in json_dict]
print("Names of people to list: " + str(names))
print("Names of people: ")
# pretty print Names of People
pprint.pprint("Names of people: " + str(names))
