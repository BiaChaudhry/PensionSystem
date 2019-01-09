#THIS PROGRAM IS MADE TO CALCULATE PENSION OF AN EMPLOYEE

print("                                     {{{  PENSION CALCULATOR  }}}                                    ")

def pensionCalculator(nameOfEmployee,salary,basicPay,age,marriedOrNot,months,monthsM,dateOFservice,dateOfRetirement,totalTax ):

	if age < 45 and marriedOrNot == "Married":                   #HERE TERMS LIKE SAL1 , SAL2 , SAL3 ARE THE PARTS OF PENSION                  
		print(basicPay)
		sal1    = basicPay * 2 * months
		pension = sal1 * 2
		print("Pension : ", pension)
		print("And your net Salary is :", sal1 )

	elif age < 45 and  marriedOrNot == "unMarried" :
		houseRent = basicPay * (15 / 100 )
		netPay    = basicPay + houseRent
		sal1      = basicPay * 2 * months
		sal2      = netPay * 2
		pension   = sal1 +  sal2
		print("Pension:", pension)
		print("And your net Salary is :", basicPay + houseRent )
		
	elif   45 < age <= 55   and marriedOrNot == "Married":
		OldAgeAllow = basicPay * (10 / 100 )
		netPay      = basicPay + OldAgeAllow
		sal1        = basicPay * 2 * months
		sal2        = netPay * 2
		pension     = sal1  + sal2
		print("Pension :", pension)
		print("And your net Salary is :", basicPay  + OldAgeAllow )
		
	elif 45 < age <= 55   and  marriedOrNot == "unMarried" :
		OldAgeAllow = basicPay * (10 / 100 )
		houseRent   = basicPay * (15 / 100 )
		netPay      = basicPay + OldAgeAllow + houseRent
		sal1        = basicPay * 2 * months
		sal2        = houseRent * monthsM
		sal3        = OldAgeAllow * 3
		sal4        = netPay * 2
		pension     = sal1 + sal2 + sal3 + sal4 
		print("Pension:", pension)
		print("And your net Salary is :", basicPay + houseRent + OldAgeAllow )
		
	elif age > 55 and marriedOrNot == "Married" :
		OldAgeAllow = basicPay * (15 / 100)
		netPay      = basicPay + OldAgeAllow
		sal1        = basicPay * 2 * months
		sal2        = netPay * 2
		pension     = sal1 + sal2
		print("Pension : ", pension)
		print("And your net Salary is :", basicPay  + OldAgeAllow )  
		
	elif age > 55 and  marriedOrNot == "unMarried" :
		OldAgeAllow = basicPay * (15 / 100)
		houseRent   = basicPay * (15 / 100 )
		netPay      = basicPay + OldAgeAllow + houseRent
		sal1        = basicPay * 2 * months
		sal2        = houseRent * monthsM
		sal3        = OldAgeAllow * 3
		sal4        = netPay * 2
		pension     = sal1 + sal2 + sal3 + sal4 
		print("Pension :", pension)
		print("And your net Salary  :", basicPay + houseRent + OldAgeAllow )


	print("Thankyou Dear :" , nameOfEmployee , "We are very glad and satisfied with your service for :" , months , "months" )

	print("The pension has been calculated by your given data:")

	print("Age : ", age )

	print("Married Or not : ", marriedOrNot)

	print("date since you start service : ", dateOFservice)

	print("date when you retired : " , dateOfRetirement)

	print("after deduction of taxes : ", totalTax)

	print("your Basic pay is : ", basicPay)

	print("As you worked at our organization for :",months,"months")

	print("Again we thank you for your Service")


def main():
	#THIS FUNCTION IS TAKING INPUTS REQUIRED TO CALCULATE PENSION ALSO HERE DATE IS BEING CONVERTED INTO NO. OF MONTHS FOR :
	#1) DATE OF JOINING THE SERVICE 2) DATE OF RETIREMENT 3) DATE FROM JOINING TO MARRIAGE
	nameOfEmployee      =  input("Enter your name Please:")
	age                 =  int(input("Enter your age :"))
	marriedOrNot        =  input("Tell whether you are Married or unMarried:")
	salary              =  int(input("Enter your salary:"))
	incomeTax           =  salary * (7 / 100)
	provincialTax       =  salary * (5 / 100)
	totalTax            =  incomeTax + provincialTax
	basicPay            =  salary - totalTax
	dateOFservice       =  input("Enter date of Joining the Company in format:'20-13-2013':")
	dateOfRetirement    =  input("Enter date of retirement in format:'20-13-2013':")
	dateSinceMarried    =  input("Enter date since Married in format:'20-13-2013':")

	date1               =  int(dateOFservice[0:2])
	month1              =  int(dateOFservice[3:5])
	year1               =  int(dateOFservice[6:])
	date2               =  int(dateOfRetirement[0:2])
	month2              =  int(dateOfRetirement[3:5])
	year2               =  int(dateOfRetirement[6:])                

	d1                  =  365*year1 + year1/4 - year1/100 + year1/400 + date1 + (153*month1+8)/5     # FORMULA TO CONVERT DATE INTO DAYS THIS SAME FORMULA IS USED IN UNDERLYING CODE
	d2                  =  365*year2 + year2/4 - year2/100 + year2/400 + date2 + (153*month2+8)/5     # d2 - d2 IS THE NO. OF DAYS FROM JOINING TO RETIREMENT
	days                =  d2 - d1
	months              =  int(days / 30 )                                                            # GIVING MONTHS FROM JOINING TO RETIREMENT
	date3               =  int(dateSinceMarried[0:2])
	month3              =  int (dateSinceMarried[3:5])
	year3               =  int(dateSinceMarried[6:])
	date4               =  int(dateOFservice[0:2])
	month4              =  int(dateOFservice[3:5])
	year4               =  int(dateOFservice[6:])
	
	d3                  =  365*year3 + year3/4 - year3/100 + year3/400 + date3 + (153*month3+8)/5        
	d4                  =  365*year4 + year4/4 - year4/100 + year4/400 + date4 + (153*month4+8)/5
	daysM               =  d4 - d3                                                                     # GIVING NO. OF DAYS FROM JOINING TO MARRIAGE
	monthsM             =  int(daysM / 30 )                                                            # CONVERTING DAYS SINCE MARRIAGE INTO MONTHS

	pensionCalculator(nameOfEmployee,salary,basicPay,age,marriedOrNot,months,monthsM,dateOFservice,dateOfRetirement,totalTax)
main()