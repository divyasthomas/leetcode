class Solution:
    def containsDuplicate(self,nums:list[int])->bool:
        hashset = set()
        for ele in nums:
            if ele in hashset:
                return True
            else:
                hashset.add(ele)
        
        return False


def main():

    solution = Solution()
    
    while True:
        try:

            userInput = input('Enter numbers to check separated by comma: ')
            userlist = list(map(int,userInput.split(',')))
            break
        except ValueError:
            print("Invalid input. Please enter again")
    
    print(f"This list of numbers which are {userlist} contains duplicates: {solution.containsDuplicate(userlist)}")



if __name__=="__main__":
    main()