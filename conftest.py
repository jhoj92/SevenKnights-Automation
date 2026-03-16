import pytest
from airtest.core.api import *
import logging

# 로그 레벨 설정
logging.getLogger("airtest").setLevel(logging.WARNING)

@pytest.fixture(scope="session", autouse=True)
def setup_automation():
    print("\n[Setup] 기기 연결 및 앱 실행 중...")

    try:
        auto_setup(__file__, devices=["Android:///emulator-5554"])
        
        ST.THRESHOLD = 0.8
        ST.FIND_TIMEOUT = 120
        
        package_name = "com.netmarble.tskgb"
        stop_app(package_name) 
        sleep(1.0)
        start_app(package_name)
        
        print(f"[Setup] {package_name} 실행 완료")
        
    except Exception as e:
        print(f"\n[Error] 초기화 실패: {e}")
        raise e

    yield  
    
    print("\n[Teardown] 테스트 세션 종료")