## 6.100A PSet 1: Part C
## Name:
## Time Spent:
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input("Enter the initial deposit: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
cost_of_dream_home = 800000
portion_down_payment = 0.25
months = 36
steps = 0
eps = 100

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################
if initial_deposit >= cost_of_dream_home * portion_down_payment - eps:

    r = 0.0

    print(f"Best savings rate: {r} [or very close to this number]")
    print(f"Steps in bisection search: {steps} [or very close to this number]")

elif initial_deposit * ( ( 1 + 1 / 12 ) ** months ) < cost_of_dream_home * portion_down_payment - eps:

    r = None
    
    print(f"Best savings rate: {r}")  
    print(f"Steps in bisection search: {steps} [May vary based on how you implemented your bisection search]")

else:

    low = 0
    high = 1
    r =( low + high ) / 2
    steps = 1
    amount_saved = initial_deposit * ( ( 1 + r / 12 ) ** months )

    while abs( amount_saved - cost_of_dream_home * portion_down_payment ) > eps:

        if amount_saved > cost_of_dream_home * portion_down_payment:
            high = r
        else:
            low = r
        
        r = ( low + high ) / 2
        amount_saved = initial_deposit * ( ( 1 + r / 12 ) ** months )

        steps = steps + 1

    print(f"Best savings rate: {r} [or very close to this number]")
    print(f"Steps in bisection search: {steps} [or very close to this number]")