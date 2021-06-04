# # Tip calculator:
# Create a Tip calculator (or rather a function for a tip calculator)!

# ------ Version 1 with interactive input

# defining input Variables (with a default value)
# input_percentage = float(
#   input("How much tip do you like to give (in percent)?: ") or 10)
#input_bill = float(input("Bill amount: ") or 80)
#input_guest = int(input("Number of guests: ") or 2)


def tip_calculator(percentage, bill, guest):
    tip = (bill*(percentage/100))/guest
    return round(tip, 2)


def bill_amount(percentage, bill, guest):
    guest_bill = (bill+(bill*(percentage/100)))/guest
    return round(guest_bill, 2)


# print(
    # f"Each guest needs to pay {bill_amount(input_percentage, input_bill, input_guest)} Euro. The amount of tip for each guest is {tip_calculator(input_percentage, input_bill, input_guest)} Euro.")

# ------ Version 2 without interactive input
percentage = 0.1
bill = 80.00
guest = 2


def tip_calculator2(bill, guest):
    tip = (bill*percentage)/guest
    return round(tip, 2)


def bill_amount2(bill, guest):
    guest_bill = (bill+(bill*percentage))/guest
    return round(guest_bill, 2)


# Version 3 (after class discussion)
guest = 2
bill = 80
tip = 10


def tip_calculator3(percentage, bill, guest):
    tip = (bill*(percentage/100))/guest
    round(tip, 2)
    guest_bill = (bill+(bill*(percentage/100)))/guest
    round(guest_bill, 2)
    return(f"Everyone needs to pay {guest_bill} Euro. This includes {tip} Euro tip per person.")

#print(tip_calculator(input_percentage, input_bill, input_guest))
