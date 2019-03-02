class Solution:
    def getKth(self, A, B, k):
        '''
        得到两个序列中排名第ｋ个数
        :param A:
        :param B:
        :param k:
        :return:
        '''
        lenA = len(A)
        lenB = len(B)
        if lenA > lenB:
            return self.getKth(B, A, k)
        if lenA == 0:
            return B[k - 1]
        if k == 1:
            return min(A[0], B[0])
        pa = int(min(k / 2, lenA))
        pb = int(k - pa)
        if A[pa - 1] <= B[pb - 1]:
            return self.getKth(A[pa:], B, pb)
        else:
            return self.getKth(A, B[pb:], pa)

    def findMedianSortedArrays(self, nums1, nums2) -> float:
        '''
        这题还是比较有难度的，主要是有一种思路是合并两个序列找中位数，然而这样最快也要O((m+n)log(m+n))
        使用递归解法，略有理解难度，主要是一个二分查找思路
        :param nums1:
        :param nums2:
        :return:
        '''
        lenA = len(nums1)
        lenB = len(nums2)
        if lenA == 0:
            if lenB % 2 == 0:
                return (nums2[int(lenB/2)-1] + nums2[int(lenB/2)+1-1]) / 2
            else:
                return nums2[int(lenB/2)]
        if lenB == 0:
            if lenA % 2 == 0:
                return (nums1[int(lenA/2)-1] + nums1[int(lenA/2)+1-1]) / 2
            else:
                return nums1[int(lenA/2)]
        if (lenA + lenB) % 2 == 1:
            return self.getKth(nums1, nums2, (lenA + lenB) / 2 + 1)
        else:
            return (self.getKth(nums1, nums2, (lenA + lenB) / 2) + self.getKth(nums1, nums2, (lenA + lenB) / 2 + 1)) * 0.5
