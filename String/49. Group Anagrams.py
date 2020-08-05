# MEDIUM 
# create a Dict with key => (a:count, b:count ,,,z:count) | value => [list[index]]
#     loop the list and find same pattern and save to Dict 
#     add each value of Dict to result 

# Time O(N^2) Space O(N)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = defaultdict(list)
        for s in strs:
            tmp = [0 for _ in range(26)]
            for c in s:
                tmp[ord(c)- ord('a')]+=1
            tu = tuple(tmp)
            check[tu].append(s)
            
        result = []
        for k,v in check.items():
            result.append([*v])
         
        return result
        print(result)