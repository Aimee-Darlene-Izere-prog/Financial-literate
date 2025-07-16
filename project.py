'''
    This code simulate how much money a financially literate versus a non-financially literate person
    has after 40 years making small financial decisions in how to save,
    and when to buy a house

    Author: Aimee Darlene Izere
'''

class Person:
    '''
        This class simulate the financial literacy of two people, a financially literate (fl)
        and a non-financially literate (fl).
        Those two person are represented by the parameter "person_ident"
    '''
    def __init__(self,checking, person_ident, loan = 0):
        '''
        Initialize savings, checking, debt, loan, house, and person_ident attributes
        The initial balnce is equal to $5000 for both person
        And the initial debt for all people is equal to $30100
        '''
        self.savings = 5000
        self.checking = checking
        self.debt = 30100
        self.loan = loan
        self.house = False # Determine if a person has a house or not 
        self.person_ident = person_ident
    
    def get_savings_yearly(self):
        '''
        Updating the amount the person has in the savings account after one year.
        A financially literate has an annual interest of 7%,
        Whereas, a non-financially literate person has an annual interest of 1% 

        This method doesn't take parameters and does not return anything
        '''
        if self.person_ident == "fl":
            self.savings += (self.savings * 0.07)
        
        elif self.person_ident == "nfl":
            self.savings += (self.savings * 0.01)   
    
    def get_debt_balance_yearly(self):
        """
        Calculates the debt balance and amount left in the checking account after one year.
        Each month, a person pays 3% of their remaining debt plus an additional fixed amount.
        That additional fixed amount for a financially literate (fl) is $15, 
        and for a non-financially literate (fl) is $1. 

        The debt payment should stop on the month that the debt is <= $0
        If debt is not fully paid off after 12 months, a 20% interest is applied to the remaining debt.

        Returns:
            paid_debt_amount(float): Total debt payment amount for the year.
        """
        month = 0
        remaining_debt = self.debt   
        paid_debt_amount = 0  # Track total debt payment amount for the year

       
        while remaining_debt > 0 and month < 12:
            month += 1

            if self.person_ident == "fl":
                monthly_debt_payment = (remaining_debt * 0.03) + 15

            elif self.person_ident == "nfl":
                monthly_debt_payment = (remaining_debt * 0.03) + 1

            # Pay the exact amount left in the debt account
            if monthly_debt_payment >= remaining_debt:
                monthly_debt_payment = remaining_debt 

            # Calculating the amount of money a person have left in their checking, and debt accounts 
            # after paying the company
            self.checking -= monthly_debt_payment
            remaining_debt -= monthly_debt_payment
            paid_debt_amount += monthly_debt_payment

            # Update debt balance
            self.debt = remaining_debt  

            # Stop calculating the remaining debt if it is fully paid
            if remaining_debt <= 0:
                remaining_debt = 0
                break

        # if the debt is still over $ 0 after a year, the interested rate required 
        # by the company increase to be (remaining_debt * 1.2 )
        if remaining_debt > 0:
            remaining_debt *= 1.2
            self.debt = remaining_debt
            
        return paid_debt_amount   
            
    def subtract_rent_payment_from_checking_account(self):
        '''
            Updating the amount of money a person will have left in their checking accounts
            after one year if they are renting an apartment.
            The cost per month is $850
 
            This method does not retun anything
        '''

        monthly_renting_cost = 850
        for month in range (12):
            # The money to pay rent comes out of the checking account
            self.checking -=  monthly_renting_cost
        
    def subtract_mortgage_payment_from_checking_account(self):
        '''
            Calculates the amount of money a person will have left in their checking and loan checking accounts
            after paying the mortgage.
            The interest on the loan for a fl person is 4.5%,
            and for a nfl person if 5%

            A person should stop paying mortage after they have paid off their loan.

            This method does not return anything

        '''
        
        num_payments = 360
        if self.person_ident == "fl":
            loan_interest_rate_per_month = 0.045 / 12
        
        elif self.person_ident == "nfl":
            loan_interest_rate_per_month = 0.5 / 12

        discount_factor = ((loan_interest_rate_per_month + 1) ** (num_payments - 1))/(loan_interest_rate_per_month * (1 + loan_interest_rate_per_month) ** num_payments)
        monthly_mortage_payment = 175000 / discount_factor

        for month in range(12):
            if self.loan > 0:
                self.checking -=  monthly_mortage_payment
                self.loan -= monthly_mortage_payment
            else:
                self.loan = 0
                break
        
