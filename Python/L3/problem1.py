def payTheMin():
        """Calculate the annual payment when someone only services the minimum amount. 
                Use 3 floats to take user input and handle the calculation"""
        bal = float(raw_input('Enter the outstanding balance on your credit card '))
        air = float(raw_input('Enter the annual credit card interest rate as a decimal '))
        mmr = float(raw_input('Enter the minimum monthly payment rate as a decimal '))
        TotalAmountPaid = 0
        
#        print(bal,air,mmr)
        print('================= STARTING Calculations ==============')
        for i in range(1, 13):
                print 'Month:', i
                MinMonPay = mmr * bal
                print 'Minimum monthly payment: $',round(MinMonPay, 2)
                IntPaid = (air / 12) * bal
                PrinPaid = MinMonPay - IntPaid
                print 'Principal paid: $',round(PrinPaid, 2)
                bal = bal - PrinPaid
                print 'Remaining balance: $',round(bal,2)
                TotalAmountPaid += MinMonPay
                if i == 12:
                        print 'RESULT'
                        print 'Total amount paid: $', round(TotalAmountPaid, 2)
                        print 'Remaining balance: $',round(bal,2)
                        
##                print("Minimum monthly payment =",MinMonPay,"Interest Paid =",IntPaid,"Principal paid =",PrinPaid, "Balance remaining =", bal)
                
##        print("Total amount paid =", TotalAmountPaid) 
                
        
def payTheMax():
        bal = float(raw_input('Enter the outstanding balance '))
        air = float(raw_input('Enter the annual interest rate '))
        MinMonPay = 10
        NoOfMons = 1
        MonIntRate = air / 12.0
        
        print('Starting Calculations......')
        bal = bal * (1.0 + air)
        for pay in range(1, bal):
                NoOfMons = bal / (float(pay) * 10.0)
                IntBal = bal - MinMonPay 
                if NoOfMons <= 12.0:
                        MinMonPay = pay * 10
                        print 'It would take', NoOfMons, 'months'
                        print 'It might be wise to pay', MinMonPay, 'per month'
                        print 'Your balance will be', IntBal
                        break
                
##                elif (int(bal) / (pay * 10)) == 12:
##                        MinMonPay = pay * 10
##                        print 'It would take 12 months to pay ', MinMonPay
##                        break
                
        


        
