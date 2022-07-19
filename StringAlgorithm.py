import collections
from functools import wraps

#反转字符串
s1 = ["h","e","l","l","o"]

class Solution01:    #切片
    def reverseString(self, s: list[str]) -> None:
        s[:] = s[::-1]
        return s

class Solution01:   #双指针
    def reverseString(self, s: list[str]) -> None:
        left = 0
        for right in range(len(s)-1,-1,-1):
            if left <= right:
                s[right],s[left] = s[left],s[right]
            else:
                break
            left +=1
        return s



'''**************************************************************************'''

#反转整数
x = -123654
class Solution02:    #转换字符串切片
    def reverse(self, x: int) -> int:
        str_x = str(x)
        if str_x[0] != '-':
            x = str_x[::-1]
        else:
            x1 = str_x[:0:-1]
            x = -int(x1)
        if int(x) < -2**31 or int(x) > 2**31-1:
            return 0
        return int(x)


class Solution02:    #取模
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1

        rev = 0
        while x != 0:
            # INT_MIN 也是一个负数，不能写成 rev < INT_MIN // 10
            if rev < INT_MIN // 10 + 1 or rev > INT_MAX // 10:
                return 0
            digit = x % 10
            # Python3 的取模运算在 x 为负数时也会返回 [0, 9) 以内的结果，因此这里需要进行特殊判断
            if x < 0 and digit > 0:
                digit -= 10

            # 同理，Python3 的整数除法在 x 为负数时会向下（更小的负数）取整，因此不能写成 x //= 10
            x = (x - digit) // 10
            rev = rev * 10 + digit

        return rev

'''**************************************************************************'''

#字符串中的第一个唯一字符
s2 = "leetcode"
class Solution03:
    def firstUniqChar(self, s: str) -> int:
        buffer_dict = collections.Counter()       #66~68行buffer_dict = collections.Counter(s)可以这样写，入参本质也是遍历
        for i in s:
            buffer_dict[i] += 1
        for i in range(len(s)):
            if buffer_dict[s[i]] == 1:
                return i
        return -1

'''**************************************************************************'''

#有效的字母异位词，即每个字母出现次数一样
s3 = "anagram"
s4 = "nagaram"
class Solution04:  #排序对比
    def isAnagram(self, s: str, t: str) -> bool:
        s,t= sorted(s),sorted(t)
        if s==t:
            return True
        return False

class Solution04:   #哈希计数对比
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)

class Solution04: #计数器，s存在+1，t存在-1，len=0返回true
    def isAnagram(self, s: str, t: str) -> bool:
        buffer_map = collections.Counter()
        for i in s:
            buffer_map[i] += 1
        for j in t:
            buffer_map[j] -= 1
            if buffer_map[j] ==0:
                del buffer_map[j]
                print(buffer_map)
        return True if len(buffer_map) == 0 else False

'''**************************************************************************'''

#验证回文串
s5 = "A man, a plan, a canal: Panama"
class Solution05:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(ch.lower() for ch in s if ch.isalnum() is True)  #""join()表示拼接入参，lower()转小写，isalnum()判断是否为字母和数字
        left, right = 0,len(s)-1
        while left <= right :
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True


'''**************************************************************************'''

##装饰器：封装一个函数，并且用这样或者那样的方式来修改它的行为，即a_function_requiring_decoration在a_new_decorator中被重写
def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("my name is ")
        a_func()
        print("nice to meet you!")
    return wrapTheFunction

def a_function_requiring_decoration(*args):
    return print("wangning")

#a_function_requiring_decoration()
#a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
#a_function_requiring_decoration()

@a_new_decorator
def a_function_requiring_decoration(*args):
    return print("wangning")


if __name__== '__main__':
    '''
    print(Solution01().reverseString(s1))
    print(Solution02().reverse(x))
    print(Solution03().firstUniqChar(s2))
    print(Solution04().isAnagram(s3,s4))
    print(Solution05().isPalindrome(s5))
    '''
    print(a_function_requiring_decoration())
    print(a_function_requiring_decoration.__name__)