def run_tests():
    # TEST CASES 1 on get_savings_yearly() method: 
    # Testing the methods on a financially literate person (fl)

    fl_person = Person(1000,"fl")
    fl_person.get_savings_yearly()
    assert fl_person.savings == 5350 , "Error in get_savings_yearly() method"

    fl_person.savings = 0
    fl_person.get_savings_yearly()
    assert fl_person.savings == 0 , "Error in get_savings_yearly() method"

    # Testing the methods on a non-financially literate person (nfl)
    fl_person_nfl = Person(1000,"nfl")
    fl_person_nfl.get_savings_yearly()
    assert fl_person_nfl.savings == 5050 , "Error in get_savings_yearly() method"

    fl_person_nfl.savings = 0
    fl_person_nfl.get_savings_yearly()
    assert fl_person_nfl.savings == 0 , "Error in get_savings_yearly() method"
    print ("TEST CASES 1 passed")

     # TEST CASES 2 on get_debt_balance_yearly() method
    # Testing the methods on a financially literate person (fl)
    
    fl_person1 = Person(2000,"fl") 
    assert fl_person1.get_debt_balance_yearly() >= 9368.42, "Error in get_debt_balance_yearly() method"
    assert fl_person1.debt >= 24877.89, "Error in get_debt_balance_yearly() method"
    assert fl_person1.checking >=  -7368.424 , "Error in get_debt_balance_yearly() method"

    # Testing the methods on a non-financially literate person (nfl)

    fl_person11 = Person(2000,"nfl")
    assert fl_person11.get_debt_balance_yearly()>= 9225.55, "Error in get_debt_balance_yearly() method"
    assert fl_person11.debt >= 25049.33, "Error in get_debt_balance_yearly() method"
    assert fl_person11.checking >= -7225.6 , "Error in get_debt_balance_yearly() method"
    print ("TEST CASES 2 passed")

    # TEST CASES 3 on subtract_rent_payment_from_checking_account() method

   # Testing the methods on a financially literate person (fl)
    fl_person2 = Person(2000,"nfl")
    fl_person2.subtract_rent_payment_from_checking_account() 
    assert fl_person2.checking == -8200, "Error in subtract_rent_payment_from_checking_account() method"
    
    fl_person20 = Person(0,"nfl")
    fl_person20.subtract_rent_payment_from_checking_account()
    assert fl_person20.checking == -10200, "Error in subtract_rent_payment_from_checking_account() method" 
  
    # Testing the methods on a non-financially literate person (nfl)
    fl_person21 = Person(2000,"nfl")
    fl_person21.subtract_rent_payment_from_checking_account() 
    assert fl_person21.checking == -8200, "Error in subtract_rent_payment_from_checking_account() method"
    print ("TEST CASES 3 passed")


    # # TEST CASES 4 on subtract_rent_payment_from_checking_account() method

    # Testing the methods on a financially literate person (fl)
    fl_person3 = Person(7089, "fl")
    fl_person3.loan = 100 
    fl_person3.subtract_mortgage_payment_from_checking_account()
    assert fl_person3.checking <= 6430.29, "Error in subtract_rent_payment_from_checking_account() method"
    assert fl_person3.loan == 0,"Error in subtract_rent_payment_from_checking_account() method"

    fl_person3.loan = - 100
    assert fl_person3.checking <= 7089, "Error in subtract_rent_payment_from_checking_account() method"
    # Testing the methods on a non-financially literate person (nfl)
    
    fl_person4 = Person(7089,"nfl")
    fl_person4.loan = 100 
    fl_person4.subtract_mortgage_payment_from_checking_account()
     
    assert fl_person4.checking == -506.4861111111104, "Error in subtract_rent_payment_from_checking_account() method"
    assert fl_person4.loan == 0,"Error in subtract_rent_payment_from_checking_account() method"
    fl_person4.loan = - 100
    assert fl_person4.checking <= 7089, "Error in subtract_rent_payment_from_checking_account() method"
    print("TEST CASES 4 passed")


    # Testing the Simulation Method 
    # Simulation of a financially literate person
    pers = Person(1200,"fl")
    sim_person = Simulation(pers)
    sim_person.simulation()
    assert sim_person.total_amount_paid_debt == 51714.555292170844 , "Error in Simulation"
    assert sim_person.years_renting_a_house == 11 , "Error in Simulation"
    assert sim_person.years_remained_in_debt == 28 , "Error in Simulation"

    # Simulation of a non_financially literate person
    pers1 = Person(1200,"nfl")
    sim_person1 = Simulation(pers1)
    sim_person1.simulation()
    assert sim_person1.total_amount_paid_debt == 54652.69873291382 , "Error in Simulation"
    assert sim_person1.years_renting_a_house == 6 , "Error in Simulation"
    assert sim_person1.years_remained_in_debt == 33 , "Error in Simulation"

    print("TESTS CASES ON SIMULATION passed")



