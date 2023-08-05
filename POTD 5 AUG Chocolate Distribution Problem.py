class Solution:

    def findMinDiff(self, A, N, M):
        A = sorted(A)
        i = 0
        mini = float("inf")

        while i <= N - M: 
            c = A[i + M - 1] - A[i]
            mini = min(mini, c)
            i += 1

        return mini
