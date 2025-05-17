def dictionary_operations(fruit_prices:dict, fruits:list):
    # add the fruit fruits[0] to fruit_prices with cost 3
    fruit_prices[fruits[0]] = 3
    order_print(fruit_prices) # type: ignore # this function is in the hidden code 

    # modify the cost of fruits[1] as 2 in fruit_prices
    fruit_prices[fruits[1]] = 2
    order_print(fruit_prices) # type: ignore

    # increase the cost of fruits[2] by 2 in fruit_prices
    fruit_prices[fruits[2]] += 2
    order_print(fruit_prices) # type: ignore

    # delete both key and value for fruits[3] from fruit_prices
    del fruit_prices[fruits[3]]
    order_print(fruit_prices) # type: ignore

    # print the price of fruits[4]

    print(fruit_prices[fruits[4]])

    # print the names of fruits in fruit prices as a list sorted in ascending order
    print(sorted(fruit_prices.keys()))

    # print the prices of the fruits as a list sorted in ascending order.
    print(sorted(fruit_prices.values()))

def increase_prices(fruit_prices:dict) -> None:
    
    for fruit in fruit_prices:
        fruit_prices[fruit] *= 1.2 
        fruit_prices[fruit] = round(fruit_prices[fruit] , 2)

def dict_from_string(string:str,key_type,value_type):
   
    D = {}
    for line in string.split("\n") :
        key , value = line.split(",")
        D[key_type(key)] = value_type(value)
    return D

def dict_to_string(D:dict) -> str:
  
 #{'Apple': 2, 'Banana': 3, 'Grapes': 3, 'Orange': 4, 'Papaya': 5}
    return "\n".join(str(key)+ ","+str(value) for key,value in D.items())