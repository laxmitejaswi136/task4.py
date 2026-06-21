# 1. Create a new list containing the names of 5 different cities
cities = ["Hyderabad", "Mumbai", "Bangalore", "Delhi", "Chennai"]
print("Original list:", cities)

# 2. Use indexing to access and print the name of the city at the middle index of the list
# Total 5 elements, so middle index is 5 // 2 = 2
middle_index = len(cities) // 2
print("City at middle index:", cities[middle_index])

# 3. Use slicing to extract a subset of cities from the list (e.g., the first 3 cities) and print the result
first_three_cities = cities[0:3]
print("First 3 cities:", first_three_cities)

# 4. Sort the list of cities in ascending order and print the result
cities.sort()
print("Sorted list (ascending):", cities)

# 5. Append a new city to the end of the list and print the updated list
cities.append("Kolkata")
print("After appending a new city:", cities)

# 6. Remove the first city from the list and print the updated list
# pop(0) removes the element at index 0
cities.pop(0)
print("After removing the first city:", cities)

# 7. Write a function that takes a list of cities as input and returns the length of the list
def get_list_length(city_list):
    return len(city_list)

# 8. Test the function with the list of cities created in the first task and print the result
# Passing our updated 'cities' list into the function
length_of_list = get_list_length(cities)
print("Length of the list using function:", length_of_list)