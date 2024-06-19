# Download and install poppler

download poppler-package Release 24.0.02.0-0 from 
url: https://github.com/oschwartz10612/poppler-windows/releases/

.zip file을 열어 poppler folder를 Program Files 에 설치후

System 환경변수의 Path 에 C:\Program Files\poppler-24.02.0\Library\bin 을 추가하고 Window Ssytem 을 Resatrt 

시스템 환경변수 설정 찾아가기

Window> 설정 > 시스템 > 정보 > 관련링크 고급 시스템 설정 > 시스템속성 환경변수 >
사용자 변수 및 시스템 변수 편집 에서 Path 추가 하면 됨

# Python Environment

Select Python Environment 에서 3.11.x (base) 환경 선택

Power Shell terminal 에서
(base) conda activate
(base) conda install -c conda-forge poppler