class Simulation:
    '''
        Simulate how much money a person will have after 40 years of making small financial decisions
        Parameter: person(a person object)
    '''  
    def __init__(self,person):
       self.person = person
       self.price_house = 175000
       self.person.loan = self.price_house # Before subtracting the down payment
       self.years_remained_in_debt = 0
       self.years_renting_a_house = 0
       self.total_amount_paid_debt = 0
       
    def simulation(self): 
        '''
            Updating the money in each account. 

            Returns: 
                wealth(a list of int): contains 41 elements, each element represents the wealth the inputted person had each year.
            
            The initial wealth is equal to -25100
        '''
        
        wealth = [-25100]
        initial_amount = 59000
        
        for year in range (40):
            # Check if a person is still renting a house or have unpaid debt at the beginning of the year
            #print(f"loan {self.person.loan}")
            if self.person.loan > 0 or self.person.debt > 0:
                self.years_remained_in_debt += 1
            #print(f"have a house: {self.person.house}")
            if self.person.house == False:
                self.years_renting_a_house += 1

            # Money received at the start of each year
            self.person.checking += (initial_amount * 0.3)
            self.person.savings += (initial_amount * 0.2)

            # Updating savings and debt methods 
            paid_debt = self.person.get_debt_balance_yearly()
            #print (f"Paid debt annually: {paid_debt}")
            self.total_amount_paid_debt +=  paid_debt
            self.person.get_savings_yearly()

            # Pay rent until they buy a house
            if self.person.house == False:
                self.person.subtract_rent_payment_from_checking_account()

            # Calculate the down payment for fl of nfl person 
            if self.person.person_ident == "nfl":
                down_payment = self.price_house * 0.05
            elif self.person.person_ident == "fl":
                down_payment = self.price_house * 0.2

            if self.person.checking >= down_payment and self.person.house == False:
                self.person.house = True
                self.person.checking -= down_payment

                # Updating loan 
                self.person.loan -= down_payment

            # Pay mortage when owning a house
            if self.person.house == True and self.person.loan > 0:
                self.person.subtract_mortgage_payment_from_checking_account()
            
            total_money_in_all_accounts = round (self.person.savings + self.person.checking - (self.person.debt + self.person.loan))
            wealth.append(total_money_in_all_accounts) 
            #print(wealth)

        return wealth  

# # # # MAIN PROGRAM # # # #

def main ():
    fl = Person (0, "fl")
    nfl = Person (0, "nfl")

    # Run the simulation 
    nfl_sim = Simulation(nfl)
    fl_sim = Simulation (fl)

    nfl_info = nfl_sim.simulation()
    fl_info = fl_sim.simulation()

    print()
    print("After 40 year:")
    print(f"A financially literate person will have:\n $ {round(fl.checking)} in their checking account and  ${round(fl.savings)} in their savings account")
    print(f"A non-financially literate person will have:\n $ {round(nfl.checking)} in their checking account and ${round(nfl.savings)} in their savings account")
    print("***********************************************************************************************************************************************************")
    print (f"A financially literate person remained in debt for: {fl_sim.years_remained_in_debt} year")
    print (f"A non-financially literate person remained in debt for: {nfl_sim.years_remained_in_debt} year")
    print("*************************************************************************************************")
    print (f"A financially literate person rented a house for {fl_sim.years_renting_a_house} years" )
    print (f"A non-financially literate person rented a house for {nfl_sim.years_renting_a_house} years" )
    print("**********************************************************************************************")
    print(f"A financially literate person paid off the debt a total amount of $ {round(fl_sim.total_amount_paid_debt)} ")
    print(f"A non-financially literate person paid off the debt a total amount of $ {round(nfl_sim.total_amount_paid_debt)} ")

    
if __name__ == "__main__":
    main () 
   
print("\n")
run_tests()

    

