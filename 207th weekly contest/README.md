# 题解

## Rearrange Spaces Between Words
送分题，解法题目中已经有了，一个除法确定单词间空格数目，一个取余确定最末尾空格的数目。

## Split a String Into the Max Number of Unique Substrings
比较基础的一道字符串分割，回溯搜索即可。

## Maximum Non Negative Product in a Matrix
这种网格最优解得到搜索首选思路就是DP，这题由于乘法所以要考虑到符号陡变性，因此需要维护两个DP数组来搜索，明白这点，本题并不难。

## Minimum Cost to Connect Two Groups of Points
主要思路就是先将组1的结点连接到组2，每个结点只出发一条边，然后对组2中每一个结点以最小代价连接到组1中。通过DP和bitmask可以方便实现这个思路。