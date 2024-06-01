class Solution:
    def validAnagram(self, s:str, t:str) -> bool:
        if len(s)!=len(t):
            return False
        
        else:
            sDict, tDict = {}, {}
            for idx in range(len(s)):
                sDict[s[idx]] = sDict.get(s[idx],0) +1 
                tDict[t[idx]] = tDict.get(t[idx],0) +1 

            return sDict == tDict


def main():
    solution = Solution()

    while True:
        try:
            uInput = input('Enter s and t strings separated by a comma: ')
            parts = uInput.split(',')
            if len(parts) == 2:
                s, t = parts[0].strip(), parts[1].strip()
                if s and t:  # Ensure neither string is empty
                    break
            print("Invalid input. Please enter two strings separated by a comma.")
        except Exception as e:
            print(f"Error: {e}. Please enter two strings separated by a comma.")


    res = solution.validAnagram(s,t)
    print(res)


if __name__ == "__main__":
    main()
