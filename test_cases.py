
from functools import reduce
# lambda is a anonymous function  funciton which dont have a name
# syntax : lambda arg_list:expression
# f = lambda x,y : x*y


f = lambda x : 'IS_EVEN' if x%2==0 else 'NOT_EVEN'
print(f(90)) 

# lambda with filter
ip_list = [2,5,3,6,7,8]
even_list = list(filter(lambda x:x %2 ==0,ip_list))
print(even_list)


# lambda with map : change every value
square_numbers = list(map(lambda x: x**2,ip_list))
print(square_numbers)

# lambda with reduce

red_val = reduce(lambda a,b : ip_list[-1] + ip_list[-2] ,ip_list)
print(red_val)


fib_series = lambda number : number if number <= 1 else fib_series(number - 1) + fib_series(number - 2);

list_of = list(map(fib_series,range(0,6,1)))

print(list_of,"FIB USING MAP")


fib_series_reduce = lambda n : reduce(lambda x,_ : x  + [x[-1] + x[-2]],range(n-2),[0,1])
print(fib_series_reduce(8))

"""
# reverse a string

#syntax range:  range(start, stop, step)

input_string = "basav"
print(list(reversed(input_string)),"INBUILT FUNC")
print(input_string[::-1])

def reverse(input_string):
	i = len(input_string) -1
	rev_str = ''
	for x in input_string:
		rev_str = rev_str + input_string[i]
		print(input_string[i])
		i = i -1
	return rev_str


print(reverse(input_string))


input_strings = "hi basu how are you"
# print(list(reversed(input_strings.split())))

# for x in reversed(input_strings.split()):
# 	print(x)
reversed_char = []
for x in input_strings.split():
	reversed_char.append(x[::-1])
print(reversed_char)
"""




""" dictionary """

"""

# dict.pop(key, defaultvalue)


# The values of a dictionary can be of any type, but the keys must be of an immutable data type such as strings, numbers, or tuples.
input_dictionary = {"A":3,"B":2,"C":1}

sorted_keys = {x:dict_var[x] for x in sorted(dict_var.keys())}

sorted_values = {x:input_dictionary[x] for x in sorted(input_dictionary,key=input_dictionary.get,reverse=False)}
print(sorted_values)

def checkindictionary():
    dictionary = {'age1': 42, 'name1': 'Basavaraj', 'name2': 'dharwad'}

    print(dictionary.get("hello"))

    if 'place' in dictionary:
        place = dictionary['place']
    else:
        place = "its a default value"
    print(place, 'first approach')

    name = dictionary.get('name')
    print(name)

    if 'age' not in dictionary:
        dictionary['age'] = '20'
    print(dictionary['age'])

    dictionary.setdefault('name2', 'The Man with No Name')
    print(dictionary)
checkindictionary()

"""

tup = [('rishav', 10), ('akash', 5), ('ram', 20), ('gaurav', 15)] 
print(tup)
# tup.sort(key = lambda x:x[1])
tup =sorted(tup,key = lambda x: x[1])
print(tup)


