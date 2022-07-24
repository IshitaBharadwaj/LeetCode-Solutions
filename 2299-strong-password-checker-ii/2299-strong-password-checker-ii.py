import re
class Solution(object):
    
    def strongPasswordCheckerII(self, password):
        """
        :type password: str
        :rtype: bool
        """

        if len(password)>=8 and any(l.isupper() for l in password) and any(l.islower() for l in password) and any(l.isdigit() for l in password) and any(not l.isalnum() for l in password):
            for i in range(len(password)-1):
                if password[i]==password[i+1]:
                    return False
            return True
        return False
        