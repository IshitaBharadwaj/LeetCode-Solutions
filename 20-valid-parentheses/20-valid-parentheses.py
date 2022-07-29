class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        n=len(s)
        for i in range(n):
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                stack.append(s[i])
            elif s[i]==')':
                if len(stack)!=0 and stack.pop()=='(':
                    continue
                else:
                    return False
            elif len(stack)!=0 and s[i]=='}':
                if stack.pop()=='{':
                    continue
                else:
                    return False
            else:
                if len(stack)!=0 and stack.pop()=='[':
                    continue
                else:
                    return False
        if len(stack) !=0:
            return False
        return True