from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *
import time

class KiwoomAPI(QAxWidget):
    def __init__ (self):
        super().__init__()
        self.output_list = []
        self.set_kiwoom_api()
        self.set_event_slot()

# ========== #
    def set_kiwoom_api(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")

    def set_event_slot(self):
        # 공통
        self.OnReceiveMsg.connect(self.E_OnReceiveMsg)

        # 로그인 버전처리
        self.OnEventConnect.connect(self.E_OnEventConnect)

# ========== #
    ### Event 함수 ###
    ## 공통 ##
    def E_OnReceiveMsg(self, sScrNo, sRQName, sTrCode, sMsg):
        print(sScrNo, sRQName, sTrCode, sMsg)

    ## 로그인 버전처리 ##
    def E_OnEventConnect(self, nErrCode):
        print(nErrCode)

        self.event_loop_CommConnect.exit()

# ========== #
    ### OpenAPI 함수 ###
    ## 로그인 버전처리 ##
    # 로그인
    def CommConnect(self):
        self.dynamicCall('CommConnect()')
        self.event_loop_CommConnect = QEventLoop()
        self.event_loop_CommConnect.exec_()

    # 로그인 상태
    def GetConnectState(self):
        ret = self.dynamicCall('GetConnectState()')

        print(ret)

    def GetLoginInfo(self, kind=''):
        ret = self.dynamicCall('GetLoginInfo(String)', kind)

        print(ret)
        
    def CommRqData(self, sRQName, sTrCode, nPrevNext, sScreenNo):
        ret = self.dynamicCall('CommRqData(String, String, int, String)', sRQName, sTrCode, nPrevNext, sScreenNo)
        self.event_loop_CommRqData = QEventLoop()
        self.event_loop_CommRqData.exec_()   

    def wait_secs(self,msg, secs=10):        
        while secs > 0:
            time.sleep(1)
            print(f"{msg} waiting: {secs}")
            secs = secs - 1