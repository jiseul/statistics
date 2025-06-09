import json

investors = [
    {
        "name": "레이 달리오",
        "company": "Bridgewater Associates",
        "performance": "3.4%",
        "portfolio": "$23 Billion",
        "topStocks": ["P&G", "코카콜라", "존슨앤존슨"],
        "moreCount": 27,
        "img": ""
    },
    {
        "name": "워렌 버핏",
        "company": "Berkshire Hathaway",
        "performance": "5.2%",
        "portfolio": "$325 Billion",
        "topStocks": ["애플", "뱅크오브아메리카", "아메리칸 익스프레스"],
        "moreCount": 44,
        "img": ""
    },
    {
        "name": "조지 소로스",
        "company": "Soros Fund Management",
        "performance": "4.1%",
        "portfolio": "$6 Billion",
        "topStocks": ["리비안", "알파벳", "아마존"],
        "moreCount": 12,
        "img": ""
    },
    {
        "name": "케시 우드",
        "company": "ARK Investment Management",
        "performance": "6.3%",
        "portfolio": "$14 Billion",
        "topStocks": ["테슬라", "줌", "로쿠"],
        "moreCount": 35,
        "img": ""
    },
    {
        "name": "빌 애크먼",
        "company": "Pershing Square Capital",
        "performance": "2.8%",
        "portfolio": "$10 Billion",
        "topStocks": ["로우즈", "칩틀레", "힐튼"],
        "moreCount": 7,
        "img": ""
    },
    {
        "name": "피터 린치",
        "company": "Fidelity Magellan",
        "performance": "--",
        "portfolio": "$--",
        "topStocks": [],
        "moreCount": 0,
        "img": ""
    },
    {
        "name": "스탠리 드러켄밀러",
        "company": "Duquesne Family Office",
        "performance": "3.9%",
        "portfolio": "$2 Billion",
        "topStocks": ["마이크로소프트", "뉴욕타임즈", "델타"],
        "moreCount": 18,
        "img": ""
    },
    {
        "name": "짐 사이먼스",
        "company": "Renaissance Technologies",
        "performance": "5.6%",
        "portfolio": "$80 Billion",
        "topStocks": ["애플", "마이크로소프트", "아마존"],
        "moreCount": 300,
        "img": ""
    },
    {
        "name": "켄 그리핀",
        "company": "Citadel Advisors",
        "performance": "4.7%",
        "portfolio": "$62 Billion",
        "topStocks": ["애플", "마이크로소프트", "아마존"],
        "moreCount": 100,
        "img": ""
    },
    {
        "name": "칼 아이칸",
        "company": "Icahn Associates",
        "performance": "1.5%",
        "portfolio": "$20 Billion",
        "topStocks": ["CVR 에너지", "노보카르보", "허츠"],
        "moreCount": 15,
        "img": ""
    }
]

with open('sample_13f_portfolios.json', 'w', encoding='utf-8') as f:
    json.dump(investors, f, ensure_ascii=False, indent=2)
