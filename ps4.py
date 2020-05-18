sample={"physics": 88 ,"maths": 75,"chemistry": 72,"Basic electrical" : 89}
least = min(sample.values())
print(list(sample.keys())[list(sample.values()).index(least)])