import json
import matplotlib.pyplot as plt

# 1. JSON 파일 불러오기
with open("/content/evaluation_results.json", "r", encoding="utf-8") as file:
    evaluation_results = json.load(file)

# 2. 평가 기준 정의
criteria = ["Comprehensiveness", "Diversity", "Empowerment", "Overall Winner"]
win_counts = {criterion: {"Answer 1": 0, "Answer 2": 0} for criterion in criteria}

# 3. 데이터 집계
for result in evaluation_results:
    for criterion in criteria:
        winner = result[criterion]["Winner"]
        if winner in ["Answer 1", "Answer 2"]:
            win_counts[criterion][winner] += 1

# 4. 승률 계산
total_count = sum(win_counts["Comprehensiveness"].values())  # 전체 평가 개수
win_percentages = {criterion: {key: (value / total_count) * 100 if total_count > 0 else 0 for key, value in win_counts[criterion].items()} for criterion in criteria}

# 5. 그래프 생성
fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.4
index = range(len(criteria))

# Answer 1과 Answer 2의 승률
bars1 = [win_percentages[criterion]["Answer 1"] for criterion in criteria]
bars2 = [win_percentages[criterion]["Answer 2"] for criterion in criteria]

# 막대 그래프 생성
ax.bar(index, bars1, bar_width, label="Answer 1", color="blue")
ax.bar([i + bar_width for i in index], bars2, bar_width, label="Answer 2", color="orange")

# 그래프 설정
ax.set_xlabel("Evaluation Criteria")
ax.set_ylabel("Winning Percentage (%)")
ax.set_title("Answer 1 vs Answer 2 - Evaluation Results")
ax.set_xticks([i + bar_width / 2 for i in index])
ax.set_xticklabels(criteria)
ax.legend()

# 값 표시
for i, (bar1, bar2) in enumerate(zip(bars1, bars2)):
    ax.text(i, bar1 + 1, f"{bar1:.1f}%", ha="center", color="black")
    ax.text(i + bar_width, bar2 + 1, f"{bar2:.1f}%", ha="center", color="black")

# 그래프 출력
plt.show()
