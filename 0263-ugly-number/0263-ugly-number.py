class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 1:
            return True
        if n <= 0:
            return False

        p_fs = [2,3,5]

        while n > 1:
            if n % 2 != 0  and n % 3 != 0 and n % 5 != 0:
                return False


            if n % 2 == 0:
                n = n //2
            if n % 3 == 0:
                n = n // 3
            if n % 5 == 0:
                n = n // 5
        return True






        # n_d = {}
        # for i in range(len(p_fs)):
        #     if n % p_fs[i] == 0:
        #         n_d[p_fs[i]] = 1
        #         tempN = n
        #         while (tempN // p_fs[i]) % p_fs[i] == 0:
        #             n_d[p_fs[i]] += 1
        #             newN = tempN // p_fs[i]
        #             tempN = newN

        # val = 1
        # for key, value in n_d.items():
        #     val *= key ** value 
        # return val == n

        