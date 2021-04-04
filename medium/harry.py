"""The median of a set of integers is the midpoint value of the data set for which an equal number of integers are less than and greater than the value.
To find the median, you must first sort your set of integers in non-decreasing order, then:

If your set contains an odd number of elements, the median is the middle element of the sorted sample. In the sorted set , is the median.
If your set contains an even number of elements, the median is the average of the two middle elements of the sorted

Given an input stream of integers, perform the following task for each integer:

Add the  integer to a running list of integers.
Find the median of the updated list (i.e., for the first element through the element).
Print the updated median on a new line. The printed value must be a double-precision number scaled to  decimal place (i.e.,  format).
"""

# [1,2,3,4, 5]
# [5]

# []
# 2 -> 2

# [2]
# 3

# [2,3] 2.5
# 1 


# [1,2,3,4,6], 

# [1,2,3,4,6,5] 3
# [1,2,3,4,5,6] 2 -> len 6,  [2:4]
# [1,2,3,4] -> [1:3

# 7

# [4, 5, 6, 7] # 
# [3, 2, 2, 1] # 

# [4,2,5,1]

# [4, 5]
# [2, 1]

class Median:
    def __init__(self, lst=[]):
        self.lst = lst
        self.median = None
    
    def get_median(self, val):
        # Return the current median of self.lst
        if self.lst == []:
            self.lst.append(val)
            self.median = val
            return val
        if val > median:
            self.lst.append(val)
            i = len(self.lst)
            while i > 0: # edge cases
                if self.lst[i-1] > self.lst[i]:
                    self.lst[i-1], self.lst[i] = self.lst[i], self.lst[i-1]
                    i -= 1
                else:
                    break

        if val <= median: # edge cases
            self.lst = [val] + self.lst
            while i < len(self.lst)-1:
                if self.lst[i+1] < self.lst[i]:
                    self.lst[i], self.lst[i+1] = self.lst[i+1], self.lst[i]
                    i += 1
                else:
                    break
        
        self.median = self._current_median()
        return self.median

    def _current_median(self):
        l = len(self.lst)
        if l % 2 == 1:
            return self.lst[l//2]
        return sum(self.lst[l//2-1: l//2+1])/2