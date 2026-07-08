class Solution:

    def sumAndMultiply(
        self, s: str, queries: list[list[int]]
    ) -> list[int]:
        MOD = 10**9 + 7

        nz_vals, nz_idx = [], []
        pref_sum, pref_val = [0], [0]

        for i, ch in enumerate(s):
            if ch != "0":
                v = int(ch)
                nz_vals.append(v)
                nz_idx.append(i)
                pref_sum.append(pref_sum[-1] + v)
                pref_val.append((pref_val[-1] * 10 + v) % MOD)

        pow10 = [1]
        for _ in range(len(nz_vals) + 1):
            pow10.append((pow10[-1] * 10) % MOD)

        ans = []
        for L, R in queries:
            ql = bisect.bisect_left(nz_idx, L)
            qr = bisect.bisect_right(nz_idx, R)

            if ql >= qr:
                ans.append(0)
            else:
                x = (pref_val[qr] - pref_val[ql] * pow10[qr - ql]) % MOD
                s_digits = pref_sum[qr] - pref_sum[ql]
                ans.append((x * s_digits) % MOD)

        return ans