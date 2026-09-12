class Solution:
    def getSum(self, a: int, b: int) -> int:
        def get_binary(n : int):
            return bin(n)[2:]
        carry = 0
        if a<0 or b<0:
            return a+b
        bin_a = get_binary(a)
        bin_b  = get_binary(b)
        n =  max(len(bin_a),len(bin_b))
        ans = [-1]*32
        bin_a = "0"*(32-len(bin_a))+bin_a
        bin_b = "0"*(32-len(bin_b))+bin_b

        print(bin_a, bin_b,n)
        for i in range(len(bin_a)-1,-1, -1):
            
            if bin_a[i] == bin_b[i] == '1':
                if carry and int(bin_a[i]) + int(bin_b[i]) + carry >=2:
                    ans[i] = "1"
                else:
                    carry = 1
                    ans[i] = "0"
            elif carry and int(bin_a[i]) ^ int(bin_b[i]):
                    ans[i] = "0"
            elif carry:
                    ans[i] = "1"
                    carry = 0
            else:
                ans[i] = str(int(bin_a[i]) | int(bin_b[i]))
                    

        if carry:
            return int("".join(["1"]+ans),2)
        else:
            return int("".join(ans),2)
