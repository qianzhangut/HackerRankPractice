def minion_game(string):
    ct1 = 0
    ct2 = 0
    for i in range(len(string)):
        if string[i] in ['A', 'E', 'I', 'O', 'U']:
            ct1+=len(string)-i
        else:
            ct2+=len(string)-i
        
    if ct1>ct2:
        return print('Kevin'+' '+'{}'.format(ct1))
    elif ct1<ct2:
        return print('Stuart'+' '+'{}'.format(ct2))
    else:
        return print('Draw')