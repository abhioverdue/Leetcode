class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        n = len(board)
        dp = [[-1, 0] for _ in range(n)]

        for r in range(n - 1, -1, -1):
            next_dp = [[-1, 0] for _ in range(n)]
            for c in range(n - 1, -1, -1):
                if board[r][c] == "X":
                    continue
                
                if board[r][c] == "S":
                    next_dp[c] = [0, 1]
                    continue

                options = [
                    dp[c], 
                    dp[c + 1] if c + 1 < n else [-1, 0], 
                    next_dp[c + 1] if c + 1 < n else [-1, 0]
                ]
                max_val = max(opt[0] for opt in options)

                if max_val >= 0:
                    val = int(board[r][c]) if board[r][c] != "E" else 0
                    paths = sum(opt[1] for opt in options if opt[0] == max_val) % 1000000007
                    next_dp[c] = [max_val + val, paths]
            dp = next_dp

        return dp[0] if dp[0][0] >= 0 else [0, 0]