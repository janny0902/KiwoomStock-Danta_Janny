import sys
from PyQt5.QtWidgets import *
import KiwoomAPI

class KiwoonMain:
    def __init__(self):
        self.kiwoom = KiwoomAPI.KiwoomAPI()
        self.kiwoom.CommConnect()

# ========== #
    def GetLoginInfo(self):
        # 로그인 상태
        self.kiwoom.GetConnectState()

        # 로그인 정보
        self.kiwoom.GetLoginInfo("ACCOUNT_CNT")
        self.kiwoom.GetLoginInfo("ACCLIST")
        self.kiwoom.GetLoginInfo("USER_ID")
        self.kiwoom.GetLoginInfo("USER_NAME")
        self.kiwoom.GetLoginInfo("KEY_BSECGB")
        self.kiwoom.GetLoginInfo("FIREW_SECGB")
        self.kiwoom.GetLoginInfo("GetServerGubun")

    def run(self):

        #### 주식 단타 프로그램 가이드 ####
        #### TODO 읽고 할 수 있는부분 또는 하고싶은 부분 만들면됨  TODO 뒤에 본인 이름적고 커밋 하셈 안건들겠음  .
        #### 완성 못해도 상관없으니 그냥 해보셈
        #### DB에 저장 하고싶은 데이터 있으면 카톡 주셈 DB만들어서 드림 현재는 DB없이개발 해보셈
        #### 기능 구현 위치는 TODO 아래에 그냥 만들면됨 

        #### KiwoomMain.py - 실행 요소만 모아놓아야함
        #### KiwoomAPI.py - KOAStudioSA 에서 제공해주는 기능 메소드 구현시 여기에 작성
        #### math.py - (구현중) - 수학 연산 기능 여기에 작성(%계산식) (수익률 계산식) 등등 자주 쓰는 위주로. 
        

        #TODO 1.스케줄러 적용  구글에 python 스케줄러 라고 검색하면  사용 방법 나옴  10초에 한번식 print('성공') 찍는 기능 만들기
                    #매일 오후 3시 15분에 print('매도') 찍기 기능

        #TODO 1-2.종목 서칭 (거래 순위 상위 10등 종목 나열, 실시간 검색 순위 없음 > 10위권 진입 종목 캐치)

        #TODO 1-3 종목 서칭2 (거래상위 10위 중 거래 할 대상 선정 1~2종목 그래프 보면서 좋은자리 찾아야함.)
                    #5분봉기준 전봉 대비 거래대금 *2 터진종목 우선

        #TODO 1-3-1 키움종목 매수 기능 -조건 설정
                    #5분봉 기준 20일선 골드 크로스 매수

        #TODO 2-1.키움 종목 매수 (한개 종목 코드를 입력하면 해당 종목 매수 기능 완료)
        

        #TODO 2-2 키움 종목 매도 (한개 종목 코드를 입력하면 해당 종목 매도 기능 완료)

        #TODO 2-2-1 키움 종목 매도 기능 - 조건 설정  
                    # 호가 -1% 이상 넘으면 매도, (손절)
                    # 5분봉기준 전봉 거래량 기준 60% 이상 하락시 매도, (익절)
                    # 5분봉기준 5일선 데드크로스시 매도

        #TODO 3. 잔고조회 (현재 잔고 조회해서 보유종목및 수익률 확인 )

        #TODO 4. 



        result = api_con.GetLoginInfo()
        print(result)


app = QApplication(sys.argv)
api_con = KiwoonMain()

api_con.run()

