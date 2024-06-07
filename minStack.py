import logging
class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []
    
    def push(self, val:int) ->None:
        self.stack.append(val)
        min_val = val
        if self.minstack:
            min_val = min(min_val, self.minstack[-1])
        self.minstack.append(min_val)
        print(f"pushed {val} onto the stack.")


    
    def pop(self) ->None:
        if self.stack:
            self.stack.pop()
            self.minstack.pop()
            print("popped top element from the stack.")

        else:
            print('Empty stack')


    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            print('Empty stack')
            return None
    
    def getMin(self) ->int:
        if self.stack:
            return self.minstack[-1]
        else:
            print('Empty stack')
            return None
    
    def printstack(self)->None:
        print(f'my stack is {self.stack}')

def main():
    min_stack = MinStack()
    while True:
        try:
            print("\nChoose a number (1to 5) for the specified operation:")
            print("1. push")
            print("2. pop")
            print("3. top")
            print("4. getMin")
            print("5. exit")
            choice = input("Enter the number of your choice: ")
            user_choice = int(choice)
            if user_choice == 1:
                val = int(input("Enter INTEGER value to push: "))
                min_stack.push(val)
                min_stack.printstack()
            elif user_choice == 2:
                min_stack.pop()
                min_stack.printstack()

            elif user_choice == 3:
                print(f"top element is {min_stack.top()}")
                min_stack.printstack()

            elif user_choice == 4:
                print(f"minimum element is {min_stack.getMin()}")
                min_stack.printstack()

            elif user_choice == 5:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError as e:
            logging.error(f'Please enter only an integer number. Bad input. {e}')
        except Exception as e:
            logging.error(f'I AM MOMO! {e}')


if __name__ == "__main__":
    main()



