import json
import requests
import time
from tqdm import tqdm
import re
# GPT-4o-mini API 설정
API_URL = "https://api.openai.com/v1/chat/completions"  # OpenAI API URL
API_KEY = "sk-"
mode1 = "final_del"
mode2 = "final"
cls = "agriculture"
#  result.json 파일 읽기
with open(f"eval_{mode1}_{mode2}_{cls}_result.json", "r", encoding="utf-8") as file:
    prompts = [json.loads(line) for line in file.readlines()]
#  API 요청 및 응답 저장
evaluation_results = []
total_requests = len(prompts)
success_count = 0
fail_count = 0
max_retries = 5  # 최대 재시도 횟수
print(f"총 {total_requests}개의 요청을 처리합니다...")

category_pattern = r'"([^"]+)"\s*:\s*\{([^}]+)\}' 
key_value_pattern = r'"([^"]+)"\s*:\s*"([^"]+)"'  
for i, prompt in enumerate(tqdm(prompts, desc="Processing API Requests", unit="req")):
    request_data = {
        "model": "gpt-4o-mini",
        "messages": prompt["body"]["messages"],
        "temperature": 0.7
    }
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    retries = 0
    while retries < max_retries:
        response = requests.post(API_URL, headers=headers, json=request_data)
        if response.status_code == 200:
            try:
                response_json = response.json()
                response_text = response_json["choices"][0]["message"]["content"]
                # response_data = json.loads(response_text)
                parsed_data = {}

                # 대분류(카테고리) 추출
                for category_match in re.finditer(category_pattern, response_text):
                    category_name = category_match.group(1)
                    category_content = category_match.group(2)

                    # 각 카테고리 내부의 Winner와 Explanation을 추출
                    key_value_matches = re.findall(key_value_pattern, category_content)

                    parsed_data[category_name] = {key: value for key, value in key_value_matches}
                response_data = parsed_data
                response_data['swap'] = prompt['swap']
                # 응답이 예상한 형식인지 확인
                criteria = ["Comprehensiveness", "Diversity", "Empowerment", "Overall Winner"]
                if all(criterion in response_data for criterion in criteria):
                    evaluation_results.append(response_data)
                    success_count += 1
                    break
                else:
                    raise ValueError("응답 형식이 올바르지 않음")
            except (json.JSONDecodeError, KeyError, ValueError) as e:
                print(f"{i+1}번째 응답이 예상된 형식이 아님, 재요청 중... ({retries+1}/{max_retries})")
                retries += 1
                time.sleep(5)
        else:
            print(f"{i+1}번째 요청 실패, 재시도 {retries+1}/{max_retries} Error: {response.status_code}, {response.text}")
            retries += 1
            time.sleep(5)
    if retries == max_retries:
        print(f"{i+1}번째 요청 최종 실패. 스킵합니다.")
        fail_count += 1
print(f"\n완료: 총 {total_requests}개 요청 중 {success_count}개 성공, {fail_count}개 실패\n")
#  API 응답 저장
with open(f"{mode1}_{mode2}_{cls}_evaluation_results.json", "w", encoding="utf-8") as outfile:
    json.dump(evaluation_results, outfile, ensure_ascii=False, indent=4)