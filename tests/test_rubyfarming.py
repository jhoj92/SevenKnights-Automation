import pytest
from pages.step_page import FarmingPage

class TestSevenKnights:
    def test_ruby_farming(self):
        """쫄작 자돟화 테스트"""

        tutorial = FarmingPage()
        tutorial.ruby_farming() 

        print("\n>>> 테스트 완료")