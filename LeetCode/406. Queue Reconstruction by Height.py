from typing import List


# 0ms / 18.42MB
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        results = []
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        for person in people:
            results.insert(person[1], person)
        return results
