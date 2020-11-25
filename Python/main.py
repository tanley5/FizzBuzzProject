"""
Todo list:
1. Create a loop that shows a number from 1 to 100
2. For every number divisible by 3, show "FIZZ"
3. For every number divisible by 5, show "BUZZ"
4. For every number divisible by 3 and 5, show "FIZZ BUZZ"
"""

def app():
    for i in range(100):
        num = i
        num+=1
        if num%3 == 0 and num%5==0:
            print("FIZZ-BUZZ", end=" ")
        elif num%3 == 0:
            print("FIZZ", end=" ")
        elif num%5 == 0:
            print("BUZZ", end=" ")
        else:
            print(num, end=" ")
        
if __name__ == "__main__":
    app()