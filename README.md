# MyProject

간단한 스크린샷 캡처 및 텍스트 저장 기능을 제공하는 Python GUI 애플리케이션입니다.

## 주요 기능
- 스크린샷 영역 선택 및 저장 **(실행한 상태에서 'pagedown'키로 선택한 영역 스크린샷)**
- 텍스트 메모 작성 및 파일로 저장
- 다크 모드 지원
- 다양한 파일 형식 지원 (`.png`, `.jpg`, `.bmp`)

## 설치 방법

1. **Python 설치**  
   Python 3.8 이상이 필요합니다. [Python 다운로드](https://www.python.org/downloads/)

2. **필수 라이브러리 설치**  
   git clone 후, 아래 명령어로 라이브러리를 설치합니다.
   ```bash
   pip install -r requirements.txt
   python capture.py
   
------

# 사용방법
 1. 캡처 영역 선택
   - 프로그램에서 "캡처 영역 선택" 버튼을 눌러 영역을 드래그하여 선택합니다.
   - 'Pagedown'키를 누르면 스크린샷 저장
 2. 간단한 메모 작성
   - 텍스트 메모 작성 "텍스트 저장" 버튼을 눌러 저장합니다.
 3. 다크 모드 전환
   - "다크 모드 전환" 버튼으로 UI 테마를 변경합니다.
