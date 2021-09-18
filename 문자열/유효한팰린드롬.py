from _collections import deque

input_string = input()

class Solution:
    def isPalindrome1(self, s: str) -> bool:
        strs = []
        for char in strs:
            if char.isalnum():
                strs.append(char.lower())

        while len(s) > 1:
            if strs.pop(0) != strs.pop():
                return False
        return True

    def isPalindrome2(self, s: str) -> bool:
        strs : deque = deque()

        for char in strs :
            if char.isalpha():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop:
                return False
        return True

print(Solution.isPalindrome1(input_string))

print(Solution.isPalindrome2(input_string))