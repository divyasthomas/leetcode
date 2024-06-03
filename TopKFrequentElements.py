class Solution:
    def topkFreqElem(self, nums:list[int], k:int)->list[int]:
        countDict = {}

        for ele in nums:
            countDict[ele] = countDict.get(ele,0) + 1

        freqList = [[] for _ in range(len(nums)+1)]

        for key, value in countDict.items():
            freqList[value].append(key)
        # print(freqList)
        result = []
        for idx in range(len(freqList)-1,-1,-1):
            if freqList[idx]:
                result.extend(freqList[idx])
                # print(f'result is {result}')

            
            if len(result) >= k:
                return result[:k]

# "",'',None,False,[]

# def isValidElement(e):
#     if e is not None and isinstance(e, str) and e.isdigit() and e.isnumeric():
#         return int(e)
#     else:
#         raise ValueError(f"element {e} is not valid according to our rules")

def main():
    solution =Solution()
    while True:
        try:
            uInput = input("Enter list of numbers separated by comma: ")
            uK = input("Enter the k value for Top k frequent elements: ")
            k=int(uK)

            if uInput is not "" or uInput is not '':
                if "," in uInput:
                    userVals = [s.strip() for s in uInput.split(',')]

            uNums=[]
            for id in userVals:
                if id:
                    uNums.append((id))

            uSet =  set(uNums)
            if len(uSet)<k:
                print(f'Please enter again! k value in the range of [1, number of unique elements in list]')
                continue
            else:
                print(f'k is {k},userlist is {uNums},set is {uSet}')
                break
        except ValueError as e1:
            print(f"Hoo hoo ha ha index error {e1}")
        except Exception as e:
            print(f"error {e} I didn't think of this")

    resList = solution.topkFreqElem(uNums,k)
    print(f'Top {k} frequent elements are {resList}')

                

if __name__ == "__main__":
    main()


