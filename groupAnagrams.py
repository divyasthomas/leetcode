from collections import defaultdict 

class Solution:
    def groupAnagrams(self, strs:list[str]) -> list[list[str]]:

        hashm = defaultdict(list)

        for s in strs:
            count =[0]*26
            for ch in s:
                count[ord(ch)-ord('a')] += 1
            
            hashm[tuple(count)].append(s)


        return hashm.values()



def main():
    solution = Solution()

    while True:
        try:
            uInput = input('Enter strings separated by a comma: ')
            parts = uInput.split(',')
            if parts:  # Ensure neither string is empty
                    break
            print("Invalid input. Please enter two strings separated by a comma.")
        except Exception as e:
            print(f"Error: {e}. Please enter two strings separated by a comma.")


    res = solution.groupAnagrams(parts)
    print(res)


if __name__ == "__main__":
    main()
