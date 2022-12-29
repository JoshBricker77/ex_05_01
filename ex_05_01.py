#iteration variable for count
num = 0
tot = 0.0
#infinite loop
#input gives a string
while True :
    sval = input('Enter a number: ')
    if sval == 'done' :
        break
    try:
        fval = float(sval)
    except:
        print('Invald input')
        continue
    #print(fval)
    num = num + 1
    tot = tot + fval
    
#print('ALL DONE')
print(tot,num,tot/num)