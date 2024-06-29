import pandas as pd
import numpy as np

# 랜덤 시드 설정
np.random.seed(42)

# 데이터셋 파일명
dataset_file = 'expense_dataset.csv'

# 사용자 수 설정
num_users = 10000

# 재정 카테고리 및 예측에 필요한 특성 범위 설정
financial_categories = {
    '간편결제/충전': (0, 500000),
    '교통/자동차': (0, 5000000),
    '편의점/마트': (0, 1000000),
    '외식': (0, 1000000),
    '온라인쇼핑': (0, 5000000),
    '출금/이체': (0, 1000000),
    '배달': (0, 2000000),
    '건강/뷰티': (0, 3000000),
    '카페/디저트': (0, 1000000),
    '기타': (0, 5000000),
    '쇼핑': (0, 3000000),
    '의료': (0, 3000000),
    '생활비': (0, 5000000),
    '이자/대출': (0, 2000000),
    '여행/숙박': (0, 7000000),
    '저축/투자': (0, 10000000),
    '교육': (0, 8000000),
    '보험': (0, 1000000),
    '주거/세금': (0, 5000000),
    '반려동물': (0, 5000000),
    '술/유흥': (0, 5000000),
    '경조/기부': (0, 1000000),
    '취미/여가': (0, 5000000)
}

wedding_categories = {
    '스튜디오': (500000, 5000000),
    '드레스': (500000, 3000000),
    '메이크업': (100000, 500000),
    '한복대여': (200000, 1000000),
    '예복대여': (150000, 1000000),
    '예식장대관': (2000000, 15000000),
    '예식진행': (1000000, 3000000),
    '식비': (10000000, 20000000),
    '신혼여행': (3000000, 8000000),
}

# 데이터 생성
data = {'User_ID': []}

# 카테고리와 예산 범위를 데이터에 추가
for category, _ in financial_categories.items():
    data[category] = []

for category, _ in wedding_categories.items():
    data[category] = []

for user_id in range(1, num_users + 1):
    data['User_ID'].append(user_id)

    for category, amount_range in financial_categories.items():
        amount = np.random.uniform(amount_range[0], amount_range[1])
        data[category].append(amount)

    for category, amount_range in wedding_categories.items():
        amount = np.random.uniform(amount_range[0], amount_range[1])
        data[category].append(amount)

# 데이터프레임 생성
df = pd.DataFrame(data)

# CSV 파일로 저장 (인코딩을 'utf-8-sig'로 지정)
df.to_csv(dataset_file, index=False, encoding='utf-8-sig')

# 생성된 데이터 확인
print(df.head())

# 랜덤 시드 설정
np.random.seed(42)
