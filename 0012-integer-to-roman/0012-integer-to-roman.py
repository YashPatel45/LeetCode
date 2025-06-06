class Solution:
    def intToRoman(self, num: int) -> str:
        n_d = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }
        result = ''

        for k, v in sorted(n_d.items(), reverse=True):
            while num >= k:
                
                if num == 4 or num == 9:
                    result += n_d[num]
                    num -= num
                else:
                    num -= k
                    result += v

        return result