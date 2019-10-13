# Author :Mcmoses Wanna
# Bandwidth Allocation Schemes in 5G wireless network
# Supervisor:Dr Olabisi Falowo


def choice():
    print("Choose between the bandwidth allocation according to numbers below:\n")
    print("1. Complete sharing.\n")
    print("2. Complete partitioning.\n")
    print("3. Handoff call prioritization.\n")
    n=eval(input('Enter the bandwidth allocation strategy needed:\n'))
    return n

def factorial(num):
    """This is a recursive function that calls
   itself to find the factorial of given number"""
    if (num == 1 or num==0):
        return 1
    else:
        return num * factorial(num - 1)
    
def handcall_prioritization(RAT,bbu,A,B,constant):
    # one RAT this should be chaanged
    
    
    # capacity
    print("Choosing handcall prioritization\n")
    # S initial values
    if(RAT==1):
        c1=eval(input('Enter the bandwidth capacity for RAT 1 :\n'))
            #bandwidth
           # bbu =1 
        #c1=40
        #t1=t
        #c1=c
        t1 =eval(input('Enter the threshold :\n'))
       
        n1 =0
        h1 =0 
        G=0
       
        loading_hand=(1-constant)*(A/B)
        loading_new=(A/B)
        prob_drop=0
        prob_block=0
       # start=time.time()
        while (n1 < t1):
            n1 = n1 + 1
            h1 = 0
            while (h1 < c1):
                h1 = h1 + 1
                condition1 = bbu * (n1+h1)
                condition2 = bbu * (n1)
                if (condition1 <= c1 and condition2 <= t1):
                    eN= (loading_new)**(n1)
                    eH= (loading_hand)**(h1)
                    if(loading_hand!=0):
                        prob=eN*eH
                    else:
                        prob=eN
                    den=(factorial(n1))*(factorial(h1))
                    probs=(prob/den) 
                    G+=probs
                         # Blocking group A
                    if ( bbu *( n1+h1 +1) > t1 ):
                        prob_block+= probs
                    if(loading_hand!=0):    
                        if ( bbu *( n1+h1 )>(c1 -bbu )):
                            prob_drop+=probs
                    else:
                        prob_drop=0
        if(G==0):
            prob_drop=1
            prob_block=1
            G=1                            
       # end=time.time()
        print ("\nc1 :", c1)
        print ("t1 :", t1)
        print ("bbu :", bbu)
     # probability values
        print ("probability of blocking group A",( prob_block/G ))
     
        print ("probability of dropping group A ",( prob_drop/G ))
        #print("The time it took to complete the simulation is :",(end-start))
                
    elif(RAT==2):
        c1=eval(input('Enter the bandwidth capacity for voice call :\n'))  
        c2=eval(input('Enter the bandwidth capacity for data call :\n'))  
            #bandwidth
           # bbu =1
           
        
        A1=(c1/(c1+c2))*A #Arrival Rate for voice calls
        A2=(c2/(c1+c2))*A   #Arrival Rate for data calls
        B1=(c1/(c1+c2))*B #Departure Rate for voice calls
        B2=(c2/(c1+c2))*B   #Departure Rate for data calls
        
        t1=eval(input('Enter the threshold of voice call :\n'))
        t2 =eval(input('Enter the threshold of data call:\n'))
       # t1=t/2
        #t2=t/2
        # S initial values
        n1 =0
        h1 =0
        n2 =0
        h2 =0
        #total initial admissions
        G=0
               
        loading_hand_voice=(1-constant)*(A1/B1)
        loading_new_voice=(A1/B1)
        loading_hand_data=(1-constant)*(A2/B2)
        loading_new_data=(A2/B2)       
        prob_drop=0
        prob_block=0       
    
       # start=time.time()
        while (n1 < t1):
            n1 = n1 + 1
            #h2
            h1 = 0
            while (h1 < c1):
                h1 = h1 + 1
                #n2
                n2 = 0
                while (n2 < t2):
                    n2 = n2 + 1
                    #h2
                    h2 = 0
                    while (h2 < c2):
                        h2 = h2 + 1
                        #m3
                        m3 = 0
                        while (m3 < 30):
                            m3 = m3 + 1
                            # admission conditions needed
                            condition1 = bbu * (n1+h1)
                            condition2 = bbu * (n1)
                            condition3 = (1.2*bbu) * (n2+h2)
                            condition4 = (1.2*bbu) * (n2)
                            if (condition1 <= c1 and condition2 <= t1 and condition3 <= c2 and condition4 <= t2 ):
                                eN1= (loading_new_voice)**(n1)
                                eH1= (loading_hand_voice)**(h1)
                                eN2= (loading_new_data)**(n2)
                                eH2= (loading_hand_data)**(h2) 
                                if(constant!=1):
                                    prob=eN1*eH1*eN2*eH2
                                else:
                                    prob=eN1*eN2
                                den=(factorial(n1))*(factorial(h1)*factorial(n2)*factorial(h2))
                                probs=(prob/den) 
                                G+=probs
                                # Blocking group A
                                if ( bbu *( n1+h1 +1) > t1 and (1.2*bbu) *( n2+h2 +1) > t2 ):
                                    prob_block+= probs
                                    # Blocking group B
                                if(constant!=1):
                                    if ( bbu *( n1+h1 )>(c1 -bbu )and (1.2*bbu) *( n2+h2 )>(c2 -(1.2*bbu) )):
                                        prob_drop+=probs
                                else:
                                    prob_drop=0
        if(G==0):
            prob_drop=1
            prob_block=1
            G=1                 
       # end=time.time()        
        # initial capacity and bandwith values
        print ("\nc1 :", c1)
        print ("c2 :", c2)
        print ("t1 :", t1)
        print ("t2 :", t2)
        print ("bbu :", bbu)
        
        print ("probability of blocking group",( prob_block/G))
       # print ("probability of blocking group B",( abB/ tAD ))
        print ("probability of dropping group ",( prob_drop/G ))
       # print ("probability of dropping group B ",( adB/ tAD ))
      #  print("The time it took to simulate is :",(end-start))
        
    elif (RAT==3):
        c1=eval(input('Enter the bandwidth capacity for voice call:\n'))  
        c2=eval(input('Enter the bandwidth capacity for data call:\n'))
        c3=eval(input('Enter the bandwidth capacity for video call :\n'))
            #bandwidth
           # bbu =1 
        A1=(c1/(c1+c2+c3))*A #Arrival Rate for voice calls
        A2=(c2/(c1+c2+c3))*A   #Arrival Rate for data calls
        A3=(c3/(c1+c2+c3))*A    #Arrival rate for video calls
        
        B1=(c1/(c1+c2+c3))*B #Departure Rate for voice calls
        B2=(c2/(c1+c2+c3))*B   #Departure Rate for data calls
        B3=(c3/(c1+c2+c3))*B    #departure rate for video calls
        
        t1=eval(input('Enter the threshold of voice call:\n')) #threshold for voice call
        t2 =eval(input('Enter the threshold of data call:\n'))  #threshold for data call
        t3 =eval(input('Enter the threshold of video call:\n'))
        # S initial values
        n1 =0
        h1 =0
        n2 =0
        h2 =0
        n3=0
        h3=0
        loading_hand_voice=(1-constant)*(A1/B1)
        loading_new_voice=(A1/B1)
        loading_hand_data=(1-constant)*(A2/B2)
        loading_new_data=(A2/B2)
        loading_hand_video=(1-constant)*(A3/B3)
        loading_new_video=(A3/B3)
        G=0
        prob_drop=0
        prob_block=0
       # start=time.time()
        while (n1 < t1):
            n1 = n1 + 1
            #h2
            h1 = 0
            while (h1 < c1):
                h1 = h1 + 1
                #n2
                n2 = 0
                while (n2 < t2):
                    n2 = n2 + 1
                    #h2
                    h2 = 0;
                    while (h2 < c2):
                        h2 = h2 + 1
                        n3=0
                        while (n3 < t3):
                            n3 = n3 + 1
                            h3=0
                            while (h3 < c3):
                                h3 = h3 + 1
                                condition1 = bbu * (n1+h1)
                                condition2 = bbu * (n1)
                                condition3 = (1.2*bbu) * (n2+h2)
                                condition4 = (1.2*bbu) * (n2)
                                condition5=(1.3*bbu)*(n3+h3)
                                condition6=(1.3*bbu)*n3
                            
                                if (condition1 <= c1 and condition2 <= t1 and condition3 <= c2 and condition4 <= t2 and condition5<= c3 and condition6<= t3 ):
                                    eN1= (loading_new_voice)**(n1)
                                    eH1= (loading_hand_voice)**(h1)
                                    eN2= (loading_new_data)**(n2)
                                    eH2= (loading_hand_data)**(h2)
                                    eN3= (loading_new_video)**(n3)
                                    eH3= (loading_hand_video)**(h3)  
                                    if(constant!=1):
                                        prob=eN1*eH1*eN2*eH2*eN3*eH3
                                    else:
                                        prob=eN1*eN2*eN3
                                    den=(factorial(n1))*(factorial(h1)*factorial(n2)*factorial(h2)*factorial(h3)*factorial(n3))
                                    probs=(prob/den) 
                                    G+=probs                                
                                    # Blocking group A
                                    if ( bbu *( n1+h1 +1) > t1 and (1.2*bbu) *( n2+h2 +1) > t2 and (1.3*bbu) *( n3+h3 +1) > t3  ):
                                        prob_block+=probs
                                        # Dropping group A
                                    if(constant!=1):
                                        if ( bbu *( n1+h1 )>(c1 -bbu )and (1.2*bbu) *( n2+h2 )>(c2 -(1.2*bbu) ) and (1.3*bbu) *( n3+h3 )>(c3 -(1.3*bbu) )):
                                            prob_drop+=probs
                                    else:
                                        prob_drop=0
        if(G==0):
            prob_drop=1
            prob_block=1
            G=1             
        # initial capacity and bandwith values
       # end=time.time()
        print ("\nc1 :", c1)
        print ("c2 :", c2)
        print ("c3 :", c3)
        print ("t1 :", t1)
        print ("t2 :", t2)
        print ("t3 :", t3)
        #print ("bbu :", bbu)
        print ("probability of blocking group",( prob_block/G))
        # print ("probability of blocking group B",( abB/ tAD ))
        print ("probability of dropping group ",( prob_drop/G ))
        # print ("probability of dropping group B ",( adB/ tAD ))
       # print("The time it took to simulate is :",(end-start))    



