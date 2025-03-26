# 2517ms / 19.24MB
from collections import Counter, defaultdict
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        result = 0

        while True:
            sub_count = 0
            for task, _ in counter.most_common(n + 1):
                sub_count += 1
                result += 1

                counter.subtract(task)
                counter += Counter()

            if not counter:
                break

            result += n - sub_count + 1

        return result


class Solution2:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        counter = Counter(tasks)
        interval = defaultdict(int)
        while len(counter) > 0:
            # task
            for x in counter.most_common():
                task = x[0]
                if interval[task] == 0:
                    interval[task] = n + 1
                    counter[task] -= 1
                    if counter[task] == 0:
                        del counter[task]
                    break
            # interval
            for key, val in interval.items():
                if val != 0:
                    interval[key] -= 1
            time += 1
        return time
