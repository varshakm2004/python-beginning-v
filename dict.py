l=[1,2,3,4,5]
output=dict(map(lambda x:(x,x*2),l))
print(output)
################################################
l=[1,2,3,4,5]
output={i:i*2 for i in l}
print(output)
###########################################3
prices=[15,25,10,30,40]
prices_below_20=[price for price in prices if price<20]
print(prices_below_20)
#################################################
customers=['Rahul','Antony','Salman','Arun','Kiran']
a_customer=[customer for customer in customers if customer.startswith('A')]
print(a_customer)
################################################################################333
employees={'Antony':55000,'Susan':45000,'Kiran':60000}
categorized_employees={name:'high'if salary>50000 else 'low' for name,salary in employees.items()}
print(categorized_employees)
#################################################################################################
words=['apple','banana','apple','orange','banana','apple']
words_count={word:words.count(word) for word in set(words) }
print(words_count)