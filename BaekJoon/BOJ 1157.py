from collections import Counter
word=input().upper()
counter = Counter(word)

max_counter=-1
for letter in counter:
    if(counter[letter]>max_counter):
        max_counter=counter[letter]
cnt=0
for letter in counter:
    if(cnt==0 and counter[letter]==max_counter):
        max_counter_letter=letter
        cnt+=1
    elif(cnt==1 and counter[letter]==max_counter):
        max_counter_letter="?"
        break
    
print(max_counter_letter)
    
    
