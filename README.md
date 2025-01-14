# 효과적인 에이전트 구축 가이드

Erik Schluntz와 Barry Zhang의 [Building Effective Agents](https://anthropic.com/research/building-effective-agents) 연구의 참조 구현입니다.<br><br>
또한 Anthropic Cookbook의 내용을 Amazon Bedrock 기반 코드로 수정하였습니다. (by Jesam Kim)<br>
Amazon SageMaker AI - JupyterLab 에서 테스트 되었습니다. (Region : us-west-2)

이 저장소는 블로그에서 논의된 일반적인 에이전트 워크플로우의 최소 구현 예제를 포함하고 있습니다:

- 기본 구성 요소
  - 프롬프트 체이닝
  - 라우팅
  - 다중 LLM 병렬화
- 고급 워크플로우
  - 오케스트레이터-서브에이전트
  - 평가자-최적화기

## 시작하기
자세한 예제는 다음 Jupyter 노트북을 참조하세요:

- [Basic Workflows](basic_workflows.ipynb)
- [Evaluator-Optimizer Workflow](evaluator_optimizer.ipynb)
- [Orchestrator-Workers Workflow](orchestrator_workers.ipynb)

---
원본 Repo : https://github.com/anthropics/anthropic-cookbook/tree/main/patterns/agents