def Complete_Sharing(RAT,bbu,A,B,constant,c):
    # one RAT this should be chaanged
        
    print("Choosing Complete Sharing\n")
    if(RAT==1):
        # capacity
        c1=eval(input('Enter the bandwidth capacity for RAT 1  :\n'))  
        #bandwidth
        #c1=c
        #bbu =1        
        # S initial values
        n1 =0
        h1 =0 
        G=0
              
        loading_hand=(1-constant)*(A/B)
        loading_new=(A/B)
        prob_drop=0
        prob_block=0        
     #   start=time.time()
        while (n1 < c1):
            n1 = n1 + 1
            h1 = 0
            while (h1 < c1):
                h1 = h1 + 1
                condition1 = bbu * (n1+h1)
                #condition2 = bbu * (n1)
                if (condition1 <= c1):
                    eN= (loading_new)**(n1)
                    eH= (loading_hand)**(h1)
                    if(constant!=1):
                        prob=eN*eH
                    else:
                        prob=eN
                    den=(factorial(n1))*(factorial(h1))
                    probs=(prob/den) 
                    G+=probs
                    if(constant!=1):
                        if ( bbu *( n1+h1 )>(c1 -bbu )):
                            prob_block+= probs
                            prob_drop+= probs
                    else:
                        if ( bbu *( n1+h1 )>(c1 -bbu )):
                            prob_block+= probs
                            prob_drop=0                        
        if(G==0):
            prob_drop=1
            G=1
       # end=time.time()
        print ("\nc1 :", c1)
                           
        print ("bbu :", bbu)
                         # Final val
                         # probability values
        print ("probability of blocking group A",( prob_block/G ))
                         
        print ("probability of dropping group A ",( prob_drop/G ))
       # print("The time it took to complete the simulation is :",(end-start))
    elif(RAT==2):
        c1=eval(input('Enter the bandwidth capacity for voice call :\n'))
        c2=eval(input('Enter the bandwidth capacity for data call:\n'))
        A1=(c1/(c1+c2))*A #Arrival Rate for voice calls
        A2=(c2/(c1+c2))*A   #Arrival Rate for data calls
        B1=(c1/(c1+c2))*B #Departure Rate for voice calls
        B2=(c2/(c1+c2))*B   #Departure Rate for data calls               
                   #bandwidth
                   #bbu =1        
                   # S initial values
        n1 =0
        h1 =0
        n2=0
        h2=0
        G=0
                      
        loading_hand_voice=(1-constant)*(A1/B1)
        loading_new_voice=(A1/B1)
        loading_hand_data=(1-constant)*(A2/B2)
        loading_new_data=(A2/B2)      
        prob_drop=0
        prob_block=0               
                   #total initial admissions
       # start=time.time()
        while (n1 < c1):
            n1 = n1 + 1
            h1 = 0
            while (h1 < c1):
                h1 = h1 + 1
                n2=0
                while(n2<c2):
                    n2=n2+1
                    h2=0
                    while(h2<c2):
                        h2=h2+1

                        condition1 = bbu * (n1+h1)
                        condition2=(1.2*bbu)*(n2+h2)
                        if (condition1 <= c1 and condition2 <= c2):
                            eN1= (loading_new_voice)**(n1)
                            eH1= (loading_hand_voice)**(h1)
                            eN2= (loading_new_data)**(n2)
                            eH2= (loading_hand_data)**(h2)
                            if(constant!=1):
                                prob=eN1*eH1*eN2*eH2
                            else:
                                prob=eN1*eN2
                            den=(factorial(n1))*(factorial(h1)*factorial(n2)*factorial(h2))
                            probs=(prob/den) 
                            G+=probs
                            if(constant!=1):
                                if ( bbu *( n1+h1 )>(c1 -bbu ) and (1.2*bbu) *( n2+h2 )>(c2 -(1.2*bbu) )):
                                    prob_block+= probs
                                    prob_drop+= probs
                            else:
                                if ( bbu *( n1+h1 )>(c1 -bbu ) and (1.2*bbu) *( n2+h2 )>(c2 -(1.2*bbu) )):
                                    prob_block+= probs
                                    prob_drop=0                                
        if(G==0):
            prob_drop=1
            prob_block=1
            G=1        
        #end=time.time()
        print ("c1 :", c1)
        print("c2 :",c2)
                #print("c3 :",c3)                              
       # print ("bbu :", bbu)
                                           # Final values
         # probability values
        print ("probability of blocking group ",( prob_block/ G ))
                                            
        print ("probability of dropping group ",( prob_drop/G ))
                   
       # print("The time it took to complete the simulation is :",(end-start))    
   
        
    elif(RAT==3):
        c1=eval(input('Enter the bandwidth capacity for voice call:\n'))
        c2=eval(input('Enter the bandwidth capacity for data call:\n'))
        c3=eval(input('Enter the bandwidth capacity for video call:\n'))
           #bandwidth
           #bbu =1        
           # S initial values
        A1=(c1/(c1+c2+c3))*A #Arrival Rate for voice calls
        A2=(c2/(c1+c2+c3))*A   #Arrival Rate for data calls
        A3=(c3/(c1+c2+c3))*A    #Arrival rate for video calls
        
        B1=(c1/(c1+c2+c3))*B #Departure Rate for voice calls
        B2=(c2/(c1+c2+c3))*B   #Departure Rate for data calls
        B3=(c3/(c1+c2+c3))*B    #departure rate for video calls      
        
        n1 =0
        h1 =0
        n2=0
        h2=0
        n3=0
        h3=0
           #total initial admissions
        loading_hand_voice=(1-constant)*(A1/B1)
        loading_new_voice=(A1/B1)
        loading_hand_data=(1-constant)*(A2/B2)
        loading_new_data=(A2/B2)
        loading_hand_video=(1-constant)*(A3/B3)
        loading_new_video=(A3/B3)
        G=0
        prob_drop=0
        prob_block=0        
      #  start=time.time()
        while (n1 < c1):
            n1 = n1 + 1
            h1 = 0
            while (h1 < c1):
                h1 = h1 + 1
                n2=0
                while(n2<c2):
                    n2=n2+1
                    h2=0
                    while(h2<c2):
                        h2=h2+1
                        n3=0
                        while(n3<c3):
                            n3+=1
                            h3=0
                            while(h3<c3):
                                h3+=1
                                
                           
                                condition1 = bbu * (n1+h1)
                                condition2=(1.2*bbu)*(n2+h2)
                                condition3=(1.3*bbu)*(n3+h3)
                                if (condition1 <= c1 and condition2 <= c2 and condition3 <= c3):
                                    eN1= (loading_new_voice)**(n1)
                                    eH1= (loading_hand_voice)**(h1)
                                    eN2= (loading_new_data)**(n2)
                                    eH2= (loading_hand_data)**(h2)
                                    eN3= (loading_new_video)**(n3)
                                    eH3= (loading_hand_video)**(h3)
                                    if(constant!=1):
                                        prob=eN1*eH1*eN2*eH2*eN3*eH3
                                    else:
                                        prob=eN1*eN2*eN3
                                    den=(factorial(n1))*(factorial(h1)*factorial(n2)*factorial(h2)*factorial(h3)*factorial(n3))
                                    probs=(prob/den) 
                                    G+=probs 
                                    if(constant!=1):
                                        if ( bbu *( n1+h1 )>(c1 -bbu ) and (1.2*bbu) *( n2+h2 )>(c2 -(1.2*bbu) ) and (1.3*bbu) *( n3+h3 )>(c3 -(1.3*bbu) )):
                                            prob_block+= probs
                                            prob_drop+= probs
                                    else:
                                        if ( bbu *( n1+h1 )>(c1 -bbu ) and (1.2*bbu) *( n2+h2 )>(c2 -(1.2*bbu) ) and (1.3*bbu) *( n3+h3 )>(c3 -(1.3*bbu) )):
                                            prob_block+= probs
                                            prob_drop=0                                      
        if(G==0):
            prob_drop=1
            prob_block=1
            G=1        
      #  end=time.time()
        print ("c1 :", c1)
        print("c2 :",c2)
        print("c3 :",c3)                              
        #print ("bbu :", bbu)
                                   # Final values
       
        print ("probability of blocking group A",( prob_block/G))
                                    
        print ("probability of dropping group A ",( prob_drop/G ))
           
        #print("The time it took to complete the simulation is :",(end-start))
    
