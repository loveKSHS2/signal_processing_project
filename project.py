import numpy as np  # numpy를 np로씀
import pygame  # pygame 임포트
highFrequencies =  [783., 659., 698., 783.,659.,698.,783, 493.,440.,493.,523.,587.,659.,698.,
                   659.,523.,587.,659.,329.,349.,392.,440.,392.,349.,392.,523.,493.,523.,
                   440.,523.,493.,440.,392.,349.,
                   392.,349.,329.,349.,392.,440.,493.,523.,
                   440.,523.,493.,523.,493.,523.,
                   493.,523.,587.,523.,493.,523.,440.,493.,523.]  # 낮은 주파수
lowFrequencies = [659., 523., 587., 659.,523.,587.,659.,392.,349.,392.,440.,493.,523.,587.,
                   523.,440.,493.,523.,261.,293.,329.,349.,329.,293.,329.,440.,392.,440.,
                   349.,440.,392.,349.,329.,293.,
                   329.,293.,261.,293.,329.,349.,392.,440.,
                   349.,440.,392.,440.,392.,440.,
                   392.,440.,493.,440.,392.,440.,349.,392.,440.]
def generateDTMF(freq, duration=0.5, sample_rate=8000):  # 신호만들기
    Ts = 1. / sample_rate  # 샘플링 간격
    t = np.arange(0, duration, Ts)  # 0에서 duration까지 샘플링 주기 나누기
    # 32767                                 #간격으로 나눠서 배열t에 저장
    dtmf = 16383. * (np.sin(2 * np.pi * freq[0] * t) + np.sin(2 * np.pi * freq[1] * t))
    return dtmf.astype(np.int16)  # 더한 신호 리턴
def sounds(x, fs=8000.):  # 소리내기
    pygame.mixer.pre_init(int(fs), -16, 1)  # 오디오 장치 초기화
    pygame.mixer.init()
    xx = x.astype(np.int16)
    sound = pygame.sndarray.make_sound(xx)  # 듀얼톤 array를 Sound object로 바꿈
    length = sound.get_length()         #만든 sound의 길이를 length에 저장
    sound.play()  # sound object재생
    pygame.time.wait(int(length*1000))  # 1초동안 기다림
    pygame.mixer.quit()  # 오디오 장치 종료
xx = np.array([]).astype(np.int16)
for i in range(0, len(lowFrequencies)):
    x = generateDTMF([highFrequencies[i], lowFrequencies[i]])
    xx= np.append(xx,x)
sounds(xx, 8000)
