from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def compute(request):
    allotment = int(request.GET['allotment'])
    finalSharePrice = int(request.GET['finalSharePrice'])
    sellCommission = int(request.GET['sellCommission'])
    initialSharePrice = int(request.GET['initialSharePrice'])
    buyCommission = int(request.GET['buyCommission'])
    capitalGainTaxRate = int(request.GET['capitalGainTaxRate'])
    
    proceeds = (allotment * finalSharePrice)
    totalPurchasePrice = (allotment * initialSharePrice)
    totalTax = (((finalSharePrice - initialSharePrice) * allotment) - buyCommission - sellCommission)
    taxOnCapitalGain = (totalTax * (capitalGainTaxRate/100))
    cost = ((allotment * initialSharePrice) + buyCommission + sellCommission + taxOnCapitalGain)
    netProfit = (totalTax - taxOnCapitalGain)
    returnOnInvestment = ((netProfit / cost) * 100)
    finalSharePrice = ((totalPurchasePrice + buyCommission + sellCommission) / allotment)

    return render(request, "home.html", 
    {
    "proceeds": proceeds, 
    "cost": cost,
    "totalPurchasePrice": totalPurchasePrice, 
    "buyCommission": buyCommission,
    "sellCommission": sellCommission,
    "taxOnCapitalGain": taxOnCapitalGain, 
    "netProfit": netProfit,
    "returnOnInvestment": returnOnInvestment,
    "finalSharePrice": finalSharePrice
    })

