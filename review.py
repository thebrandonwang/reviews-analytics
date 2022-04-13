import random
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += len(line)
		if len(data) % 100 == 0:
			print(len(data))
print('Toatal', count, 'types') 
print('Average review types: ', count/len(data))	
r = random.randint(1, len(data))
print()
print('Review', r)
print(data[r])