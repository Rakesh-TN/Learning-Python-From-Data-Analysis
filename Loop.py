# While Loop 
print("- While Loop")

count = 1
while count <= 5:
    print("Count is:", count)
    count += 1
    
# For Loop
print("- For Loop")

for i in "Rakesh":
    print(i)
    
countries = ['United Status of America', 'Canada', 'Brazil', 'Australia', 'India']

for country in countries:
    print(country) 
    
for country in countries:
    if country == 'Australia':
        break
    print("country are all same line :",country)  