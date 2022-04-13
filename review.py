import random
data = [] # 先建一個空清單
count = 0 # 建立一個計算字數的variable

with open('reviews.txt', 'r') as f: 
	for line in f:
		data.append(line) # 讀檔案並且把每個 review 加到 data 清單
		count += len(line) # 每讀完一個 review 計算字數並且加總
		if len(data) % 100 == 0: # 每讀一百個review 印出來 review 總數
			print(len(data))
print() # 間隔
print('Total', len(data), 'reviews') # data清單 (review) 總數
print('Toatal', count, 'types') #字數總和
print('Average review types: ', count/len(data)) # 平均字數

r = random.randint(0, len(data)) # 從 data 清單總數隨機挑一個數字
print() # 間隔
print('Review', r, 'type count: ', len(data[r])) # 印出 哪一則 review 多少字數
print() # 間隔
print(data[r]) # 印出該 review

new = [] # 建一個篩選清單
for d in data: # 讀 data 清單並且把少於200字的 review 加到 new 清單
	if len(d) < 200:
		new.append(d)
print('Total', len(new), 'reviews have less than 200 words') # 印出 new 清單總和

great = [] # 建一個篩選清單
for d in data:
	if 'great' in d: # 讀 data 清單並且把有 great 字的 review 加到 great 清單
		great.append(d)
print() # 間隔
print('Total', len(great), 'reviews have the word great in it') # 印出 great 清單總和

x = random.randint(0, len(great))
print() # 間隔
print('review', x)
print() # 間隔
print(great[x])

if data[r] in great:
	print(data[r])