# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import collections

##删除排序数组中的重复项
nums0 = [0,0,1,1,1,2,2,3,3,4]
class Solution01:
    def removeDuplicates(self, nums: list) -> int:
        for i in range(len(nums) - 1, 0, -1):  #用逆序遍历避开数组长度变化
            if nums[i] == nums[i - 1]:
                del nums[i]
        return nums

'''**************************************************************************'''

##买卖股票的最佳时机 II
prices = [7,1,5,3,6,4]
class Solution02:
    def maxProfit(self, prices: list) -> int:
        buffer_list = []
        for i in range(0,len(prices)-1,1):
            if prices[i+1] > prices[i]:
                buffer_list.append(prices[i+1]-prices[i])
                #print(list1)  [4,3]
        return sum(buffer_list)   #踩坑：sum(list or arr),不可以是int等，所以sum(prices[i+1]-prices[i])无效

'''**************************************************************************'''

##旋转数组
nums2 = [1, 2, 3, 4, 5, 6, 7]
k2 = 3  #向右移动k位
class Solution03:
    def rotate(self, nums:list, k:int) -> None:
        if len(nums)>=k:
            k = k
        else:
            k = k%len(nums)  #防止出现k大于数组长度的情况
        #print(nums[len(nums) - k:])   [5, 6, 7]
        #print(nums[:len(nums) - k])   [1, 2, 3, 4]
        nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]
        return nums

'''**************************************************************************'''

#存在重复元素
nums3 = [2,14,18,22,22]
'''
leetcode超时，不允许暴力拆解
class Solution04:
    def containsDuplicate(self, nums: list) -> bool:
        for i in range(len(nums)-1) :
            for j in range(i+1,len(nums)):
                if nums[j] != nums[i]:
                    j+=1
                else:
                    return True
        return False
'''
class Solution04:
    def containsDuplicate(self, nums: list) -> bool:
        return len(nums) != len(set(nums))  #set去重对比长度是否一致

class Solution04:
    def containsDuplicate(self, nums: list) -> bool:
        #len(nums) == 1  考虑数组只有一个元素情况
        buffer_list = sorted(nums)         #sorted()排序后遍历对比
        for i in range(len(buffer_list)-1):
            if buffer_list[i] == buffer_list[i+1]:
                return True
            else:
                i+=1
        return False

class Solution04:
    def containsDuplicate(self, nums: list) -> bool:
        buffer_set = set()    #集合不能重复添加元素
        for i in nums:
            buffer_set.add(i)
            if len(buffer_set) == len(nums):
                return False
        return True

'''**************************************************************************'''

#只出现一次的数字
nums4 = [3,2,2,1,1,3,4]    #要考虑只有一个元素的情况[1]
class Solution05:
    def singleNumber(self, nums: list) -> int:
        buffer_list = sorted(nums)
        print (buffer_list)
        for i in range(len(buffer_list)-1):
            if buffer_list[i-1] != buffer_list[i] and buffer_list[i-1] !=buffer_list[i-2]:
                return buffer_list[i-1]
        return buffer_list[0]

class Solution05:         #官方答案：异或算法    例：a=10 b=76  a^b=70  a=0b1010  b=0b1001100  最后一位对齐，不同为1相同为0，0b1000110
    def singleNumber(self, nums: list) -> int:
        return reduce(lambda x, y: x ^ y, nums) #lambda ：前参数 ：后是表达式  reduce表示值从nums取
    '''
    任何数和0做异或运算，结果仍然是原来的数
    任何数和其自身做异或运算，结果是0
    异或运算满足交换律和结合律
    '''

'''**************************************************************************'''

#两个数组的交集
nums5 = [1,2,2,1,3]
nums6 = [2,2,3]
class Solution06:      #使用哈希表
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)    #判断nums长度，将长度短的数组放在前

        m = collections.Counter()    #collections创建一个hashmap，Counter是collections函数的统计key次数作为value
        buffer_list = list()
        for num in nums1:
            m[num] += 1
            #print(m)  #输出：Counter({2: 2, 3: 1})

        for num1 in nums2:
            count = m.get(num1, 0)  #获取nums2的元素在m，即nums1中出现的次数，如没有置为0
            #print(count)  #输出0 2 1 0 1
            if count > 0:                    #此处优化： if (count := m.get(num1, 0)) > 0,省略124行赋值运算
                buffer_list.append(num1)
                m[num1] -= 1   #自减1应对出现多次相同数值的情况
                if m[num1] == 0:
                    m.pop(num1)      #pop()函数删除列表中的元素，129&130行可省略，多判断一步为了避免出现负值运算
        return buffer_list


class Solution06:  #排序+双指针
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()

        buffer_list = list()
        index1 = index2 = 0
        while index1 < len(nums1) and index2 < len(nums2):
            if nums1[index1] < nums2[index2]:
                index1 += 1
            elif nums1[index1] > nums2[index2]:
                index2 += 1
            else:
                buffer_list.append(nums1[index1])
                index1 += 1
                index2 += 1
        return buffer_list

