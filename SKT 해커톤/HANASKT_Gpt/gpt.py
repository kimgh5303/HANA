from flask import Flask, request, jsonify
import openai as ai
import numpy as np
import time as t
import os
from tqdm import tqdm
import json

app = Flask(__name__)

# 대화 상태 관리를 위한 변수
conversation = []
cAns = None  # 자식의 대답을 저장하기 위한 변수
pAns = None  # 부모의 대답을 저장하기 위한 변수

class GPT:
    def __init__(self):
        self.QnA = {}
        self.response : str = ""

        with open('./secure/api.txt','r',encoding='utf-8') as f:
            data = f.read().split('\n')
        ai.organization = data[0]
        ai.api_key = data[1]
        self.__getQnA()

    # 교과내용에 대해 물어볼 질문
    def __getQnA(self):
        with open('QnA.txt','r',encoding='utf-8') as f:
            self.QnA["query"] = f.read()

    # gpt에게 질문을 던지는 기능 수행
    def __GPT(self, content):
        try:
            self.response = ai.ChatCompletion.create(
                        model='gpt-3.5-turbo',
                        messages=conversation
                    )
        except Exception as e:
            print(f"GPT Error : {e}")
            return "", True
        return self.response.choices[0].message.content, False

    # 질문 디테일
    def query(self, requests):
        s = t.time()
        query = self.QnA["query"]
        
        content = f'질문을 던졌고 다음과 같이 자식의 답, 부모의 답이 왔어.\n\
                    질문 : {query},\n\
                    자식의 답 : {cAns},\n\
                    부모의 답 : {pAns},\n\
                    다문화 가정인데 둘의 관계가 소원한 상태야. 해당 질문과 자식의 답, 부모의 답들은 이러한 소원한 상태의 원인이라고 볼 수 있어.\n\
                    다음과 같이 엄마가 자식에게 쓰는 미안한 편지를 작성해:\n\
                    사랑하는 자식,\n\
                    엄마가 일하느라 여가 시간을 보내지 못하는 것이 너무 미안해. 너와 더 많은 시간을 보내고 싶어. 미안하다는 마음으로 쓴 이 편지가 내 마음을 전해줄 수 있기를 바랍니다."\n\
                    '
        while True:
            response, error = self.__GPT(content)
            if not error:
                break
            else:
                t.sleep(0.1)

        print(f'run gpt time : {t.time()- s}s')
        print("response")
        return {"messsage": "create report Sucessed", "code": True}

# 자식의 대답을 받아옴
@app.route('/answers/c', methods=['POST'])
def get_child_answers():
    global cAns
    cAns = request.json.get('child_answer')
    if cAns:
        # 자식의 대화를 대화 상태에 추가
        conversation.append({"role": "user", "content": cAns})
        # 부모의 대답이 있으면 GPT에게 요청
        if pAns:
            gpt = GPT()
            response = gpt.query(cAns)
            return jsonify(response)
        else:
            return jsonify({"message": "Waiting for parent's answers"})
    else:
        return jsonify({"message": "Waiting for child's answers"})

# 부모의 대답을 받아옴
@app.route('/answers/p', methods=['POST'])
def get_parent_answers():
    global pAns
    pAns = request.json.get('parent_answer')
    if pAns:
        # 부모의 대화를 대화 상태에 추가
        conversation.append({"role": "user", "content": pAns})
        # 자식의 대답이 있으면 GPT에게 요청
        if cAns:
            gpt = GPT()
            response = gpt.query(pAns)
            return jsonify(response)
        else:
            return jsonify({"message": "Waiting for child's answers"})
    else:
        return jsonify({"message": "Waiting for parent's answers"})

if __name__ == '__main__':
    gpt = GPT()
