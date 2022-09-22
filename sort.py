'''
    Sorts and normalizes data from a text file and outputs it onto a single line
    22-9-22
    Anirudh Koteshwar
'''
lst = []
with open('courts.txt', 'r+') as file:
    for line in file:
        aline = line.replace("\n", "")
        nline = aline.lower()
        lst.append(nline)
print(", ".join(lst))


