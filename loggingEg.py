from collections import Counter
import logging

logging.basicConfig(filename="error.log",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.ERROR)

logging.basicConfig(filename="info.log",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)

# logging.info("Running Urban Planning")

logger = logging.getLogger('MyFirstLogger')



class Solution:
    def Isanagram(self,s:str,t:str) -> bool:
        # return Counter(s) == Counter (t)
        # return sorted(s) == sorted(t)

        if len(s) != len(t):
            return False

        sDict, tDict = {}, {}

        for idx in range(len(s)):
            sDict[s[idx]] = sDict.get(s[idx],0) + 1
            tDict[t[idx]] = tDict.get(t[idx],0) + 1
        
        return sDict == tDict


def main():
    solution = Solution()

    while True:
        uInput = input('Enter the two strings separated by comma in lowercase: ')

        try:
            s = uInput.split(',')[0]
            t = uInput.split(',')[1]
            print(s,t)
            if not s or not t:
                print("One of these is empty")
            if not s.islower() or not t.islower():
                print(f"Error! enter again!")
                continue

            break
        except ValueError as e:
            print(f'Error Bad Input. Please try again')
        except Exception as e:
            logger.exception(e)
            raise

        
    s = s.strip()
    t = t.strip()
    res = solution.Isanagram(s,t)
    print(f'Are these anagrams? {res}')
        

if __name__ == "__main__":
    main()
