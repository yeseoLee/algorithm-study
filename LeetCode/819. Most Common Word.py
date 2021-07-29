"""
import re
from collections import Counter
def mostCommonWord(paragraph, banned):
    words=list(re.sub(r'[^\w]', ' ', paragraph).lower().split())
    counter=Counter()
    for word in words:
        if(word not in banned):
            counter[word]+=1
    print(counter)


mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",["hit"])
"""    

import re
from collections import Counter
def mostCommonWord(paragraph, banned):
    words= [word for word in re.sub(r'[^\w]', ' ', paragraph)
        .lower().split() if word not in banned]
    
    counter=Counter(words)
    return counter.most_common(1)[0][0]


print(mostCommonWord(
    "Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
