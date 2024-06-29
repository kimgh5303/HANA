import csv
import random

def generate_random_amount(min_amount, max_amount):
    amount = random.randint(min_amount, max_amount)
    return amount

def generate_random_dataset(num_users, categories, financial_categories):
    dataset = []

    for user_id in range(1, num_users + 1):
        record = {'user_id': user_id}

        # 소비 내역 생성
        for category, (min_amount, max_amount) in categories.items():
            amount = generate_random_amount(min_amount, max_amount)
            record[category] = amount

        # 재정 상황 카테고리 생성
        financial_data = {}
        for f_category, (f_min_amount, f_max_amount) in financial_categories.items():
            f_amount = generate_random_amount(f_min_amount, f_max_amount)
            financial_data[f_category] = f_amount

        record.update(financial_data)

        dataset.append(record)

    return dataset

# 사용자 수와 카테고리 설정
num_users = 10000
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

# 데이터셋 생성
dataset = generate_random_dataset(num_users, categories, financial_categories)

# 데이터셋을 CSV 파일로 저장
filename = 'expense_dataset.csv'
fieldnames = ['user_id'] + list(categories.keys()) + list(financial_categories.keys())

with open(filename, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(dataset)

print(f"데이터셋이 {filename} 파일로 저장되었습니다.")