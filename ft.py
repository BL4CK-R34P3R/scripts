import os

def delete_line(original_file, line_number):
	is_skipped = False
	current_index = 0
	dummy_file = original_file + '.bak'

	with open(original_file, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
		for line in read_obj:
			if current_index != line_number:
				write_obj.write(line)
				print(line)
				current_index += 1
			else:
				is_skipped = True
				current_index += 1

			

	if is_skipped:
		os.remove(original_file)
		os.rename(dummy_file, original_file)
	else:
		os.remove(dummy_file)


s_username = input('username: ')
s_social = input('social media name:')
find = 0
flag = 0
upto = 0
index = 0
sf=open('password.txt','r')

for line  in sf:
	find += 1
	if s_username in line and s_social in line:
		flag = find - 1
		upto = flag + 2
		index = 1
		print(find)
		print(flag)
		print(upto)
		print(index)
		#delete_line('password.txt',upto)
if index == 0 :
	print("credentials does not exist in logs")