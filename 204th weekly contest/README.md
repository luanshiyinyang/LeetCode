# 题解

## Detect Pattern of Length M Repeated K or More Times

因为题目中限制pattern必须是连续的，所以只需要一次遍历即可。

## Maximum Length of Subarray With Positive Product

我这边采用的其实是DP的思路，维护一个最大正积和最大负积即可。

## Minimum Number of Days to Disconnect Island

这道题的难点在于，最多两天就可以断开任何给定的岛屿。

在第0天，只需要检查是否少于或者多于一个岛，是的话返回0；第1天，不是的话任一位置放水，看是否满足条件；第2天，直接返回2。

参考自[链接](https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/discuss/819303/Python-you-need-at-most-2-days) 。

## Number of Ways to Reorder Array to Get Same BST
分治思路：
1. 对每个数组，第一个元素一定是根，然后插入左子树和右子树
2. 对两个子树，首先也是插入根；
3. 当我们已经知道了安排左子树和右子树的方法数目的时候，仅仅需要计算如何将它们安排进一个数组里而不改变子数组的原始元素相对位置。

参考[链接](https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/discuss/820263/Python3-Divide-and-Conquer-or-detailed-explanation)。