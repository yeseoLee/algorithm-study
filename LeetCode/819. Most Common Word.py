from collections import Counter
import re
from types import List


def mostCommonWord(paragraph, banned):
    words = [
        word
        for word in re.sub(r"[^\w]", " ", paragraph).lower().split()
        if word not in banned
    ]

    counter = Counter(words)
    return counter.most_common(1)[0][0]


print(
    mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
)


# 1 ms / 17.54 MB
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub("[!?',;.]", " ", paragraph)
        paragraph = paragraph.lower()
        words = paragraph.split()

        counter = Counter(words)
        for word, _ in counter.most_common():
            if word not in banned:
                return word
