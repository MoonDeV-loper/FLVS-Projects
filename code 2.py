# Assigment 02.06 Project
# Date: Wed 27/01/2025 #2025 already! 
# Student: Daniel Bealer 
# Grade: 11th
# Purpose: Calculating prices with a small twist.

# GLOBAL V A R S
global text #the text var for the typing animation 
text = "test text texting"
global systemName
systemName = "Buy stuff in a Captalist Society Assistant by Simulating a Recepit Simulator!"
global curMD
curMD = 1
global spEvent #For the posibilty of special events once the user does an incorrect input
spEvent = 0

import math

def calVolume(side_length): #calculates volume
    return pow(side_length, 3) #l^3
	
def calSurfArea(side_length): #calculates well the surface area lol
    return 6 * pow(side_length, 2)
 
#animates text well it is called first then it animated the text :D
def typeAnim(text, speed=0.1):
    #imports time and this new system thing i NEVER knew about.
    import time
    import sys

    for char in text: #char means characters 
      sys.stdout.write(char) #stdout for altering the output directly atleast its behaviour
      sys.stdout.flush() #i searched what is flush and well its a really technicall thing ensuring that data is written from internet buffer to its destination correctly and immediately.
      time.sleep(speed) #basically it will wait for the specified amount of time the code will set once the parent function is called.

def cubeSequel(): #Recognize the code? :D I reused some old code and made newer code.

    import time
    import math #very important for sqrt and other functions related to math :)
	
	
	typeAnim("Once the text starts printing, please WAIT until that process finishes. If not IDLE will behave oddly...", speed=0.04)
	time.sleep(1.0)
	
	#D I A L O U G E
	
	#Disclaimer
	print("")
    typeAnim("Program will store data only per session.", speed=0.03)
	print("")
	time.sleep(1.0)
	typeAnim("Welcome to " + systemName , speed=0.03)
	print("")
	time.sleep(1.0)
	x = 3

