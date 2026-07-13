class Solution:
    def sequentialDigits(self, low, high):
        digits = "123456789"
        result = []
        
        for length in range(2, 10):  # window sizes from 2 to 9
            for start in range(0, 10 - length):
                num = int(digits[start:start + length])
                if low <= num <= high:
                    result.append(num)
        
        return sorted(result)