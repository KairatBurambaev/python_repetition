names = ['Alice', 'Bob', 'Charlie']
rates = [100, 200, 300]
bonuses = ['10.25%', '5%', '7.5%']

result = {name: rate * float(bonus.strip('%')) / 100 for name, rate, bonus in zip(names, rates, bonuses)}

print(result)