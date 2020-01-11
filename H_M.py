# Hotel Management
import sys
class H_M():
    #print('\t\t\t Hotel Avira')
 # while True:  
# =============================================================================
#     print('1.Customer Details')
#     print('2.Food Items')
#     print('3.Room Details and Tariff\n')
#     
# =============================================================================
    def __init__(self,t=0,name='',cin='',cout='',ph='',add='',f1='',f2='',f3='',f4='',f5='',q=0,w=0,f6='',f7='',f8='',f9='',f10='',f11='',f12=''):
          self.n=name
          self.ph=ph
          self.add=add
          self.q=q;self.t=t
          self.w=w
          self.cin=cin
          self.cout=cout
  #while True:
   
    def u_d(self):
          self.n=str(input('Name: '))
          self.ph=int(input('Contact Number: '))
          self.add=str(input('Address: '))
          self.cin=(input("Check-in Date (in DD-MM-YYYY): "))
          self.cout=(input("Check-out Date (in DD-MM-YYYY): "))      
    #elif a==2:
    def Food_Items(self):
         #print('To select the desired food item, enter a number from 1 and 7: ')
         print('\t\t\tMenu\n')
         print('To select the desired food item, enter a number from 1 and 7: ')
         print('\tItem\t\tPrice')
         print('1.Keylime Pie:         $43')
         print('2.Tater Tots:          $29')
         print('3.Cobb Salad:          $39')
         print('4.Pot Roast:           $36')
         print('5.Fujitas:             $45')
         print('6.Chicken Fried Steak: $28')
         print('7.Meat Loaf:           $30\n')
         print('To go back to main menu, click 0')
         
         #b=int(input('Choose a number from 1-7: '))
         while (1):
             b=int(input('Choose a number from 1-7: ')) 
             if b==1:
                 print('Keylime Pie:         $43')
                 q=int(input('Quantity: '))
                 self.q=self.q+43*q
             elif b==2:  
                 print('Tater Tots:          $29')
                 q=int(input('Quantity: '))
                 self.q=self.q+29*q
             elif b==3:  
                 print('Cobb Salad:          $39')
                 q=int(input('Quantity: '))
                 self.q=self.q+39*q
             elif b==4:  
                 print('Pot Roast:           $36')
                 q=int(input('Quantity: '))
                 self.q=self.q+36*q
             elif b==5:  
                 print('Fujitas:             $45')
                 q=int(input('Quantity: '))
                 self.q=self.q+45*q
             elif b==6:  
                 print('6.Chicken Fried Steak: $28')
                 q=int(input('Quantity: '))
                 self.q=self.q+28*q
             elif b==7:
                 self.f7=print('7.Meat Loaf:           $30\n')
                 q=int(input('Quantity: '))
                 self.q=self.q+30*q
             elif b==0:
                 break
             else:
                 print('Invalid number, please enter number from 1-7.')
         print('Total: \n\n',self.q)
    
    #elif a==3:    
    def Tariff(self):
         #while True:
             print('1.Single cot with Non-A/C:  $300/day')
             print('2.Double cot with Non-A/C:  $400/day')
             print('3.Single cot with A/C:      $550/day') 
             print('4.Double cot with A/C:      $600/day')
             print('5.King size (Only A/C):     $950/day\n')
             print('To get back to main menu, click 0\n')
             while 1:
               c=int(input('For selecting any room, choose a number from 1-5: '))
               #r=int(input('No. of nights: '))
               if c==1:
                   r=int(input('No. of nights: '))
                   print("You've chosen Single cot with Non-A/C room.")
                   self.w=r*300
                 
               elif c==2:
                   r=int(input('No. of nights: '))
                   print("You've chosen Double cot with Non-A/C room.")
                   self.w=r*400
               elif c==3:
                   r=int(input('No. of nights: '))
                   print("You've chosen Single cot with A/C room.")
                   self.w=r*550            
               elif c==4:
                   r=int(input('No. of nights: '))
                   print("You've chosen Double cot with A/C room.")
                   self.w=r*600               
               elif c==5:
                   r=int(input('No. of nights: '))
                   print("You've chosen King size (Only A/C) room.")
                   self.w=r*950
                 #elif c==0:
                 #break
               elif c==0:
                   break
             print('Price: ',self.w,'\n')       
    #else a==0:
     #   print('Invalid number')
            
    def tot(self):
        print('------------------------------------------------------------------')
        print('\n\t\t\tTOTAL BILL')
        print('\t-----------------------------------------------')
        tot=self.w+self.q
        print('\nName: ',self.n)
        print('Total bill: $',tot)
        print('Contact Number: ',self.ph)
        print('Address: ',self.add)
        print("Check-in: ",self.cin)
        print("Check-out: ",self.cout)
        print('Food Items: ',self.q)
        print('Room Rent: ',self.w)
        print('Laundry: ',self.t)
        print('Total price: $',self.t+self.w+self.q)
        print('------------------------------------------------------------------\n\n\n')    
            
    def Laundry(self):
        print('To avail Laundry services, select any of the following: ')
        print('1.Shirt\t\t\t\t$15')
        print('2.Trouser\t\t\t$20')
        print('3.Ironing per piece\t\t$20\n')
        print('To get back to main menu, click 0' )          
            
        while 1:
            u=int(input('Choose any of the above: '))
            if u==1:
                print("You've opted for shirt washing")
                t=int(input('Quantity: '))
                self.t=15*t+self.t
            
            elif u==2:
                print("You've opted for trouser washing")
                t=int(input('Quantity: '))
                self.t=20*t+self.t
            
            elif u==3:
                print("You've opted for ironing")
                t=int(input('Quantity: '))
                self.t=20*t+self.t
            elif u==0:
                break
        
        print('Price: ',self.t)
            
            
            
            
            
            
            
obj=H_M()
#obj.u_d()
#obj.Food_Items()
#obj.Tariff()        
while True:
    print("\t\t\t Koundinya's Kitchen\n\t\t\t       LONDON")
    print('----------------------------------------------------------------------')
    print('1.Customer Details')
    print('2.Food Items')
    print('3.Room Details and Tariff')
    print('4.Laundry')
    print('5.Billing\n')
    print('To exit, click 0')
    
    a=int(input('Enter a number from 1-5: '))
    if a==1:
        obj.u_d()
    elif a==2:
        obj.Food_Items()
    elif a==3:
        obj.Tariff()  
    elif a==4:
        obj.Laundry()
    elif a==5:
        obj.tot()
    elif a==0:
        print('Please visit again.')
        break