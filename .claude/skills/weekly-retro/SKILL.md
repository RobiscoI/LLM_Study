---
name: weekly-retro
description: 세션을 마무리한다. retro-writer 에이전트로 docs/weeks/week-NN.md 에 학습 요약·체크리스트·막힌 점·다음 행동 3개를 기록하고 커밋 명령을 안내한다. "/weekly-retro", "오늘 마무리", "회고", "정리해줘" 에 사용한다.
---

# 세션 마무리

1. 학습자에게 묻는다: "오늘 몇 시간 했나요? 완료 체크리스트 중 본인이 확실히 한 항목은?"
2. **retro-writer 서브에이전트**에게 대화 요약(한 일·배운 것·막힌 점)과 학습자의 체크 항목을 넘긴다. 에이전트가 `docs/weeks/week-NN.md`를 갱신한다.
3. 결과 파일을 학습자에게 보여주고 틀린 부분이 있는지 확인받는다.
4. 다음 행동 3개 중 1개는 **"다음 세션 첫 10분에 할 것"**으로 아주 작게 만든다 (예: "week-02/app.py 를 열어 add() 를 다시 실행한다").
5. 커밋 명령을 보여준다. **학습자가 직접 입력한다.**
   ```
   git add -A
   git commit -m "week-NN: <한 줄 요약>"
   git push
   ```
6. 장이 끝났으면(설명·재현 가능 확인 후) 태그도 안내한다: `git tag week-NN-done; git push --tags` (PowerShell은 `&&` 대신 `;`)
