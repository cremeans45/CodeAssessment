"""
Please write a class in the language of your choice that contains the 
following two public methods:

aboveBelow
accepts two arguments
An unsorted collection of integers (the list)
an integer (the comparison value)
returns a hash/object/map/etc. with the keys "above" and "below" with the 
corresponding count of integers from the list that are above or below the 
comparison value

Example usage:

input: [1, 5, 2, 1, 10], 6

output: { "above": 1, "below": 4 }

stringRotation
accepts two arguments
a string (the original string)
a positive integer (the rotation amount)
returns a new string, rotating the characters in the original string to the right 
by the rotation amount and have the overflow appear at the beginning

Example usage:

input: "MyString", 2

output: "ngMyStri"

"""

class CodeAssessment:
    
    def aboveBelow(self, numList, comparator):
        """
        @param numList: The list of numbers to be iterated through
        @param comparator: The number to compare against the numbers in numList
        
        returns a dictionary with updated above and below comparator values
        """
        dictionary = {"above" : 0,
                      "below" : 0}
                      
        if numList:
            for number in numList:
                if number > comparator:
                    dictionary["above"] += 1
                if number < comparator:
                    dictionary["below"] += 1
                
        return dictionary
        
    def stringRotation(self, string, rotation):
        """
        @param string: the string passed in to be modified
        @param rotation: the index starting from the end to shift to 
                         the beginning of the new string.
                         
        returns the formatted string
        """
        ending    = string[-rotation:]
        beginning = string[:-rotation]
        formattedString = "{}{}".format(ending, beginning)
            
        return formattedString
 
 
nums = CodeAssessment()

print(nums.aboveBelow([1, 5, 2, 1, 10], 6))
print(nums.aboveBelow([1, 5, 2, 1, 10], 10))
print(nums.aboveBelow([1, 5, 2, 1, 10], 0))
print(nums.aboveBelow([], -1))

print(nums.stringRotation("MyString", 2))
print(nums.stringRotation("My String", 0))
print(nums.stringRotation("MyStr ing", 8))
print(nums.stringRotation("MyS tring", 4))
print(nums.stringRotation("", 4))




