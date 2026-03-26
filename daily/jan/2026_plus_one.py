class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry_val = 1
        for idx in range(len(digits) - 1, -1, -1):
            total = digits[idx] + carry_val
            digits[idx] = total % 10
            carry_val = total // 10

        if carry_val:
            digits = [1] + digits

        return digits 
