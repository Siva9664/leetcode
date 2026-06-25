class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = [0]*26
        c2 = [0]*26
        w = len(s1)

        if w > len(s2):
            return False

        for i in s1:
            c1[ord(i)-97]+=1
        

        
        for i in range(w):
            c2[ord(s2[i])-97]+=1
            
            if c1 == c2:
                return True


        for i in range(w,len(s2)):
            c2[ord(s2[i-w])-97]-=1
            c2[ord(s2[i])-97]+=1



            if c1 == c2:
                return True

        return False
