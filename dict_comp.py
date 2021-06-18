def stop():
    pass

def step():  
    pass
        
    
def dict_comp(stop,step):
    stop=(input('Your stop: '))
    while not stop or stop.isdigit()==False:
        stop=input('Invalid number. Your stop again:')
    my_list= list(range(1,int(stop)+1))
    
    step= (input('You step: '))
    while not step or step.isdigit()==False:
        step= input('invalid input. Your step again: ')
    output= [my_list [i:i+ int(step)]for i in range(0,len(my_list),int(step))]
    if len(output[-1])!=int(step):
        output.pop()
        
    key=[f'item-{i}'for i in range(1,len(output)+1)]

    my_dict={k:v for (k,v)in zip(key,output)}
    print (my_dict)

print (dict_comp(stop,step()))

