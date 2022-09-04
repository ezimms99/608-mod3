
"""Creating a custom object with corresponding methods"""

#This represents our purchase
class Purchase(object):
    def __init__(self, amount):
        self.amount = amount
    def calculateTax (self, taxPercent):
        return self.amount * taxPercent/100.0
    def calculateTip(self, tipPercent):
        return self.amount * (tipPercent/100.0)
    def calculateTotal(self, taxPercent, tipPercent):
        return self.amount * (1 + taxPercent/100.0 + tipPercent/100.0)

#Create a purchase
purchase = Purchase(100.0)

#Define Variables
taxPercent = 7.5
tipPercent = 20.0

#Tax and Tip calcs
tax = purchase.calculateTax(taxPercent)
tip = purchase.calculateTip(tipPercent)

#Display
print('Tax', tax)
print('Tip', tip)
print('Total:', purchase.calculateTotal(taxPercent, tipPercent))