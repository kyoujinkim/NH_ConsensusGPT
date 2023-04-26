def loadTemplate():
    template = """아래에 주어진 근거를 사용해서 질문에 대한 자세한 정답의 목록을 생성해줘.
    정답의 형식은 아래 <예시>를 참고해. 정답은 <실제> 부분만을 보고 작성해줘.

    <예시>
    질문: 기술주 상승 배경과 향후 전망
    =========
    근거: 일반적으로 선진국의 은행위기가 발생했을 경우, 변동성과 위험자산 회피심리가 확대되며 신흥국에 더 큰 리스크 프리미엄을 요구
    출처: 전병하,엄서진. (2023, April 17). Changing. 20pg
    근거: 하지만 금리 인상의 정점 부근에서는 우리가 알 수 없는 이벤트 리스크라는 공포가 등장할 수 있다. IT버블, 서브프라임 모기지 등 여러 경기 충격이 금리 인상 시기의 말미에 등장했다.
    출처: 리서치센터. (2023, April 10). NH FICC. 4pg
    =========
    정답: - 선진국의 은행위기 발생시 변동성과 위험자산 회피심리가 확대되며 신흥국에 더 큰 리스크 프리미엄을 요구할 수 있음(*1)
    - 금리 인상의 정점 부근에서 파급효과(*2)

    <실제>
    질문: {question}
    =========
    근거: {summaries}
    =========
    정답:"""

    template_s = """ 아래에 주어진 근거를 질문과 관련이 없는 근거는 제외하고 올바른 순서대로 다시 정렬해줘
    정답의 형식은 아래 <예시>를 참고해. 정답은 <실제> 부분만을 보고 작성해줘.

    <예시>
    질문: 2차전지 소재
    =========
    근거: - 2차전지 소재 업체 중 가장 빠른 성장성 기대하는 CNT도전재(*1)
    - 나노신소재가 고체 도전재 기술 보유로 인한 주가 탄력(*3)
    - 유럽 CRMA의 2차전지 Upstream 정책으로 인한 2차전지 셀, 소재 주가 소폭 하락(*6)
    - CNT도전재의 원료인 CNT 파우더 생산 업체인 동사는 전자의 통로 역할을 하는 필수 소재인 도전재를 생산함(*7)
    - 2차전지 내 기술 경쟁력을 토대로 성장이 본격화되는 소재는 실리콘 음극재, CNT 도전재 등이 남아 있다(*8)
    - LG에너지솔루션, 삼성SDI가 Top Pick으로 추천됨(*11)
    =========
    정답: - 2차전지 내 기술 경쟁력을 토대로 성장이 본격화되는 소재는 실리콘 음극재, CNT 도전재 등이 남아 있다(*8)
    - 2차전지 소재 업체 중 가장 빠른 성장성 기대하는 CNT도전재. 나노신소재가 고체 도전재 기술 보유로 인한 주가 탄력(*1)(*3)
    - CNT도전재의 원료인 CNT 파우더 생산 업체인 동사는 전자의 통로 역할을 하는 필수 소재인 도전재를 생산함(*7)

    <실제>
    질문: {question}
    =========
    근거: {summaries}
    =========
    정답: """

    template_agg = """아래에 주어진 근거를 종합해서 질문에 대한 결론을 간단하고 명료한 어조로 작성해줘.
    정답의 형식은 아래 <예시>를 참고해. 정답은 <실제> 부분만을 보고 작성해줘.

    <예시>
    질문: 기술주 상승 배경과 향후 전망
    =========
    근거: - 인공지능에 대한 관심 증가로 최근 기술주 상승 주도.
    - 최근 기술주의 상승은 생성형 인공지능 시장으로 인해 생성된 기회에 기인하지만, 그와 동시에 강해질 경쟁 압력은 상승에 부정적.
    =========
    정답: 위 내용들을 종합하면, 기술주는 향후 상승할 가능성이 높습니다.

    <실제>
    질문: {question}
    =========
    근거: {summaries}
    =========
    정답: """

    return {'template':template,
            'template_s':template_s,
            'template_agg':template_agg}