# S Y S T E M

    #end of product storage

    #def productCart():

    #end of product cart
	
	
	# c a l l
    def productWizrd():
	
		print("")
		typeAnim("Let's make the products for your fake receipt :D", speed=0.04)
	    print("")
	    time.sleep(1.0)
		typeAnim("...", speed=1.0)

		
		
		#productStore Vars
		
		global prs
		prs = ["Free Gift (Receipt)","Product1","Product2", "Product3", "Product4", "Product5",  "Product6", "Product7", "Product8", "Product9",]
		
        global prCategories
		prCategories = ["Other", "Tech & Software", "Food", "Office", "Drinks", "Licor", "Enterntainment", "Drug / Medicine", "Artesanal", "Unspecified"] #Categories Available, You can change this :D, And add how many ctageories you want!
		
		global cost
		cost = [0,0,0,0,0,0,0,0,0,0]
		
		global totalCost
		totalCost = [0,0,0,0,0,0,0,0,0,0]	
		
		
		global tax
		tax = 2.7
		
		global taxPRS
		taxPRS = [0,0,0,0,0,0,0,0,0,0]		
		
		global shippingVal
		shippingVal = 1.2
		
		global idPR
		idPR = ["0","0","0","0","0","0","0","0","0","0"] #IDs for each profuct containg each index that wil be compiled in to showcase its final values.
			
		#Process of Creation of Products
	    
        i = 0
		f = 9 #on what index it should end
		global iPR
		iPR = int(input("How many products you wish to make (Max 10) "))
		time.sleep(0.5)


	    lpZoom = 0
		for i in range(0, iPR):
		     

			 lpZoom += 1
			 print("")
		     typeAnim("Name the product" , speed=0.02)
	         print("")
			 prs[lpZoom] = input("Name product " + str(lpZoom)) #:D Saves the product name to its corresponding oject index in the array
	         time.sleep(1.0)
			 temStr = prs[lpZoom]
		     typeAnim("Alright. In what category would your product, " , speed=0.02)
			 print(temStr)
			 typeAnim("be in?" , speed=0.04)
	         time.sleep(1.0)
			 print("")
			 time.sleep(1.0)
             for index, val in enumerate(prCategories):
               print(" {}: {}".format(index, val))
			   
	         time.sleep(0.05)
	         temCatg = input("Select from the 5 categories mention below, by its corresponding number. eg: 2, for (Food)")
		     time.sleep(0.05)
			 
			 failsafeA = len(prCategories)
			 failsafeA = int(failsafeA)
			 temCatgFS = int(temCatg) # converts catgory string into input for the if statement
			 #print(failsafeA , temCatgFS) #debug
			 if temCatgFS > failsafeA:
			   print("")
		       typeAnim("That isn't a real category :)" , speed=0.04)
	           print("") 
			   time.sleep(1.0)
			   print("")                              
               typeAnim("Reverting Data." , speed=0.03)
			   time.sleep(0.5)
			   print("")
			   typeAnim("...", speed=1.5)
			   time.sleep(0.1)
			   print("")
			   productWizrd()

			 
		     typeAnim("Now give a price for your product." , speed=0.02)
			 time.sleep(1.0)
			 cost[lpZoom] = input("Set a price for your product, " + prs[lpZoom] + " Any decimal and natural int values are admitted.")
			 
			 # A S S I G N ID for product 
			 time.sleep(0.05)
			 print("")
			 idPR[lpZoom] = temCatg #itemCatg (Category)
	         #print(idPR[lpZoom]) #test to check if the id was succesfully set	
			 print("")
			 
			 #print(lpZoom, iPR) #DEBUG | To check the current loop turn or index
			 if lpZoom < iPR:
		       typeAnim("Alright, Let's head to fill the details of the next product." , speed=0.02)
			   time.sleep(1.0)			   
		curMD = 2
		#print(curMD) #more dubug print functions
		print("")
		typeAnim("Now," , speed=0.02)
		time.sleep(0.5)	
		curMD == 2
              

    if curMD == 1:
        productWizrd()
 
    # SETUP T A X E S  C O S T
	print("")
    typeAnim("Set the percentage for the Tax Addition. (Just set the number, DO NOT add the % symbol.)  A percentage like 1 would be the ideal tax." , speed=0.04)
	print("") 
	time.sleep(1.0)	
	tax = float(input("Set the percentage for the Tax Addition. (Just set the number, DO NOT add the % symbol.)  "))

	
	
    def receiptSim():
        #print(prCategories)
		print("")
		typeAnim(". . ." , speed=0.8)
		print("")
		time.sleep(1.0)	
		
		print("")
		typeAnim("Welcome! " , speed=0.05)

		
		time.sleep(1.0)
		global cart
		cart = [0,0,0,0,0,0,0,0,0,0]
		global itemQ 
		itemQ = [0,0,0,0,0,0,0,0,0,0]
		global paymentString
		paymentString = ["Receipt (Free)","1","2","3","4","5","6","7","8","9"]
		global cartMode
		cartMode = 1 #1 for yes
		global subTotal
		subTotal = 0
		

		global lp
		lp = 1
		#for i in range(0, 9):
		while cartMode != 2:  #loops until cartMode matches 2
		    #print("works") #debug thing
		  
		    #IF STATEMENTS for channeling final modes	

		    if cartMode == 1:
		    
		      time.sleep(0.5)			
		      print("")
		      iPRFix = iPR - 1
              #for index, val in enumerate(prs):
			  
			  print("")
		      typeAnim("What product would you like to buy?" , speed=0.05)
			  print("")
		      for index in range(min(iPR + 1, len(prs))): #in order to avoid th eprogram from reapiting the loop from how many items are or doing less than the items available.
		         iPRtem = prs[index] #ipr is temporal var fro the print statement below
                 print(" AVAILABLE {}: {}".format(index, iPRtem ) + "     $"+str(cost[index]))
			  time.sleep(0.5) 
			  item = int(input("Which item would you like to buy? (eg: 2 for Bread)"))
			
		      cart[item] = cart[item] + 1 
		      #print(cart[item]) debug,check if works
		      print("")
		      typeAnim("Sounds like a great choice! How much " , speed=0.05)
		      print(prs[item] + ", ")
		      print("would you like to buy?")
		      time.sleep(1.0)
		      time.sleep(0.5)
			
		      itemQD = int(input("How much " + prs[item] + ",  would you like to buy? (Write only the amount, eg: 2 for 2 apples))"))
		      itemQ[item] = itemQD #item Quantity Data
			  time.sleep(0.5)
		      print("")	
		      typeAnim("Are there any more things you want to buy?" , speed=0.05)
		      time.sleep(1.0)
	          typeAnim("  [ Y / N ]" , speed=0.04)
		  
		      global userBoolean
		      userBoolean = "U" #as for unknown
			   
			#T A X CALCUALTION | calculates item and adds tax amount
			global taxC
			
			n = float(cost[item]) #temporal var for cost and index item of array
			nt = float(tax) # temporal var for float
			   
			taxC = n * (nt / 100.00) #tax is calculated by dividing n with 100
			taxPRS[item] = taxPRS[item] #saves the tax value to the array for later calculation :D
			totalCost[item] = float(taxC) + float(cost[item])
			# tempvars
			qd = float(totalCost[item]) * float(itemQ[item]) #quantity data wich multiplies the amount of times the user wants to buy the same product with the product price
			subTotal += qd
			ctd = int(idPR[item]) #category data
		    psip = str(itemQ[item]) + " " + str(prs[item]) + "   |   $" +  str(qd) + "   |   "   #payment string index preview
			paymentString[lp] = psip + prCategories[ctd]
		    #print(paymentString[item])		#for dubug if the string that showcases everything works	
		  
		    time.sleep(0.5)
		    userBoolean = input("Are there any more things you want to buy? (Y for Yes, N for no)")
			
			if userBoolean in ["N", "n"]: #breaks loop if user has bought everything they want.
			   cartMode = 2
			   break
			   
			elif userBoolean in ["Y","y"]:

			   cartMode = 1
			   #print("user pressed yes") #debug
			   lp += 1
			   
			
		  #elif cartMode == 2:		
		    #break
       
	   
        # FINALLY THE , R E C E I P T

		#for num in cost: #adds every products cost into 1
        #   subTotal += cost(num)
		#subTotal = float(sum(cost))
		taxTotal = subTotal * (tax / 100)
		total = taxTotal + subTotal #adds both for the total of the receipt
		  
	    print("")
	    time.sleep(1.0)
		typeAnim("...", speed=1.2)	
		
		#important calculations (for taxes, subtotal)
		
		
		time.sleep(0.5)
		
		# receipt render
		print(" ")
		typeAnim("Your Order: ", speed=0.06)
		print(" ")
		print(" ")
		typeAnim(" Item                         Cost      Category ", speed=0.05)
		print("  ")
		
		for index in range(min(iPR + 1, len(prs))): #in order to avoid th eprogram from reapiting the loop from how many items are or doing less than the items available.
		   iPRtemB = paymentString[index] #ipr is temporal var fro the print statement below
           print(" {}".format(iPRtemB) + " ")		
		
		print(" ")
		#print(str(lp) + " " + str(iPR)) #debug var
		typeAnim("-----------------------------------------------", speed=0.03)	
		print(" ")
		print("  Subtotal:                                     $" + str(subTotal))
		print("  Tax:                                          $" + str(taxTotal))
		print("  Order Total:                                  $" + str(total))
		
		print(" ")
		typeAnim("We appreciate You for shopping with us!" , speed=0.05)
		print(" ")
		
		
	
    receiptSim()		
	
	typeAnim("PROGRAM HAS ENDED" , speed=0.05)
	print(" ")
	typeAnim("\ (•◡•) /  " , speed=0.05)

    
	

cubeSequel()  

#hope you had fun testing the code!
