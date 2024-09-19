class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = map(str, nums) #convert integer to strings

        def compare(a: str, b:str) -> int: #define a comparison function
            if a+b < b+a:
                return 1
            elif a+b > b+a:
                return -1
            else:
                return 0
        
        sorted_nums = sorted(str_nums, key=cmp_to_key(compare)) #sorted the string number using ths comparison function

        return "0" if sorted_nums[0] == "0" else "".join(sorted_nums) # Join sorted numbers or return "0" if the result is leading zeroes

        #Time Complexity =  O(n⋅m⋅logn)
        #Space Complexity = O(n⋅m)