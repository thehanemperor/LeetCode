# MEDIUM
# maintain a Bool for state of CommentBlock
#         if the CommentBlock is open, we ignore every char till we find a close tag
# 1. be aware of /* //.  read "//" as common char when commentBlock is open 
# 2. be aware of case as:
#         int a = 1;/*
#             this is comment*/int b = 2;
#         when we get rid of comments. those codes should be in the same line

# Time O(N) Space O(N)

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        for s in source:
            print(s)
        commentOpen = False
        result = []
        for chunk in source:
            if not commentOpen:
                curr = []
            i = 0
            while i < len(chunk):
            
                if i+1 < len(chunk) and chunk[i] =="/" and chunk[i+1] =="*" \
                    and not commentOpen:
                    commentOpen = True
                    i+=1
                elif i+1 < len(chunk) and chunk[i] =="*" and chunk[i+1] =="/" \
                    and  commentOpen:
                    i+=1
                    commentOpen = False
                elif i+1 < len(chunk) and chunk[i]=="/" and chunk[i+1] =="/"\
                    and not commentOpen:
                    #skip line
                    break
                   
                    
                elif not commentOpen :
                    curr.append(chunk[i])
                    
                
                i+=1
            if curr and not commentOpen:
                result.append("".join(curr))
        return result
           
                