width=70
print("="*width)

print("$" + "Welcome to Blue Collar Q Project Estimator".center(width-2) + "$")
print("$" + "Prototype by Destiny Acuna".center(width-2) + "$")

print("="*width)
#Using end to format without having to type all the equals and keep next thing
#   on same line
print("\n")

def compute_labor(foreman_size, crew_size, foreman_hours, crew_hours,
                  foreman_rate, crew_rate):
    """
    computes labor costs for foreman leads and crew.
    """
    foreman_labor=foreman_size*foreman_hours*foreman_rate
    crew_labor=crew_size*crew_hours*crew_rate
    total_labor=foreman_labor+crew_labor
    return foreman_labor, crew_labor, total_labor
def compute_direct_cost(materials_total, subcontractor_total, disposal_total,
                       total_labor, risk_factor):
    """
    computes direct costs before and after risk level is assessed
    """
    direct_before_risk=materials_total + subcontractor_total + \
                        disposal_total + total_labor
    direct_after_risk=direct_before_risk*(1.05**risk_factor)
    return direct_before_risk, direct_after_risk
def compute_overhead(direct_after_risk, overhead_percentage):
    overhead_cost=direct_after_risk*(overhead_percentage)
    """
    gets the direct cost after risk has been evaluated and overhead\
    percent and returns the overhead cost
    """
    return overhead_cost
def compute_cost_basis(direct_after_risk, overhead_cost, profit_margin):
    cost_basis=direct_after_risk+overhead_cost
    return cost_basis
def compute_price(cost_basis, profit_margin):
    final_price=cost_basis/(1-profit_margin)
    return final_price
def format_money(value):
    """this formats a number as a dollar amount with 2 decimal places
    """
    return"${:,.2f}".format(value)
def main():
#I used google to figure out how to store past estimates if we wanted to look back
    past_estimates=[]
    
    keep_running=True
    while keep_running:
        
        user_choice=input("""Press 1 to create a new estimate, Press 2 to view previous estimates,
                            Press any other character to QUIT. """)
        if user_choice== "1":
            print("=========== LABOR ===========")
            foreman_size=int(input("How many foreman positions on site? "))
            crew_size=int(input("How big of a crew on site? "))
            foreman_hours=0
            while foreman_hours<=0:
                foreman_hours=int(input("Foreman hours worked? "))
                if foreman_hours<=0:
                    print("Error, please try again")
            crew_hours=0
            while crew_hours<=0:
                crew_hours=int(input("Crew hours worked? "))
                if crew_hours<=0:
                    print("Error, please try again")
            foreman_rate=float(input("Enter foreman hourly rate "))
            crew_rate=float(input("Enter crew member hourly rate "))
            print("\n\n")
            print("========= MATERIALS =========")
            materials_total=0.0
            item_count=int(input("How many items were purchased? "))
            for i in range(1, item_count+1):
                cost=float(input(f"Enter cost for item {i}: "))
                materials_total += cost
                
            subcontractor_total=float(input("Enter subcontractor costs "))
            disposal_total=float(input("Enter any dumping fees "))
            print("\n\n")
            print("========== COMPANY ==========")
            overhead_percentage=float(input("Enter company overhead as a decimal "))
            profit_margin=float(input("Enter company mandated profit margin as a decimal "))
            risk_factor=float(input("Scale of 0-3 how big are the risks associated? "))

#calculations
            foreman_labor, crew_labor, total_labor=compute_labor(foreman_size, crew_size, foreman_hours, crew_hours,
                      foreman_rate, crew_rate)
            direct_before_risk, direct_after_risk=compute_direct_cost(materials_total,subcontractor_total,
                                                                      disposal_total,total_labor, risk_factor)
            overhead_cost=compute_overhead(direct_after_risk, overhead_percentage)
            cost_basis=compute_cost_basis(direct_after_risk, overhead_cost, profit_margin)
            final_price=compute_price(cost_basis, profit_margin)
            print("====== Estimate Results ======")
            print("Foreman Labor:", format_money(foreman_labor))
            print("Crew Labor:", format_money(crew_labor))
            print("Total Labor:", format_money(total_labor))
            print("Direct Cost w/o Risk Applied:", format_money(direct_before_risk))
            print("Direct Cost w/ Risk Applied:", format_money(direct_after_risk))
            print("Overhead Cost:", format_money(overhead_cost))
            print("Cost Basis:", format_money(cost_basis))
            print("Sell for Final Price of:", format_money(final_price))

#stores estimates so you can look back
            past_estimates.append(final_price)
                  
        elif user_choice== "2":
            print("======= Past Estimates =======")
            if len(past_estimates)==0:
                print("No previous estimates")
            else:
                for price in past_estimates:
                    print(format_money(price))
        else:
            print("Ending program...")
            keep_running=False
main()
