import csv
from sklearn.linear_model import LinearRegression

# 데이터셋 파일명
dataset_file = 'expense_dataset.csv'

# 사용자 수와 카테고리 설정
num_users = 1000
categories = {
    '식료품': (0, 5000),
    '의류': (0, 3000),
    '가전제품': (0, 10000),
    '스포츠용품': (0, 500),
    '교통': (0, 1000),
    '미용': (0, 500),
    '의료': (0, 3000),
    '여행': (0, 1000),
    '문화': (0, 500),
    '음식점': (0, 3000),
    '주류': (0, 3000),
    '통신': (0, 100),
    '가정용품': (0, 600),
    '도서': (0, 200),
    '유류비': (0, 3000),
    '반려동물': (0, 200),
    '유아용품': (0, 200),
    '교육': (0, 5000),
}

# 예측에 필요한 특성 범위 설정
financial_categories = {
    '현재 소득': (20000, 60000),
    '현재 지출': (10000, 70000),
    '저축': (0, 30000),
    '금융 자산': (0, 100000),
    '부채 금액': (0, 50000),
    '재무적 안정성': (0, 10),
    '대출 상환능력': (0, 100),
    '신용 점수': (300, 850),
    '투자 수익률': (-50, 50),
    '부동산 보유량': (0, 10),
}

# 소비 카테고리와 재정 상황 카테고리
expense_categories = list(categories.keys())
financial_categories = list(financial_categories.keys())

# 데이터셋 로드
dataset = []
with open(dataset_file, 'r', encoding='cp949', errors='ignore') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        dataset.append(row)

# 입력과 출력 데이터 준비
X = []
Y_expense = []

for data in dataset:
    x = []
    for f_category in financial_categories:
        x.append(float(data[f_category]))
    X.append(x)

    y_expense = []
    for category in expense_categories:
        y_expense.append(float(data[category]))
    Y_expense.append(y_expense)

# 선형 회귀 모델 훈련
model_expense = LinearRegression()
model_expense.fit(X, Y_expense)

# 재정 상황에 따른 소비 예측 함수
def predict_expense(financial_situation):
    x = []
    for f_category in financial_categories:
        x.append(float(financial_situation[f_category]))

    predicted_expense = model_expense.predict([x])[0]

    return predicted_expense

# 현재 재정 상황 입력
current_financial_situation = {
    '현재 소득': 30000,
    '현재 지출': 20000,
    '저축': 5000,
    '금융 자산': 50000,
    '부채 금액': 20000,
    '재무적 안정성': 8,
    '대출 상환능력': 70,
    '신용 점수': 700,
    '투자 수익률': 5,
    '부동산 보유량': 3,
}

# 줄어든 재정 상황 입력
reduced_financial_situation = {
    '현재 소득': 20000,
    '현재 지출': 20000,
    '저축': 5000,
    '금융 자산': 50000,
    '부채 금액': 20000,
    '재무적 안정성': 8,
    '대출 상환능력': 70,
    '신용 점수': 700,
    '투자 수익률': 5,
    '부동산 보유량': 3,
}

# 기존 소비 예측
current_expense_recommendations = predict_expense(current_financial_situation)

# 줄어든 재정 상황 소비 예측
reduced_expense_recommendations = predict_expense(reduced_financial_situation)

# 기존 소비와 줄어든 재정 상황의 소비 카테고리 변화 출력
print("소비 카테고리 변화:")
for i, category in enumerate(expense_categories):
    print(f"{category}: {current_expense_recommendations[i]} -> {reduced_expense_recommendations[i]}".encode('utf-8').decode('utf-8'))