class Solution:
    def average(self, salary: List[int]) -> float:
        min_sal=min(salary)
        max_sal=max(salary)

        sum_ex=sum(val for val in salary if val!=min_sal and val!=max_sal)

        average=sum_ex/(len(salary)-2)
        return average