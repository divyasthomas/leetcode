import logging

class BadInputError(Exception):
    """A bad input was encountered"""

class Solution:
    def maxVol(self, height:list[int]) ->int:
        left, right = 0, len(height)-1
        max_vol = 0
        
        while left < right:
            logging.info('entered loop')
            min_height = min(height[left],height[right])
            breadth = right - left
            cur_vol = min_height * breadth
            max_vol = max( max_vol, cur_vol)
            if height[left] == min_height:
                left = left + 1
            else:
                right = right - 1
        return max_vol
    

def main():
    solution = Solution()
    while True:
        user_input = input('Enter a list of integers for heights of lines separated by comma: ')

        try:
            height_list = [int(each.strip()) for each in user_input.split(',')]
            if len(height_list)< 2:
                raise BadInputError("You are evil")
            for ele in height_list:
                if ele < 0:
                    raise ValueError
            break
        except BadInputError as e:
            logging.error(f'Sorry! please enter minimum of 2 integer values for height. Bad Input caused error {e}')
        except ValueError as v:
             logging.error(f'Sorry! please enter only non-negative integer values for height. Bad Input caused error: {v}')
        except Exception as e:
            logging.exception(f'sorry! I didnot think of this error: {e}')

    res_vol = solution.maxVol(height_list)
    print(f"Maximum amount of water container can store is {res_vol} unit cube")

if __name__=="__main__":
    main()
