import os
from airtest.core.api import *
from airtest.core.cv import Template
from pages.base_page import BasePage

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(CURRENT_DIR)
IMG_DIR = os.path.join(ROOT_DIR, "S_image.air")

class FarmingPage(BasePage):

    def path(folder, name):
        return os.path.join(IMG_DIR, folder, name)
    
    # 반복전투 관련 이미지 및 좌표
    start_btn = Template(path("반복전투", "TAP TO START.png"))
    farming_complete_btn = Template(path("반복전투", "파밍 완료.png"))
    ruby_farming_btn = Template(path("반복전투", "루비 파밍.png"))
    farming_setting_00_btn = Template(path("반복전투", "00_모험 반복 전투 버튼.png"))
    farming_setting_01_btn = Template(path("반복전투", "01_반복 종료 조건 설정.png"))
    farming_setting_02_btn = Template(path("반복전투", "02_반복 전투 횟수 설정.png"))
    farming_setting_03_btn = Template(path("반복전투", "03_영웅 자동 교체 탭.png"))
    farming_setting_04_btn = Template(path("반복전투", "04_영웅 교체 설정.png"))
    farming_setting_05_btn = Template(path("반복전투", "05_영웅 교체 설정.png"))
    farming_setting_06_btn = Template(path("반복전투", "06_스킬 우선 순위 탭.png"))
    farming_setting_07_btn = Template(path("반복전투", "07_스킬 우선 순위 설정.png"))
    farming_setting_08_btn = (1568, 539) # 스킬 버튼 좌표
    farming_setting_09_btn = (1569, 623) # 스킬 버튼 좌표
    farming_setting_10_btn = Template(path("반복전투", "10_배속 모드 탭.png"))
    farming_setting_11_btn = Template(path("반복전투", "11_배속 모드 설정.png"))
    farming_setting_12_btn = Template(path("반복전투", "12_장비 자동 판매 탭.png"))
    farming_setting_13_btn = Template(path("반복전투", "13_무기 장비 버튼.png"))
    farming_setting_14_btn = Template(path("반복전투", "14_방어구 장비 버튼.png"))
    farming_setting_15_btn = Template(path("반복전투", "15_장신구 장비 버튼.png"))
    farming_setting_16_btn = Template(path("반복전투", "16_장비 자동 판매 설정.png"))
    ruby_farming_start_btn = Template(path("반복전투", "반복 전투 시작 버튼.png"))
    background_btn = Template(path("반복전투", "최소화 버튼.png"))


    def ruby_farming(self):
        self.step(self.start_btn)
        sleep(15.0)  # 로비 진입까지 대기
        keyevent("4")

        farming_steps = [
            self.ruby_farming_btn, 
            self.farming_setting_00_btn, self.farming_setting_01_btn, self.farming_setting_02_btn,
            self.farming_setting_03_btn, self.farming_setting_04_btn, self.farming_setting_05_btn,
            self.farming_setting_06_btn, self.farming_setting_07_btn, self.farming_setting_08_btn,
            self.farming_setting_09_btn, self.farming_setting_10_btn, self.farming_setting_11_btn,
            self.farming_setting_12_btn, self.farming_setting_16_btn, self.farming_setting_14_btn,
            self.farming_setting_16_btn, self.farming_setting_15_btn, self.farming_setting_16_btn,
            self.ruby_farming_start_btn, self.background_btn
        ]

        for f in farming_steps:
            self.step(f)