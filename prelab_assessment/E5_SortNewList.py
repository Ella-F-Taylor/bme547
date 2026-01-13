#sorting and creating new lists
#given random list, create a new list that contains only even #s and sorted into ascending order

wild_list = [-5, 10, 3, 4, 22, 'a', None]
even_list = []

for item in wild_list:
    if type(item) is int or type(item) is float:
        if item %2 == 0: #even # no remainder
            even_list.append(item)

even_list_sorted = sorted(even_list) #default is ascending order, do reverse = True for descending
print("Sorted even list:", even_list_sorted)
