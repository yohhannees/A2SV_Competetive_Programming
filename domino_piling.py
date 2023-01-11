query = input()
query = query.split(' ')
data = [int(q) for q in query]
result = (data[0] // 2) * data[1]
result += data[0] % 2 * data[1] // 2
print(result)
