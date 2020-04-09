import random
from matplotlib import pyplot as plt
%matplotlib inline

def page_printer(data, start=0, screen_lines=0, pager_cmd=None):
    if isinstance(data, dict):
        data = data['text/plain']
    print(data)

import IPython.core.page
IPython.core.page.page = page_printer

def find_ternary(num):  #2
    quotient = num/3    #3
    remainder = num%3
    if quotient == 0:   #4
        return ""
    else:
        return find_ternary(int(quotient)) + str(int(remainder))



def initi(rule_number, length, time):
	'''
	This needd rule_number, length, time

	'''

	# make the initial condition
	initial_condition = []
	for i in range(length):
    	initial_condition.append(random.randint(0,2))

	neighborhoods=[]
	for i in range(2+1):
    	for j in range(2+1):
        	#for k in range(2+1):
        	n=(i,j)
            #n1=[n]
        	neighborhoods.append((n))

return initial_condition, neighborhoods


def vocabulary(rule_number):
	in_binary = find_ternary(rule_number)
	binary_length = len(in_binary)
	if binary_length != len(neighborhoods):
    	padding = 9 - binary_length
    	in_binary = in_binary + '0'*padding

# create the lookup table dictionary
	lookup_table = {}
	for i in range(len(neighborhoods)):
    	key = neighborhoods[i]
    	val = in_binary[i]
    	lookup_table.update({key:val})
   return lookup_table

def space_time(time, length, initial_condition, lookup_table):
	# initialize spacetime field and current configuration
	spacetime_field = [initial_condition]
	current_configuration = initial_condition.copy()
	print(current_configuration[-1])
# apply the lookup table to evolve the CA for the given number of time steps
	for t in range(time):
    	new_configuration = []
    	for i in range(len(current_configuration)):
        
        	neighborhood = (current_configuration[(i-1)%length], current_configuration[i])
        	print(neighborhood)
    
# print(current_configuration)

        new_configuration.append(int(lookup_table[neighborhood]))
        
    current_configuration = new_configuration
    spacetime_field.append(new_configuration)
	