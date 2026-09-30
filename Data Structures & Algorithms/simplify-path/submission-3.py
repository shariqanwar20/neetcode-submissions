class Solution:
    def simplifyPath(self, path: str) -> str:
        '''
            boolean to know if i have to reset curr or append to it
            - when changes from / to some other character, reset
            - when changes from .. to / -> pop, reset
            - when changes from some other character to / -> push, reset

            edge case: check when string finishes whatever is left in curr, handle "change from . to /"
            
        '''
        curr = "" # 

        stack = []
        for c in path + "/":
            if c != '/':
                if curr.endswith('/'):
                    # start of a possible folder
                    curr = c
                else:
                    # append to folder name
                    curr += c
            else:
                # c = "/"
                # if curr == '.':
                #     # refering to same folder
                #     curr = c
                if curr == "..":
                    if stack:
                        stack.pop()
                    
                elif curr and not curr.endswith('/') and curr != ".": 
                    stack.append(curr)
                curr = c
        
        # return "/" + "/".join(stack) -> most optimal way
        res = ""
        for folder in stack:
            res += "/" + folder
        
        return res if res else "/"
        