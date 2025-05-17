'''
GrPA 2 - Dictionary Applications - GRADED
Implement the below functions as per the docstrings.
'''
#answer 

def total_price(fruit_prices: dict, purchases) -> float:
 
    total = 0
    for fruit, quantity in purchases:
        total += fruit_prices[fruit] * quantity
    return total

def total_price_no_loops(fruit_prices: dict, purchases) -> float:
   
    return sum([fruit_prices[fruit] * quantity for fruit, quantity in purchases])

def find_cheapest_fruit(fruit_prices:dict) -> str:
  
    cheapest_fruit = ''
    cheapest_price = float('inf')
    for fruit, price in fruit_prices.items():
        if price < cheapest_price:
            cheapest_fruit = fruit
            cheapest_price = price
    return cheapest_fruit

def find_cheapest_fruit_no_loops(fruit_prices:dict) -> str:
   
    return min(fruit_prices, key=fruit_prices.get)

# grouping
def group_fruits(fruits:list):
   
    grouped_fruits = {}
    for fruit in fruits:
        first_letter = fruit[0]
        if first_letter not in grouped_fruits:
            grouped_fruits[first_letter] = []
        grouped_fruits[first_letter].append(fruit)
    for letter in grouped_fruits:
        grouped_fruits[letter].sort()
    return grouped_fruits

# binning
def bin_fruits(fruit_prices):
    
    binned_fruits = {'cheap': set(), 'affordable': set(), 'costly': set()}
    for fruit, price in fruit_prices.items():
        if price < 3:
            binned_fruits['cheap'].add(fruit)
        elif 3 <= price <= 6:
            binned_fruits['affordable'].add(fruit)
        else:
            binned_fruits['costly'].add(fruit)
    return binned_fruits