def Complete_Partition(c,bbu,A,B,constant,r1,r2,r3):
    #start=time.time() 
    print("Choosing Complete partition\n")
    print("VOICE CALL")
    c1=(1/3)*(1/6)*(c) 
    c2=(2/3)*(1/6)*c 
    #bandwidth
    #bbu =1        
    # S initial values
    n1 =0
    #total initial admissions
    G2=0
    G1=0    
    h1=0
    loading_hand1=(1-constant)*(r1/(r1+r2+r3))*(A/B)
    loading_new1=(r1/(r1+r2+r3))*(A/B)
    prob_drop=0
    prob_block=0           
    while (n1 < c1):
        n1 = n1 + 1
        condition2 = bbu * (n1)
        if (condition2 <= c1):
            eN= (loading_new1)**(n1)
                #eH= (loading_hand)**(h1)
            prob=eN
            den=(factorial(n1))
            probs=(prob/den) 
            G2+=probs
            if ( bbu *( n1 )>(c1 -bbu )):
                prob_block+= probs
    if(G2==0):
        prob_block=1
        G2=1
   
    
    #
    #
    #
    #
    #
    #handoff call option
    #c2=c-c1
    
    #loading_new=constant*loading_hand
    #prob_block=0          
     
    while (h1 < c2):
        h1 = h1 + 1
        condition1 = bbu * (h1)
            #condition2 = bbu * (n1)
        if (condition1 <= c2):
            eH= (loading_hand1)**(h1)
            prob=eH
            den=(factorial(h1))
            probs=(prob/den) 
            G1+=probs            
                
            if ( bbu *( h1 )>(c2 -bbu )):
                    prob_drop+= probs
    if(G1==0):
        prob_drop=1
        G1=1    

    print ("c1 for new call(voice) :", c1)
    print ("c2 for handoff call(voice) :", c2)
                            
    #print ("bbu :", bbu)
                            
    print ("probability of blocking group ",( prob_block/G2 ))    
                          # Final values
 
    
    print ("probability of dropping group ",( prob_drop/G1 ))
   # print("The time it took to complete the simulation is :",(end-start)+"\n")
  #///////////////////////////////////////////////////////////////////////////////  
    print("DATA CALL")
    c1=(1/4)*(1/3)*c 
    c2=(3/4)*(1/3)*c  
    #bandwidth
    #bbu =1        
    # S initial values
    n1 =0
    #total initial admissions
    G2=0
    G1=0    
    h1=0     
    loading_hand2=(1-constant)*(r2/(r1+r2+r3))*(A/B)
    loading_new2=(r2/(r1+r2+r3))*(A/B)
    prob_drop=0
    prob_block=0      
   # start=time.time()      
    while (n1 < c1):
        n1 = n1 + 1
        condition2 = (1.2*bbu) * (n1)
        if (condition2 <= c1):
            eN= (loading_new2)**(n1)
                #eH= (loading_hand)**(h1)
            prob=eN
            den=(factorial(n1))
            probs=(prob/den) 
            G2+=probs
            if ( (1.2*bbu) *( n1 )>(c1 -(1.2*bbu) )):
                prob_block+= probs
    if(G2==0):
        prob_block=1
        G2=1    
    
    #
    #
    #
    #
    #
    #handoff call option
    #c2=c-c1
    
    #loading_new=constant*loading_hand
    #prob_block=0          
     
    while (h1 < c2):
        h1 = h1 + 1
        condition1 = (1.2*bbu) * (h1)
            #condition2 = bbu * (n1)
        if (condition1 <= c2):
            eH= (loading_hand2)**(h1)
            prob=eH
            den=(factorial(h1))
            probs=(prob/den) 
            G1+=probs            
                
            if ( (1.2*bbu) *( h1 )>(c2 -(1.2*bbu) )):
                    prob_drop+= probs
    if(G1==0):
        prob_drop=1
        G1=1        
   # end=time.time()
    print ("c1 for new call(data) :", c1)
    print ("c2 for handoff call(data) :", c2)
                            
    #print ("bbu :", bbu)
                            
    print ("probability of blocking group ",( prob_block/G2 ))    
                          # Final values
  
  
    print ("probability of dropping group ",( prob_drop/G1 ))
    #print("The time it took to complete the simulation is :",(end-start)+"\n")    
    #///////////////////////////////////////////////////////////////////////////////  
    print("VIDEO CALL")
    c1=(1/5)*(1/2)* c
    c2=(4/5)*(1/2)* c  
    #bandwidth
    #bbu =1        
    # S initial values
    n1 =0
    #total initial admissions
    G2=0
    G1=0    
    h1=0     
    loading_hand3=(1-constant)*(r3/(r1+r2+r3))*(A/B)
    loading_new3=(r3/(r1+r2+r3))*(A/B)
    prob_drop=0
    prob_block=0      
   # start=time.time()      
    while (n1 < c1):
        n1 = n1 + 1
        condition2 = (1.3*bbu) * (n1)
        if (condition2 <= c1):
            eN= (loading_new3)**(n1)
                #eH= (loading_hand)**(h1)
            prob=eN
            den=(factorial(n1))
            probs=(prob/den) 
            G2+=probs
            if ( (1.3*bbu) *( n1 )>(c1 -(1.3*bbu) )):
                prob_block+= probs
    if(G2==0):
        prob_block=1
        G2=1     
    
    #
    #
    #
    #
    #
    #handoff call option
    #c2=c-c1
    
    #loading_new=constant*loading_hand
    #prob_block=0          
     
    while (h1 < c2):
        h1 = h1 + 1
        condition1 = (1.3*bbu) * (h1)
            #condition2 = bbu * (n1)
        if (condition1 <= c2):
            eH= (loading_hand3)**(h1)
            prob=eH
            den=(factorial(h1))
            probs=(prob/den) 
            G1+=probs            
                
            if ((1.3*bbu) *( h1 )>(c2 -(1.3*bbu) )):
                    prob_drop+= probs
    if(G1==0):
        prob_drop=1
        G1=1       
    #end=time.time()
    print ("c1 for new call(video) :", c1)
    print ("c2 for handoff call(video):", c2)
                            
    #print ("bbu :", bbu)
                            
    print ("probability of blocking group ",( prob_block/G2 ))    
                          # Final values
    
    
    print ("probability of dropping group ",( prob_drop/G1 ))
    print("///////////////////////////////////////////////////////////////////")
   # print("The time it took to complete the simulation is :",(end-start)+"\n")    
                     
        
