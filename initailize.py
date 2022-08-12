from jajucha.planning import BasePlanning
from jajucha.graphics import Graphics
from jajucha.control import mtx
import cv2 #opencv 라이브러리를 불러옴
import numpy as np  #numpy 라이브러리를 np로 받음
import time


class Planning(BasePlanning):  #class를 정의함
    def __init__(self, graphics): #스페이스 4칸 or tab키-->indentation(들여쓰기)
        super().__init__(graphics)

    def initialize(self, frontImage):
        V, L, R = self.gridFront(frontImage, cols=7, rows=3)

        f = open("init.txt", "w")
        for i in range(6):
            f.write(str(V[i]) + "\n")
        for i in range(3):
            f.write(str(L[i]) + "\n")
        for i in range(3):
            f.write(str(R[i])+"\n")
        f.close()
        


if __name__ == "__main__":
    g = Graphics(Planning)  # 자주차 컨트롤러 실행
    g.root.mainloop()  # 클릭 이벤트 처리
    g.exit()  # 자주차 컨트롤러 종료
