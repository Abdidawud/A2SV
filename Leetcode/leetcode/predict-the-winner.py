class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def predict(nums, score1, score2, turn):
            if len(nums) == 0:
                return score1 >= score2

            if turn == 0:
                return predict(nums[1:], score1 + nums[0], score2, 1) or predict(nums[:-1], score1 + nums[-1], score2, 1)
            return predict(nums[1:], score1, score2 + nums[0], 0) and predict(nums[:-1], score1, score2 + nums[-1], 0)
        
        return predict(nums, 0, 0, 0)