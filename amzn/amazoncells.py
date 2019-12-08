def cellCompete(states, days):
    # WRITE YOUR CODE HERE
    l = len(states)
    new = states[:]
    if l == 1:
        new = [0]
        return(new)
    for day in range(days):
        for i in range(l):  
            print(i)
            if i == 0:
                if states[i + 1] == 0:
                    new[i] = 0 
                else:
                    new[i] = 1 
            elif i == l - 1:
                if states[i - 1] == 0:
                    new[i] = 0 
                else:
                    new[i] = 1
            elif 0 < i < l - 1:
                if states[i - 1] == states[i +1]:
                    new[i] = 0 
                else:
                    new[i] = 1
        states = new[:]
        print(new)
    return new
