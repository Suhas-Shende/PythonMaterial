def questionstring(num,que):
    k="-".join(que.split())
    print(f"| {num} | [{que}?](#{k}) |")



q=input("Enter a question:")
n=int(input("Enter que no."))
questionstring(n,q)

'''
output
| 2 | [Why is Python so popular?](#why-is-python-so-popular) |
'''


