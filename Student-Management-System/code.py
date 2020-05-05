# --------------
# Code starts here

# Create the lists 
class_1 = ["Geoffrey Hinton", "Andrew Ng", "Sebastian Raschka", "Yoshua Bengio"]
class_2 = ["Hilary Mason", "Carla Gentry", "Corinna Cortes"]
# Concatenate both the strings
new_class = class_1+ class_2
print("new_class:",new_class)
# Append the list
new_class.append("Peter Warden")
# Print updated list
print("\nnew_class:",new_class)
# Remove the element from the list
new_class.remove("Carla Gentry")
# Print the list
print("\nnew_class:", new_class)
# Create the Dictionary
courses = {"Math":65, "English":70, "History":80, "French":70, "Science":60}
print("\ncourses:", courses)
# Store the all the subject in one variable `Total`
total = sum(courses.values())
# Print the total
print("\ntotal:",total)
# Print the percentage
percentage = total/5
print("\nGeoffrey Hinton percentage:", percentage)
# Slice the dict and stores  the all subjects marks in variable
mathematics = {'Geoffrey Hinton':78,'Andrew Ng':95,'Sebastian Raschka':65,'Yoshua Benjio':50,'Hilary Mason':70,'Corinna Cortes':66,'Peter Warden':75}
topper = max(mathematics,key=mathematics.get)
print("\ntopper:",topper)
first_name = (topper.split()[1])
last_name = (topper.split()[0])
print("\nfirst_name:",first_name,"\nlast_name:",last_name)
full_name = first_name+" "+last_name
certificate_name = full_name.upper()
print("certificate_name:",certificate_name)




# Create the Dictionary
 



# Given string


# Create variable first_name 

# Create variable Last_name and store last two element in the list

# Concatenate the string

# print the full_name

# print the name in upper case

# Code ends here


