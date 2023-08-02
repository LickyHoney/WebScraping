class Solution:
    def __init__(self, api):
        self.api = api
        print("Press run code to see this in the console!")
        # You can initiate and calculate things here

    def is_equal(self, str1, str2):
        """
        Task 1: Return if two strings are equal.
        
        :type str1: string
        :type str2: string
        
        :rtype: bool
        """
        # Write your code here
        
        if str1 == str2:
            return True
        else:
            return False

    def index_of_deviation(self, str1, str2):
        """
        Task 2: Return the first index at which 2 strings become unequal. If
        the strings do not deviate return the length of the string.
        
        :type str1: string
        :type str2: string
        
        :rtype: int
        """
        # Write your code here
        min_len = min(len(str1), len(str2))

        for i in range(min_len):
            if str1[i] != str2[i]:
                return i

        # If we reach this point, all characters up to min_len are the same
        # Check if one string is a prefix of the other
        if len(str1) != len(str2):
            return min_len

        # Both strings are of the same length and are identical
        return len(str1)
        

    def string_contains(self, str1, str2):
        """
        Task 3: Return a comma delimited, alphanumerically sorted, string of
        all the common characters between two strings. Whitespace and repeat
        characters should not be included.
        
        :type str1: string
        :type str2: string
        
        :rtype: string
        """
        # Write your code here
        # Create sets of characters for both strings
        set1 = set(char for char in str1 if char.isalnum())
        set2 = set(char for char in str2 if char.isalnum())

        # Find the common characters between the sets
        common_chars = set1.intersection(set2)

        # Sort the common characters alphanumerically
        sorted_chars = sorted(common_chars)

        # Convert the sorted characters to a comma-delimited string
        result = ",".join(sorted_chars)

        return result
        