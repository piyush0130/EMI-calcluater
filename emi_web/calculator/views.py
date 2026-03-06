from django.shortcuts import render
from django.http import HttpResponse

def calculate_emi(principal, annual_interest_rate, months):
    if annual_interest_rate == 0:
        return principal / months
        
    monthly_rate = (annual_interest_rate / 12) / 100
    emi = principal * monthly_rate * ((1 + monthly_rate) ** months) / (((1 + monthly_rate) ** months) - 1)
    return emi

def calculator_view(request):
    context = {}
    
    if request.method == 'POST':
        try:
            price = float(request.POST.get('price', 0))
            downpayment = float(request.POST.get('downpayment', 0))
            annual_interest_rate = float(request.POST.get('interest_rate', 0))
            months = int(request.POST.get('months', 0))
            interest_type = request.POST.get('interest_type', 'reducing')
            
            if downpayment > price:
                context['error'] = "Downpayment cannot be greater than the total price!"
            elif months <= 0:
                context['error'] = "Months must be greater than 0!"
            else:
                principal = price - downpayment
                
                if interest_type == 'flat':
                    total_interest = principal * (annual_interest_rate / 100) * (months / 12)
                    total_payment = principal + total_interest
                    emi = total_payment / months if months > 0 else 0
                else:
                    emi = calculate_emi(principal, annual_interest_rate, months)
                    total_interest = (emi * months) - principal
                    total_payment = emi * months
                
                context.update({
                    'result': True,
                    'price': price,
                    'downpayment': downpayment,
                    'principal': principal,
                    'interest_rate': annual_interest_rate,
                    'interest_type': interest_type,
                    'months': months,
                    'emi': emi,
                    'total_interest': total_interest,
                    'total_payment': total_payment,
                    'overall_cost': price + total_interest
                })
        except ValueError:
            context['error'] = "Invalid input! Please enter proper numeric values."
            
    return render(request, 'calculator/calculator.html', context)
