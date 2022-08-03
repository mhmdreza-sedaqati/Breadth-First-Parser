grammer = {}

while True :
    var = []
    a = input("Enter variable : ")
    if a == "":
        break

    while True:
        b = input("Enter substring : ")
        if b == "":
            break
        var.append(b)
        grammer[a] = var
    var = []

print("the grammer that you entered : {0}".format(grammer))

w = input("Enter your sentence : ")
w_prefixes = []
w_prefixes.append('e')

for i in range(1 , len(w)+1) :
    w_prefixes.append(w[:i])

print("prefixes of sentence that you entered : {0}".format(w_prefixes))



ls1 = []
for i in grammer['S']:
    ls1.append(i)
# print(ls1)


def parser(u):
    output = []
    for i in u:
        for m in i:
            s_prefix = []
            if ((m >= 'A') and (m <= 'Z')):

                if (i.index(m) == 0):
                    s_prefix.append('e')
                    break
                else:
                    s_prefix.append(i[:i.index(m)])
                    break

            else:
                continue


        if (len(s_prefix) == 1):
            if(s_prefix[0] in w_prefixes):
                for j in i:
                    if ((j >= 'A') and (j <= 'Z')):
                        for k in grammer[j]:
                            x = i[:i.index(j)] + k + i[i.index(j)+1:]
                            output.append(x)
                        break
                    else:
                        continue
            
            else:
                continue

        else:
            continue

    return output


ls2 = parser(ls1)
# print(ls2)

while True:

    ls2 = parser(ls2)
    # print(ls2)

    if w in ls2:
        print("Yes , this sentence can be produced by this grammer .")
        break

    if (len(ls2) == 0):
        print("No , this sentence cannot be produced by this grammer")
        break

