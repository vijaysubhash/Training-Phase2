a = int(input())
db = {}
for i in range(a):
    b, c = input().split("->")
    db.update({b: c})

print(db)

