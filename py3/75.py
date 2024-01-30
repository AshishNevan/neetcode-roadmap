class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        curr_i = -1
        for i in range(len(matrix)):
            if matrix[i][0] <= target and matrix[i][-1] >= target:
                curr_i = i
                break
        if curr_i == -1:
            print("curr_i -1")
            return False

        def binary_search(l, r):
            if l > r:
                print("binary search err")
                return False
            mid = (l + r) // 2
            if matrix[curr_i][mid] == target:
                return True
            if matrix[curr_i][mid] < target:
                return binary_search(mid + 1, r)
            else:
                return binary_search(l, mid - 1)

        return binary_search(0, len(matrix[curr_i]) - 1)


sol = Solution()
print(sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
print(sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
print(sol.searchMatrix([[1, 3]], 3))
