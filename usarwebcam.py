import cv2


def tirar_foto(nome_arquivo):
    #se vc tiver mais de uma webcam conectada, mude o inteiro dentro da funçao VIdeoCapture
    cam = cv2.VideoCapture(0)

    #read é uma função que captura um frame de sua webcam
    ret, frame = cam.read()
    if ret:
        #salvar o frame dentro do seu PC
        cv2.imwrite(nome_arquivo + ".jpg", frame)

    #desabilito a webcam ou libero a webcam
    cam.release()