'''**************************************************************************'''

#加一  [1,2,3]>[1,2,4]  [0]>[1]  [1,2,9]>[1,3,0]
nums7 = [1,2,9,9]
class Solution07:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits)-1,-1,-1):   #end到-1 是因为考虑数组只有一个元素的情况,区间问题，避免[x]>[]
            if digits[i] != 9:   #不等于9就+1
                digits[i] += 1
                return digits    #跳出循环
            else:
                digits[i] = 0    #等于9变0，继续循环到非9的值+1
        return [1] + [0] *len(digits)  #全部为9的情况

'''**************************************************************************'''

#移动零
nums8 = [0,1,0,3,12]
class Solution08:   #暴力拆解，力扣超时，不推荐
    def moveZeroes(self, nums: list[int]) -> None:
        for i in range(0,len(nums)-1,1):
            for j in range(i,len(nums),1):
                if nums[i] == 0:
                    nums[i],nums[j] = nums[j],nums[i]
        return nums


class Solution08:   #双指针，非0数向左移动，0不动
    def moveZeroes(self, nums: list[int]) -> None:
        left = right = 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            else:
                pass
            right += 1
        return nums

class Solution08:   #双指针，for循环
    def moveZeroes(self, nums: list[int]) -> None:
        i =  0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
            j += 1
        return nums

'''**************************************************************************'''

#两数之和
nums9 = [1,2,11,15,7,16]
target = 9

class Solution09:  #暴力拆解
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]


class Solution09:  #hashmap
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashtable = dict()
        for index, num in enumerate(nums):    #enumerate()函数通常结合for循环使用，遍历列表/字符串等对象，获取其index/value作为字典的key/value
            if target - num in hashtable:     #判断target-x是否在字典中
                return [hashtable[target - num], index]    #返回target-x在nums中的位置和当前num的位置
            else:
                hashtable[nums[index]] = index   #将num的位置存放在dict中作为value，num作为key
        return []

'''**************************************************************************'''

#有效的数独
board =[["5","3",".",".","7",".",".",".","."]
       ,["6",".",".","1","9","5",".",".","."]
       ,[".","9","8",".",".",".",".","6","."]
       ,["8",".",".",".","6",".",".",".","3"]
       ,["4",".",".","8",".","3",".",".","1"]
       ,["7",".",".",".","2",".",".",".","6"]
       ,[".","6",".",".",".",".","2","8","."]
       ,[".",".",".","4","1","9",".",".","5"]
       ,[".",".",".",".","8",".",".","7","9"]]

class Solution10:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row = [set() for _ in range(9)]    #创建9长度的行
        #print(row)
        col = [set() for _ in range(9)]    #创建9长度的列
        #print(col)
        palace = [[set() for _ in range(3)] for _ in range(3)]   #创建3*3长度的九宫格二维数组
        #print(palace)

        for i in range(9):
            for j in range(9):       #逐行遍历每列
                ch = board[i][j]     #根据行列定位board中的元素值
                if ch == ".":
                    continue
                if ch in row[i] or ch in col[j] or ch in palace[i//3][j//3]:    #判断元素是否在行、列、九宫格中，如存在结束循环，//除法取整
                    return False
                row[i].add(ch)     #元素存入对应buffer行，后续对比
                col[j].add(ch)     #元素存入对应buffer列，后续对比
                palace[i//3][j//3].add(ch)   #元素存入对应buffer九宫格，后续对比

        return True

'''**************************************************************************'''

#旋转图像,顺时针旋转90°
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
class Solution11:     #对于矩阵中第i行的第j个元素，在旋转后，它出现在倒数第i列的第j个位置,即matrix[i][j] = matrix_new[j][len-i-1]
    def rotate(self, matrix: list[list[int]]) -> None:
        # Python 这里不能 matrix_new = matrix 或 matrix_new = matrix[:] 因为是引用拷贝
        matrix_new = [[0] * len(matrix) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix_new[j][len(matrix) - i - 1] = matrix[i][j]
        # 不能写成 matrix = matrix_new
        matrix[:] = matrix_new
        return matrix

class Solution11:    #矩阵中列变为行，在所在行直接把列内元素塞进去，然后把前面元素删除
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        for j in range(n - 1, -1, -1):
            for i in range(n - 1, -1, -1):       #这里逆序遍历不能改变，有顺序要求
                matrix[j].append(matrix[i][j])
        for i in range(n):
            del matrix[i][:n]
        return matrix

'''**************************************************************************'''



if __name__=='__main__' :
    '''
    print(Solution01().removeDuplicates(nums0))
    print(Solution02().maxProfit(prices))
    print(Solution03().rotate(nums2,k2))
    print(Solution04().containsDuplicate(nums3))
    print(Solution05().singleNumber(nums4))
    print(Solution06().intersect(nums5,nums6))
    print(Solution07().plusOne(nums7))
    print(Solution08().moveZeroes(nums8))
    print(Solution09().twoSum(nums9,target))
    print(Solution10().isValidSudoku(board))
    print(Solution11().rotate(matrix))
    '''

