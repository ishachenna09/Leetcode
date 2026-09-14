class Solution:
    def maxVowels(self, s: str, k: int) -> int: 
        vowels = {'a','e','i','o','u'}
        wi = s[:k]
        vc = 0
        mvc = 0
        l=0
        for i in wi:
            if i in vowels:
                vc+=1
        mvc = vc
        # print(f"fist mvc{mvc}\n first vc{vc}")
        i=0
        for j in range(k, len(s)):
            if s[l] in vowels:
                if vc>0:
                    vc-=1
            if s[j] in vowels:
                vc+=1
                 
            # wi = s[l:j+1]
            mvc = max(mvc,vc)
            l+=1
            if mvc ==k:
                return mvc    
        return mvc
            # print("mvc", mvc)
            # print(f"{l}=>{j} window ", wi)
            # print("s[j]",s[j]) novowels
              



        



        