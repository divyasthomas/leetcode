class Solution:
    def SellStockBest(self, prices: list[int]) -> int: 
        left, right = 0, 1
        max_profit = 0
    

        while right < len(prices):
            cur_profit = prices[right] - prices[left]
            if cur_profit < 0:
                left = left + 1
            else:
                right = right + 1
            max_profit = max(max_profit,cur_profit)
        
        return max_profit

def main():
    solution = Solution()
    price_list = []
    while True:
        try:
            user_input = input('Enter list of prices separated by comma:')
            user_list = [each.strip() for each in user_input.split(',')]
            for ele in user_list:
                if ele.isnumeric():
                    mod_ele = int(ele)
                    price_list.append(mod_ele)
                else:
                    print(ele)
                    raise ValueError
            print(price_list)
            result = solution.SellStockBest(price_list)
            print(f'Max profit is: {result}')
            break        
        except ValueError as v:
            print(f'please only enter numbers! Try again {v}')
        except Exception as e:
            print("Error {e}: I didn't think of this:( ")
        

if __name__ == "__main__":
    main()