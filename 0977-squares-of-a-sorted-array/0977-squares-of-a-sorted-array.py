class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        positive = []
        negative = [] 
        res=[]
        for num in nums:
            if num<0:
                negative.append(num)
            else:
                positive.append(num)
        # print(positive,negative)
        if len(positive)<=0:
            res=[x*x for x in negative][::-1]
            return res
        if len(negative) <=0:
            res =[x*x for x in positive]
            return res

        positive = [x*x for x in positive]    
        negative = [x*x for x in negative][::-1]

        i=0
        j=0
        res=[]
        while i<len(positive) and j <len(negative):
            if positive[i] <= negative[j] :
                res.append(positive[i])
                i+=1
            else:
                res.append(negative[j])
                j+=1
        while i<len(positive):
            res.append(positive[i])
            i+=1
        while j < len(negative):
            res.append(negative[j])
            j+=1
            
        return res    
        # print(positive, negative)
        # print(res)

        
        
        