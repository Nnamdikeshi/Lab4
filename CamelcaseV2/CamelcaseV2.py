

def display_banner():
	'''Display program name in a banner'''
	msg = 'AWESOME camelCaseGenerater PROGRAM'
	stars = '*' * len(msg)
	print('\n', stars, '\n', msg, '\n', stars, '\n')

def instructions():
	'''Display game instructions'''
	instuct = "Enter a goofy sentence and it will be converted to camel case.\nEx: 'mY gAMe iS THE bEST'"
	print(instuct, '\n')
	
def camel_case(user_put):
	try:
	
		# Using the .title() function we capitalize each word
		capatalized = user_put.title()
		print ("Here's each word capitilized: ", capatalized)
		
		# Using the .split() function we join our string
		joined = ''.join(capatalized.split())
		print ("Here's your sentence joined: ", joined)
		
		# Lowercase the first letter in the string
		finish = joined[0].lower() + joined[1:]
		print ("Here's the sentence with the first letter lowercase: ", finish)
		return finish
	except TypeError:
		print("Oops! Thats not a valid sentence")
def main():
	
	display_banner()
	instructions()
	
	# Gather user sentence
	user_put = input("Type a sentence: ")
	finished = camel_case(user_put)
	
if __name__ == '__main__':
	main()