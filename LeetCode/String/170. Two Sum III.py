class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.appear = set([])

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.arr.append(number)
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        if len(self.arr)<2:
            return False
        if value in self.appear:
            return True
        
        check = set([])
        for i in range(len(self.arr)):
            if value - self.arr[i] in check:
                self.appear.add(value)
                return True
            check.add(self.arr[i])
            
        return False
        
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)