#task
#Assume you work in an office and your colleagues chose you to buy 
#something for a professional holiday. 
#They gave you 10 dollars for buying balloons and 50 dollars for 
#buying wine.
 #Each balloon set costs 3$ and one bottle of wine costs 15$. 
 #How many balloons sets and bottles of wine can you buy and 
 #how much money will you spend? Don't forget to print all the results.

 #code
 # create variables to calculate number of items you can buy
n_b=10//3
n_w=50//15

# create variables to calculate money left after each purchase
m_b=10%3
m_w=50%15
# calculate how many money will left
print("After both purchases there will", m_b + m_w, "$ left.")
print("There were", n_b, "balloons packages bought and", n_w, "wine bottles.")