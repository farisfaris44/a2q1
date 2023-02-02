#Name: Ifrad Hossain
#NSID: qcg520
#Student Number: 11349288
#Lab Section: Lab Section 08
#Course: cmpt145

example = input("Enter file name: ")

def distance(name):

    last = 0
    steps = []
    a = open(name, 'r')
    r = a.read()
    lines = r.splitlines()
    for x in lines:
        steps.append(x.split())
    for list1 in steps:
        for value in list1:
            if value == 'R':
                last += 1
            else:
                last -= 1
        print(abs(last))
        last = 0

distance(example)