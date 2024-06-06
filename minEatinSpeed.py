import math, logging
class Solution:
    def maxEatingSpeed(self, piles:list[int], h:int)->int:
        max_k = 0
        for ele in piles:
            max_k = max(max_k,ele)
        left = 1
        right = max_k
        result =max_k
        # print(f'result {result}')       

        while left <= right:
            # print(f'left: {left}, right: {right}')
            mid_k = (left + right)//2
            # print(f'mid_k {mid_k}')
            cur_h = 0
            for pile in piles:
                cur_h = cur_h + math.ceil(float(pile)/mid_k)
                # print(f' cur_h = {cur_h},  div: {math.ceil(float(pile)/mid_k)}')       


            if cur_h <= h: #tto fast
                right = mid_k -1
                result = mid_k
                # print(f'result {result}, cur_h = {cur_h}')       

            else:
                left = mid_k +1
        # print(f'result {result}')       
        return result



def main():
    while True:
        try:
             user_input = input('Enter list of integers separated by comma representing number of bananas in each pile:')
             user_list = [ int(each.strip()) for each in user_input.split(',')]
             for each in user_list:
                 if each < 1:
                     print('Each value in list must be greater than 0')
                     raise RuntimeError
             if len(user_list) <1:
                print('list must contain at least one value')
                raise RuntimeError

             h_input = input(f'Enter number of hours (h) by which the guards will come back. This number h must be greater than or equal to piles. In this case h must be greater than or equal to {len(user_list)}: ')
             h = int(h_input)
             if h < len(user_list):
                print('h must be at least same or greater than length of list')
                raise RuntimeError
             break
        except ValueError as e:
            logging.error('You must enter integers only. Bad Input. Try again!')
        except RuntimeError as e:
            logging.error(' Bad Input. Try again!')
        except Exception as e:
            logging.error('I am momo! Try again!')
        
    # print(f'cur list is {user_list} ')

    solution = Solution()
    minSpeed = solution.maxEatingSpeed(user_list, h)
    print(f'  Minimum integer k such that Momo can eat all the bananas within h hours is {minSpeed}')
        



if __name__=="__main__":
    main()