'''
©Noah Gergel, Sichun Xu, Weilin Qiu, Jacqueline Yang, Nina Yang 2019
Uses a MIT licence; see LICENCE file for more information.

Program that when given a time will tell you of all free
classrooms at Ualberta in Winter 2019.
'''

# Import statements.
from time_calc import time_compare

# master = {
# 	'(CAB 235)': [['R', '10:00:00', '10:50:00'], ['R', '12:30:00', '13:50:00'], ['M', '10:00:00', '11:50:00']],
# 	'(ETLC 2 002)': [['R', '10:00:00', '10:50:00'], ['R', '12:00:00', '12:50:00']],
# 	'(CCIS L1 160)': [['W', '9:00:00','10:50:00'], ['F', '11:00:00', '12:50:00']],
# 	'(CCIS L1 161)': [['W', '10:00:00','12:50:00'], ['F', '11:00:00', '12:50:00']],
# 	'(CAB L1 162)': [['W', '12:00:00','12:50:00'], ['F', '11:00:00', '12:50:00']],
# 	'(CAB L1 163)': [['W', '10:00:00','12:50:00'], ['F', '11:00:00', '12:50:00']],
# 	'(CCIS L1 164)': [['W', '10:00:00','12:50:00'], ['F', '11:00:00', '12:50:00']],
# 	'(CCIS L1 165)': [['W', '7:00:00','7:50:00'], ['F', '11:00:00', '12:50:00']],
# 	'(CCIS L1 166)': [['W', '13:00:00','13:50:00'], ['F', '11:00:00', '12:50:00']],
# 	'(CCIS L1 167)': [['W', '10:00:00','12:50:00'], ['F', '11:00:00', '12:50:00']],
# 	'(CCIS L1 168)': [['W', '14:00:00','14:50:00'], ['F', '11:00:00', '12:50:00']],
# 	'(ED N1 L1 169)': [['W', '10:00:00','12:50:00'], ['F', '11:00:00', '12:50:00']],
# 	'(CCIS L1 170)': [['W', '15:00:00','15:50:00'], ['F', '11:00:00', '12:50:00']],
# 	'(CCIS L1 171)': [['W', '16:00:00','16:50:00'], ['F', '11:00:00', '12:50:00']]
# }

f = open('newmaster_dict.txt', 'r')
data = f.read()
exec('master = '+data)

# Introduction and getting user input.
print('What Rooms Are Free?')
print('--------------------------------------------')
print('Please write a time in the form `hh:mm:ss` :')
given_time = input()
print('And what day are you checking for? (M/T/W/R/F)')
given_day = input()
print('And what building do you want? (If all, just hit enter.)')
print('If the building name has 2 words, just input the first one.')
print('For example, instead of `ED N1`, just write `ED`.')
given_building = input()
print('--------------------------------------------\n')

# Main program.
def main():
	# Initialize list to populate with rooms that are filled.
	filled_rooms = []

	# Populate the above list.
	for i in master.keys():
		for j in master[i]:
			if given_day == j[0] and time_compare(given_time, j[1], j[2]):
				filled_rooms.append(i)

	# Even if they are not filled, add rooms not in the building specified
	# to get them removed.
	for i in master.keys():
		if given_building != '' and i.split()[0][1:] != given_building:
			filled_rooms.append(i)

	empty = list(set(master.keys())-set(filled_rooms))
	
	# Print empty rooms.
	print('The rooms that are free are:')

	for i in range(len(empty)):
		if i == len(empty)-1:
			print(empty[i])
		elif i % 7 == 6:
			print(empty[i]+',')
		else:
			print(empty[i]+', ', end='')



# Verify this file is being run directly.
if __name__ == '__main__':
	main()