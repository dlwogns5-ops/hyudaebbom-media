# 진또배기 미아점(cellp_p) 주간 릴스

- `pipeline/template/` : 릴스 템플릿 (reels-visual.jsx — "놓치면 손해!" 배너 내장), 주제 데이터 `reels-visual-topics.js`
- `pipeline/make.sh "YYYY-MM-DD|이름|topicKey" ...` : 주제별 MP4(1080x1920, 약 21초) + cover.jpg 를 `media/YYYY-MM-DD/` 에 생성
- `media/YYYY-MM-DD/caption.txt` : 그날 인스타 캡션
- `topics.md` : 이미 다룬 주제 목록 (새 주제는 겹치지 않게)

## 주제 데이터 형식 (RV_TOPICS 에 추가)
장면 7개: hook → phone → phone 또는 stat → stat 또는 phone → compare → check → CTA
- phone 의 rows: [라벨, 값, 색(teal/amber/red)] 4줄. 라벨+값 합쳐 9글자 안팎 (넘으면 줄바꿈됨)
- 화면 상단 screen 문구는 10글자 안팎
- 금지: "무료", "0원", "공짜", 구체적 지원금·할인 금액
