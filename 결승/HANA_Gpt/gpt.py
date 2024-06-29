from flask import Flask, request, jsonify
import openai as ai
import time as t

app = Flask(__name__)

# 대화 상태 관리를 위한 변수
Ans = None  # 답을 저장하기 위한 변수

class GPT:
    def __init__(self):
        self.QnA = {}
        self.response : str = ""

        with open('./secure/api.txt','r',encoding='utf-8') as f:
            data = f.read().split('\n')
        ai.organization = data[0]
        ai.api_key = data[1]
        self.__getQnA()

    # # 교과내용에 대해 물어볼 질문
    # def __getQnA(self):
    #     with open('QnA.txt','r',encoding='utf-8') as f:
    #         self.QnA["query"] = f.read()

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

# 대답을 받아옴
@app.route('/answers/laws', methods=['POST'])
def get_parent_answers():
    global Ans  # Ans 변수를 전역 변수로 사용

    user_question = request.json.get('question')                    # 이걸 나중에 바꾸기
    if user_question:
        # GPT 요청
        gpt = GPT()
        
        # query 메서드를 호출하여 GPT에게 질문을 하고 응답을 받음
        result = gpt.query(user_question)

        # GPT의 응답을 Ans 변수에 저장
        Ans = gpt.Ans

        return jsonify(result)
    else:
        return jsonify({"message": "질문을 기다리는 중입니다"})

if __name__ == '__main__':
    gpt = GPT()
    app.run(debug=True)
