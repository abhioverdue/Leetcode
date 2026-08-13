class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        n = len(s)
        tree = [None] * (4 * n)
        s_list = list(s)

        def merge(left, right):
            if not left:
                return right
            if not right:
                return left
            
            lc, lrc, llen, lp, ls, lb = left
            rlc, rc, rlen, rp, rs, rb = right
            
            length = llen + rlen
            
            prefix = lp
            if lrc == rlc and lp == llen:
                prefix = llen + rp
                
            suffix = rs
            if lrc == rlc and rs == rlen:
                suffix = rlen + ls
                
            best = max(lb, rb)
            if lrc == rlc:
                best = max(best, ls + rp)
                
            return [lc, rc, length, prefix, suffix, best]

        def build(node, start, end):
            if start == end:
                char = s_list[start]
                tree[node] = [char, char, 1, 1, 1, 1]
                return
            
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            tree[node] = merge(tree[2 * node], tree[2 * node + 1])

        def update(node, start, end, idx, char):
            if start == end:
                tree[node] = [char, char, 1, 1, 1, 1]
                return
            
            mid = (start + end) // 2
            if idx <= mid:
                update(2 * node, start, mid, idx, char)
            else:
                update(2 * node + 1, mid + 1, end, idx, char)
                
            tree[node] = merge(tree[2 * node], tree[2 * node + 1])

        build(1, 0, n - 1)
        
        answer = []
        for char, idx in zip(queryCharacters, queryIndices):
            if s_list[idx] != char:
                s_list[idx] = char
                update(1, 0, n - 1, idx, char)
            answer.append(tree[1][5])
            
        return answer