def main():
    h=choice()
    while (h!=1 and h!=2 and h!=3):
        print("Wrong choice,Sorry choose again\n")
        h=choice()
    A=eval(input("\nEnter the Call Arrival Rate (calls/minute)\n"))
    B=eval(input("Enter the Call Departure Rate (calls/minute)\n"))
    while(B>A):
        B=eval(input("Departure Rate can't be bigger than the Arrival Rate.Repeat Entering the Call Departure Rate (calls/minute)\n"))    
    if(h!=2):
        RAT=eval(input('Input the number of RAT Required (1 to 3):\n'))
    constant=eval(input("The loading intensity between the handover calls to new data call between 0 and 1 inclusive\n"))
    while(constant>1):
        constant=eval(input("The loading intensity between the handover calls to new data call between 0 and 1\n"))
    bbu=eval(input('Input the bbu Required:\n'))
    if (h==3):
        #t1 =eval(input('Enter the threshold :\n'))
        handcall_prioritization(RAT,bbu,A,B,constant)
    elif(h==1):
        Complete_Sharing(RAT,bbu,A,B,constant)
        
    elif(h==2):
        c=eval(input('Enter the bandwidth capacity :\n'))
        r1=eval(input('Enter the rate of voice call :\n'))
        r2=eval(input('Enter the rate of data call:\n'))
        r3=eval(input('Enter the rate of video call :\n'))
        Complete_Partition(c,bbu,A,B,constant,r1,r2,r3) #r1,r2,r3=40,20,15
    else:
        print("\nSorry something went wrong")  
if __name__=='__main__':
    main()