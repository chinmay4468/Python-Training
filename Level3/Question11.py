def count_customers_turned_away(N, S):
    allocated_customers = set()  
    waiting_customers = set()  
    occupied_count = 0 

    for customer in S:
        if customer not in allocated_customers:
            if occupied_count < N:
                allocated_customers.add(customer)
                occupied_count += 1
            else:
                waiting_customers.add(customer)
        else:
            allocated_customers.remove(customer)
            occupied_count -= 1

    return len(waiting_customers)

N = 3
S = "GACCBDDBAGEE"
print(count_customers_turned_away(N, S)) 

N = 1
S = "ABCBAC"
print(count_customers_turned_away(N, S)) 
