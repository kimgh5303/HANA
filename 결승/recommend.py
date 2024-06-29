import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# 데이터셋 파일명
dataset_file = 'expense_dataset.csv'

# CSV 파일 로드
df = pd.read_csv(dataset_file)

# 사용자 수 설정
num_users = 10000

# 새로운 사용자 생성 (임의의 사용자 ID를 선택)
new_user_id = num_users + 1
new_user_data = {'User_ID': []}

# 새로운 사용자의 소비/지출 내역 생성 (이 예제에서는 임의로 생성)
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

# Financial 카테고리에 대한 새로운 사용자 데이터 생성
for category, amount_range in financial_categories.items():
    amount = np.random.uniform(amount_range[0], amount_range[1])
    new_user_data['User_ID'].append(new_user_id)
    new_user_data[category] = amount

# 새로운 사용자 데이터프레임 생성
new_user_df = pd.DataFrame(new_user_data)

# 기존 데이터프레임에 새로운 사용자 데이터 추가
df_with_new_user = pd.concat([df, new_user_df], ignore_index=True)

# 사용자-카테고리 행렬 생성
user_item_matrix = pd.pivot_table(df_with_new_user, index='User_ID', fill_value=0)

# 새로운 사용자와 다른 사용자들 간의 유사도 계산
new_user_similarity = cosine_similarity(user_item_matrix)[-1, :-1]

# 유사도가 높은 상위 K명의 사용자 선택
k_neighbors = 5
similar_users_indices = np.argsort(new_user_similarity)[-k_neighbors:]

# 상위 K명의 사용자들의 웨딩 카테고리 예산을 가져와서 추천
recommended_budgets = user_item_matrix.loc[similar_users_indices, '스튜디오':'신혼여행'].mean(axis=0)

# 결과 출력
print("새로운 사용자의 결혼 예산 추천:")
print(recommended_budgets)
