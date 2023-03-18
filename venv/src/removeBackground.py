import cv2
import numpy as np
from PIL import Image

# 누끼를 따기 위한 함수
def remove_background(img):
    # PIL Image 객체를 OpenCV Mat 객체로 변환
    cv_img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    # 배경과 인물을 분리하기 위한 기준 값 설정 (HSV 색상 공간 사용)
    lower = np.array([0, 0, 0]) # 검정색
    upper = np.array([100, 100, 100]) # 흰색

    # HSV 색상 공간으로 변환
    hsv = cv2.cvtColor(cv_img, cv2.COLOR_BGR2HSV)

    # 기준 값 범위 내의 영역을 찾아 마스크 생성
    mask = cv2.inRange(hsv, lower, upper)

    # 배경을 제외한 인물 이미지 추출
    result = cv2.bitwise_and(cv_img, cv_img, mask=mask)

    # OpenCV Mat 객체를 PIL Image 객체로 변환
    result = Image.fromarray(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))

    # 이미지 저장
    result.save("result.png")

    return result

# 입력받은 파일 이름
input_file = input("Enter the input file name: ")

# PIL로 이미지 열기
try:
    with Image.open(input_file) as img:
        # 누끼를 따기
        img = remove_background(img)

        # 새 파일 이름
        output_file = input_file.split('.')[0] + ".png"

        # PNG로 저장
        img.save(output_file, "PNG")

        print("PNG 파일이 성공적으로 생성되었습니다.")
except IOError:
    print("파일을 열 수 없습니다.")
