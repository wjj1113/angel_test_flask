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

# 과세 표준 계산 
def tax_base(x):
    # a = 근로소득금액, b = 차감소득금액, c = 계산금액
    a = earned_income_calculator(x)
    b = Deductible_income_amount(x)
    c = a - b
    # y = 투자 진행 case, z = 투자 미진행 case
    y = c - Recommended_investment_amount(x)
    z = c
    return y, z

#산출세액 계산, x = 과세표준
def calculated_tax(x):
    if x <= 1200:
        y = x * 6/100
    elif 1200 < x <= 4600:
        y = x *  15/100 - 108
    elif 4600 < x <= 8800:
        y = x *  24/100 - 522
    elif 8800 < x <= 15000:
        y = x *  35/100 - 1490
    elif 15000 < x <= 30000:
        y = x *  38/100 - 1940
    elif 30000 < x <= 50000:
        y = x *  40/100 - 2540
    else:
        y = x * 42/100 - 3540
    return y
    


print("근로소득금액은 " + str(earned_income_calculator(300)))
print("차감소득금액은 " + str(Deductible_income_amount(300)))
print("투자권장금액은 " + str(Recommended_investment_amount(300)))
print("과세표준은 " + str(tax_base(300)))
print("산출세액은 " + str(calculated_tax(-90)))