from collections import defaultdict 

class Solution:
    def groupAnagrams(self, strs:list[str]) -> list[list[str]]:

        hashm = defaultdict(list)

        for s in strs:
            count =[0]*26
            print(count)
            for ch in s:
                count[ord(ch)-ord('a')] += 1

            print(count)

            hashm[tuple(count)].append(s)


        return hashm.values()




def main():
    solution = Solution()

    while True:
        try:
            uInput = input('Enter strings separated by a comma: ')
            parts = [s.strip() for s in uInput.split(',')]
            print(parts)
            
            if not (1 <= len(parts) <= 104):
                print("Invalid input. Please enter between 1 and 10,000 strings.")
                continue
            
            if any(len(s) > 100 or not s.islower() or not s.isalpha() for s in parts):
                print("Invalid input. Ensure each string is at most 100 characters long, consists of lowercase English letters, and contains no punctuation or special characters.")
                continue
            
            break
        except Exception as e:
            print(f"Error: {e}. Please enter the strings correctly.")

    res = solution.groupAnagrams(parts)
    print(res)

if __name__ == "__main__":
    main()
