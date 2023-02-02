'''Ifrad Hossain
   qcg520
   11349288
   Lab Section 08
   cmpt145'''

example = input("Enter file name: ")

def distance(name):

    last = 0
    steps = []
    a = open(name, 'r')
    r = a.read()
    lines = r.splitlines()
    for x in lines:
        steps.append(x.split())