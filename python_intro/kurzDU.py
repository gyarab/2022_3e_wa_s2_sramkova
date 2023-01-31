import httpx
from  pprint import pprint
url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"

res = httpx.request("GET", url)
data = res.text
rows = data.split("\n")

rows = rows[2:-1] #removing first two and last row


data = {} #empty dicionary

for r in rows:
        cols = r.split('|')
        curr = cols[-2]
        rate = cols[-1]        
        rate = rate.replace(",", ".")
        rate = float(rate)
        amt = cols[-3]
        if amt == 100: #fixing error in list with multiple bills
            result = rate / 100  
            rate = result
        data[curr] = rate
pprint(data)

user_amount = float(input("Insert amount: "))
user_source = input("Insert original curency: ")
user_target = input("Insert target curency: ")

source = data[user_source]
value = user_amount * source
result = round(value / data[user_target], 3)

print(f"Result is {result} {user_target}.")