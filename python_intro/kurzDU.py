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
        amt = cols[-3]
        curr = cols[-2]
        rate = cols[-1]        
        rate = rate.replace(",", ".")
        if amt == 100: #fixing error in list with multiple bills
                rate = rate / 100   
        rate = float(rate)
        data[curr] = rate
pprint(data)

user_amount = float(input("Insert amount: "))
user_source = input("Insert original curency: ")
user_target = input("Insert target curency: ")

final_value = user_amount * data[user_source], 3)

result = round(final_value / data[user_target], 3)

print(f"Result is {result} {user_target}.")
