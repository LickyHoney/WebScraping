import re

larger_string = "This is a larger string containing a substring."
substring = "larger string"

# Use regex to find the matched part
match = re.search(substring, larger_string).group(0)

if match:
    matched_part = match
    print("Matched part:", matched_part)
else:
    print("Substring not found!")

    def is_equal(self, str1, str2):
        """
        Task 1: Return if two strings are equal.
        
        :type str1: string
        :type str2: string
        
        :rtype: bool
        """
        # Write your code here
        
        
        if self.str1 == self.str2:
            return True
        else:
            return False