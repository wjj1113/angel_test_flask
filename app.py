from flask import Flask, render_template, request, url_for
from crypt import methods
from flask import current_app as current_app
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
import cgitb cgitb.enable()

start_response('200 OK', [('Content-Type', 'text/html')])

scope = ['https://spreadsheets.google.com/feeds']
json_file_name = 'indigo-earth-367506-04dfd83cd1b4.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1saPfHtTWMsl2shUmh5EJGWtlE3ewFZovWOMFBckGcg4/edit#gid=0'

doc = gc.open_by_url(spreadsheet_url)
worksheet = doc.worksheet('tax_list')

app = Flask(__name__)

## GET 방식으로 값을 전달받음. 
## num이라는 이름을 가진 integer variable를 넘겨받는다고 생각하면 됨. 
## 아무 값도 넘겨받지 않는 경우도 있으므로 비어 있는 url도 함께 mapping해주는 것이 필요함

@app.route('/')
def main_get(num=None):
    return render_template('index.html', num=num)

@app.route('/calculate', methods=['POST', 'GET'])
def calculate(num=None):
    ## 어떤 http method를 이용해서 전달받았는지를 아는 것이 필요함c
    ## 아래에서 보는 바와 같이 어떤 방식으로 넘어왔느냐에 따라서 읽어들이는 방식이 달라짐
    if request.method == 'POST':
        #temp = request.form['num']
        pass
    elif request.method == 'GET':
        ## 넘겨받은 숫자 
        temp = request.args.get('num')
        temp = int(temp)
        x = temp
        ## 넘겨받은 문자
        ## 넘겨받은 값을 원래 페이지로 리다이렉트
        worksheet.append_row([temp,Recommended_investment_amount(x),refund_amount(x),Actual_investment_amount(x),refund_amount_percent(x)*100,Actual_investment_amount_percent(x)*100, (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))])
        return render_template('index.html', num=temp, char1=Recommended_investment_amount(x), char2=refund_amount(x), char3=Actual_investment_amount(x), char4=refund_amount_percent(x)*100, char5=Actual_investment_amount_percent(x)*100)
    ## else 로 하지 않은 것은 POST, GET 이외에 다른 method로 넘어왔을 때를 구분하기 위함

@app.route('/email2', methods=['POST', 'GET'])
def email2(email2=None):
    ## 어떤 http method를 이용해서 전달받았는지를 아는 것이 필요함c
    ## 아래에서 보는 바와 같이 어떤 방식으로 넘어왔느냐에 따라서 읽어들이는 방식이 달라짐
    if request.method == 'POST':
        #temp = request.form['num']
        pass
    elif request.method == 'GET':
        ## 넘겨받은 숫자 
        temp = request.args.get('email2')
        ## 넘겨받은 문자
        ## 넘겨받은 값을 원래 페이지로 리다이렉트
        worksheet = doc.worksheet('email_list')
        worksheet.append_row([temp,(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))])
        return render_template('index.html', email2=email2)



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
    return round(x-y)
    

# 차감소득금액 계산
def Deductible_income_amount(x) :
    # x = 연봉
    # x - 기본공제 - 건강보험료 - 장기요양보험료 - 고용보험료 - 국민연금

    def Health_Insurance(x) :
        y = x * 3.33/100
        return round(y)

    def Long_term_care_insurance(x):
        y = x * 3.33/100 * 6.67/100
        return round(y)

    def Employment_insurance(x):
        y = x * 0.8/100
        return round(y)

    # 국민연금 (y = 기준소득월액, z=월 급여로 수정)
    def national_pension(x):
        z = x/12  
        if z < 35:
            y = 35
        elif 553 < z:
            y = 553
        else:
            y = z
        return round(y * 4.5/100 * 12)


    z = 150 + Health_Insurance(x) + Long_term_care_insurance(x) + Employment_insurance(x) + national_pension(x)
    return round(z)


#투자 권장 금액 계산
def Recommended_investment_amount(x):
    #x는 연봉, y는 근로소득
    z = earned_income_calculator(x)
    if z/2 < 3000 :
        y = z/2
    else:
        y = 3000
    return round(y)

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
    
    return round(tax_invested)


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
    elif 4600 < z <= 8800:
        tax_not_invested = z *  24/100 - 522
    elif 8800 < z <= 15000:
        tax_not_invested = z *  35/100 - 1490
    elif 15000 < z <= 30000:
        tax_not_invested = z *  38/100 - 1940
    elif 30000 < z <= 50000:
        tax_not_invested = z *  40/100 - 2540
    else:
        tax_not_invested = z * 42/100 - 3540
    
    return round(tax_not_invested)


#투자를 했을 경우, 안했을 때 대비해서 환급금액
def refund_amount(x):
    y = calculated_tax_not_invested(x) - calculated_tax_invested(x)
    return round(y)

#환급금액을 뺀 실 투자금액
def Actual_investment_amount(x):
    y = Recommended_investment_amount(x) - refund_amount(x)
    return round(y)

# 환급 금액의 비율
def refund_amount_percent(x):
    y = refund_amount(x)/Recommended_investment_amount(x)
    return round(y)


# 실 투자 금액의 비율
def Actual_investment_amount_percent(x):
    y = Actual_investment_amount(x)/Recommended_investment_amount(x)
    return round(y)



if __name__ == '__main__':
    # threaded=True 로 넘기면 multiple plot이 가능해짐
  app.run(debug=True)


  