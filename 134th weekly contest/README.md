# 题解
- Moving Stones Until Consecutive
	- 属于基础题。
	- 是一种空位变换题。
- Coloring A Border
	-  尝试使用BFS暴力遍历，只需要扫描一次即可。
	-  核心思路还是DFS或者BFS的扫描。
	-  注意边界不一定是棋盘边界而是颜色边缘。
- Uncrossed Lines
	- 很简单的一个DP题。
	- 第一行的前i个数和第二行的前j个数中最大连接数目。
		- dp[i][j] = dp[i-1][j-1] + (A[i] == B[j]) + dp[i-1][j] + dp[i][j-1]
- Escape a Large Maze
	- 看题的第一感觉是为什么又来了一道网格搜索。
	- 原来这一题的搜索范围很大很大，很容易TLE。
	- 但是blocked的大小最大不过200 * 200 / 2左右（19900）。