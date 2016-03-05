def removeABs(step):
    for i in range(len(step)):
        while('<' in step[i]):
            x = step[i]
            step[i] = x.replace(x[x.index('<'):(x.index('>')+1)],'')
    return step

def toDicts(step):
    ret = []
    while len(step)!=0:
        ret.append({step[0]:[int(step[i+1]) for i in range(6)]})
        step = step[7:]
    return ret

def getEVs():
    f = open('evyields.html', 'r+')
    s = f.read()
    f.close()
    
    #step1 = s.split('<')
    step1 = s.splitlines()
    
    step2 = [x for x in step1 if (('FF5959' in x) or 
                                  ('F5AC78' in x) or
                                  ('FAE078' in x) or
                                  ('9DB7F5' in x) or
                                  ('A7DB8D' in x) or
                                  ('FA92B2' in x) or
                                  ('(Pokémon)' in x))]

    step3 = removeABs(step2)
    step4 = [x[1:] for x in step3]
    step5 = toDicts(step4)
    return step5

#test = getEVs()
#for x in test:
#    print(x)

def getStats():
    f = open('stats.html', 'r+')
    s = f.read()
    f.close()
    
    #step1 = s.split('<')
    step1 = s.splitlines()
    
    step2 = [x for x in step1 if (('FF5959' in x) or 
                                  ('F5AC78' in x) or
                                  ('FAE078' in x) or
                                  ('9DB7F5' in x) or
                                  ('A7DB8D' in x) or
                                  ('FA92B2' in x) or
                                  ('(Pokémon)' in x))]

    step3 = removeABs(step2)
    step4 = [x[1:] for x in step3]
    step5 = toDicts(step4)
    return step5

test = getStats()
for x in test:
    print(x)

'''BAD METHOD
def sieve(step):
    for x in step:
        if not (('FF5959' in x) or 
                ('F5AC78' in x) or
                ('FAE078' in x) or
                ('9DB7F5' in x) or
                ('A7DB8D' in x) or
                ('FA92B2' in x) or
                ('(Pokémon)' in x)):
            step.remove(x)
    return step

print(len(step1))
step1 = sieve(step1)
print(len(step1))
step1 = sieve(step1)
print(len(step1))
step1 = sieve(step1)
print(len(step1))
'''
