from crypt import methods
from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as current_app

app = Flask(__name__, static_url_path='/static')
@app.route('/')
def main_get(num=None):
    return render_template('test.html', x=num)

@app.route('/calculate', methods=['POST', 'GET'])
def calculate(num=None):


if __name__ == '__main__':
    # threaded=True 로 넘기면 multiple plot이 가능해짐
    app.run(debug=True, threaded=True)

#print('값을 입력해주세요:')
x = int(input())

# 근로소득금액 계산
def earned_income_calculator(x) :
    # x = 연봉, y = 근로소득공제액
    if x <= 500 :
        y = x * 70/100
    elif 500 < x <= 1500:
        y = 350 + (x - 500) *  40/100
    elif 1500 < x <= 4500:
        y = 750 + (x - 1500) *  15/100
    elif 4500 < x <= 10000:
        y = 1200 + (x - 4500) *  5/100
    else:
        y = 1475 + (x - 10000) *  2/100
    return x-y
    

# 차감소득금액 계산
def Deductible_income_amount(x) :
    # x = 연봉
    # x - 기본공제 - 건강보험료 - 장기요양보험료 - 고용보험료 - 국민연금

    def Health_Insurance(x) :
        y = x * 3.33/100
        return y

    def Long_term_care_insurance(x):
        y = x * 3.33/100 * 6.67/100
        return y

    def Employment_insurance(x):
        y = x * 0.8/100
        return y

    # 국민연금 (y = 기준소득월액, z=월 급여로 수정)
    def national_pension(x):
        z = x/12  
        if z < 35:
            y = 35
        elif 553 < z:
            y = 553
        else:
            y = z
        return y * 4.5/100 * 12


    z = 150 + Health_Insurance(x) + Long_term_care_insurance(x) + Employment_insurance(x) + national_pension(x)
    return z


#투자 권장 금액 계산
def Recommended_investment_amount(x):
    #x는 연봉, y는 근로소득
    z = earned_income_calculator(x)
    if z/2 < 3000 :
        y = z/2
    else:
        y = 3000
    return y

#산출세액 계산, x = 과세표준
def calculated_tax_invested(x):

    # 과세 표준 계산 
    
    # a = 근로소득금액, b = 차감소득금액, c = 계산금액
    a = earned_income_calculator(x)
    b = Deductible_income_amount(x)
    c = a - b
    # y = 투자 진행 case, z = 투자 미진행 case
    y = c - Recommended_investment_amount(x)

    #투자 진행 시, 산출 세액
    if y <= 1200:
        tax_invested = y * 6/100
    elif 1200 < y <= 4600:
        tax_invested = y *  15/100 - 108
    elif 4600 < y <= 8800:
        tax_invested = y *  24/100 - 522
    elif 8800 < y <= 15000:
        tax_invested = y *  35/100 - 1490
    elif 15000 < y <= 30000:
        tax_invested = y *  38/100 - 1940
    elif 30000 < y <= 50000:
        tax_invested = y *  40/100 - 2540
    else:
        tax_invested = y * 42/100 - 3540
    
    return tax_invested


#산출세액 계산, x = 과세표준
def calculated_tax_not_invested(x):

    # 과세 표준 계산 
    
    # a = 근로소득금액, b = 차감소득금액, c = 계산금액
    a = earned_income_calculator(x)
    b = Deductible_income_amount(x)
    c = a - b
    # y = 투자 진행 case, z = 투자 미진행 case
    z = c
    
    #투자 미 진행 시, 산출 세액
    if z <= 1200:
        tax_not_invested = z * 6/100
    elif 1200 < z <= 4600:
        tax_not_invested = z *  15/100 - 108
    elif 4600 < y <= 8800:
        tax_not_invested = z *  24/100 - 522
    elif 8800 < y <= 15000:
        tax_not_invested = z *  35/100 - 1490
    elif 15000 < y <= 30000:
        tax_not_invested = z *  38/100 - 1940
    elif 30000 < y <= 50000:
        tax_not_invested = z *  40/100 - 2540
    else:
        tax_not_invested = z * 42/100 - 3540
    
    return tax_not_invested 


#투자를 했을 경우, 안했을 때 대비해서 환급금액
def refund_amount(x):
    y = calculated_tax_not_invested(x) - calculated_tax_invested(x)
    return y

#환급금액을 뺀 실 투자금액
def Actual_investment_amount(x):
    y = Recommended_investment_amount(x) - refund_amount(x)
    return y

# 환급 금액의 비율
def refund_amount_percent(x):
    y = refund_amount(x)/Recommended_investment_amount(x)
    return y


# 실 투자 금액의 비율
def Actual_investment_amount_percent(x):
    y = Actual_investment_amount(x)/Recommended_investment_amount(x)
    return y


print("근로소득금액은 " + str(earned_income_calculator(x)))
print("차감소득금액은 " + str(Deductible_income_amount(x)))
print("투자권장금액은 " + str(Recommended_investment_amount(x)))
print("투자 시 산출세액은 " + str(calculated_tax_invested(x)))
print("투자 안할 경우 산출세액은 " + str(calculated_tax_not_invested(x)))

print("투자금액은 " + str(Recommended_investment_amount(x)))
print("환급금액은 " + str(refund_amount(x)))
print("실 투자금액은 " + str(Actual_investment_amount(x)))
print("환급비율은 " + str(refund_amount_percent(x)*100) + "%")
print("실 투자비율은 " + str(Actual_investment_amount_percent(x)*100) + "%")
