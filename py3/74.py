class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        def binary_search(l, r):
            if l > r:
                return False
            mid = (l + r) // 2
            ele = matrix[mid // n][mid % n]
            if ele == target:
                return True
            if ele > target:
                return binary_search(l, mid - 1)
            else:
                return binary_search(mid + 1, r)

        return binary_search(0, (n * m) - 1)


sol = Solution()
print(sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
print(sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
print(sol.searchMatrix([[1, 3]], 1))
print(sol.searchMatrix([[1]], 1))
print(sol.searchMatrix([[1, 1]], 2))
