from flask import Flask
import json
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

data ={
    "전창재": {
        "email": "cchun@sejong.ac.kr",
        "position": "조교수/인공지능학과",
        "major": "전기및전자공학",
        "education": {
            "bachelor": "한양대학교 전자통신컴퓨터공학",
            "master": "KAIST 전기및전자공학",
            "doctoral": "KAIST 전자및전자공학",
            "degree": "공학박사(KAIST)"
        },
        "lab": {
            "location": "대양AI센터 505",
            "phone": "02-3408-3237"
        }
    },
    "심태용": {
        "email": "tysim@sejong.ac.kr",
        "position": "조교수/인공지능학과",
        "major": "바이오메카트로닉스",
        "education": {
            "bachelor": "성균관대학교 바이오메카트로닉스",
            "master": "성균관대학교 바이오메카트로닉스",
            "doctoral": "성균관대학교 바이오메카트로닉스",
            "degree": "공학박사(성균관대학교)"
        },
        "lab": {
            "location": "대양AI센터 518",
            "phone": "02-3408-1866"
        }
    },
    "이수진": {
        "email": "genegraphy@sejong.ac.kr",
        "position": "조교수/인공지능학과",
        "major": "컴퓨터비전, HCI, 인공지능응용(예술, 엔터테인먼트)",
        "education": {
            "bachelor": "고려대학교 응용동물과학",
            "master": "서강대학교 미디어공학, 이화여자대학교 디자인학",
            "doctoral": "서강대학교 미디어공학",
            "degree": "공학박사(서강대학교)"
        },
        "lab": {
            "location": "대양AI센터 425",
            "phone": "02-3408-1867"
        }
    },
    "구영현": {
        "email": "yhgu@sejong.ac.kr",
        "position": "조교수/인공지능학과",
        "major": "소프트웨어공학",
        "education": {
            "bachelor": "세종대학교 소프트웨어공학(컴퓨터공학부)",
            "master": "세종대학교 소프트웨어공학",
            "doctoral": "세종대학교 컴퓨터공학",
            "degree": "공학박사(세종대학교)"
        },
        "lab": {
            "location": "대양AI센터 801",
            "phone": "02-3408-3253"
        }
    },
    "김정현": {
        "email": "j.kim@sejong.ac.k",
        "position": "조교수/인공지능학과",
        "major": "전기전자공학",
        "education": {
            "bachelor": "연세대학교 전기전자공학",
            "master": "연세대학교 전기전자공학",
            "doctoral": "연세대학교 전기전자공학",
            "degree": "공학박사(연세대학교)"
        },
        "lab": {
            "location": "대양AI센터 507호",
            "phone": "02-3408-3238"
        }
    },
    "신승협": {
        "email": "shshin@sejong.ac.kr",
        "position": "조교수/인공지능학과",
        "major": "기계항공공학/기계공학",
        "education": {
            "bachelor": "서울대학교 기계항공공학",
            "master": "서울대학교 기계항공공학",
            "doctoral": "서울대학교 기계공학",
            "degree": "공학박사(서울대학교)"
        },
        "lab": {
            "location": "대양AI센터 310A호",
            "phone": "02-3408-3252"
        }
    },
    "이동훈": {
        "email": "donghoun.lee@sejong.ac.kr",
        "position": "조교수/인공지능학과",
        "major": "교통공학",
        "education": {
            "bachelor": "칭화대학교(Tsinghua University) 토목공학과",
            "master": "카이스트 건설및환경공학과 (교통공학)",
            "doctoral": "카이스트 건설및환경공학과 (교통공학)",
            "degree": "공학박사(카이스트)"
        },
        "lab": {
            "location": "다산관 411",
            "phone": ""
        }
    },
    "Mohammed Al-masni": {
        "email": "m.almasani@sejong.ac.kr",
        "position": "조교수/인공지능학과",
        "major": "의공학",
        "education": {
            "bachelor": "Cairo 대학교 의공학및시스템",
            "master": "Cairo 대학교 의공학및시스템",
            "doctoral": "경희대학교 의공학",
            "degree": "공학박사(경희대학교)"
        },
        "lab": {
            "location": "대양AI센터 454",
            "phone": "02-6935-2643"
        }
    },
    "MUHAMMAD SYAFRUDIN": {
        "email": "udin@sju.ac.kr",
        "position": "조교수/인공지능학과",
        "major": "정보공학(소프트웨어공학)/산업시스템공학",
        "education": {
            "bachelor": "UIN Sunan Kalijaga 대학교 정보공학(소프트웨어공학)",
            "master": "동국대학교 산업시스템공학",
            "doctoral": "동국대학교 산업시스템공학",
            "degree": "공학박사(동국대학교)"
        },
        "lab": {
            "location": "대양AI센터 502",
            "phone": "02-3408-1879"
        }
    },
    "김장겸": {
        "email": "jk.kim@sejong.ac.kr",
        "position": "조교수/인공지능데이터사이언스학과",
        "education": {
            "bachelor": "서강대학교 전자공학",
            "master": "서강대학교 전자공학",
            "doctoral": "KAIST 전기및전자공학",
            "degree": "공학박사(KAIST)"
        },
        "lab": {
            "location": "센413A",
            "phone": "02-3408-3233"
        }
    }
}

@app.route('/faculty')
def faculty():
    
    return data

@app.route('/faculty/<name>')
def detail(name):
    faculty_data=''
    with open('./data/faculty.json','r',encoding='UTF8') as faculty:
        faculty_data = json.load(faculty)[name]
    return json.dumps(faculty_data,ensure_ascii=False)


if __name__=='__main__':
    app.run()