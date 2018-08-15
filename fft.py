import numpy as np
from scipy.fftpack import fft,ifft
import matplotlib.pyplot as plt
import seaborn



#采样点选择1400个，因为设置的信号频率分量最高为600赫兹，根据采样定理知采样频率要大于信号频率2倍，所以这里设置采样频率为1400赫兹（即一秒内有1400个采样点，一样意思的）
N = 10000
T = 0.1
x=np.linspace(0, T, N)      

#设置需要采样的信号，频率分量有180，390和600
y=7*np.sin(2*np.pi*180*x) + 2.8*np.sin(2*np.pi*390*x)+5.1*np.sin(2*np.pi*600*x)
#y=7*np.sin(2.0 * np.pi * x)

yy=fft(y)                     #快速傅里叶变换
yreal = yy.real               # 获取实数部分
yimag = yy.imag               # 获取虚数部分

yf = 2.0 * abs(fft(y)) / N                 # 取绝对值


xf = np.linspace(0.0,  N / T, N)        # 频率



plt.subplot(121)
plt.plot(x,y)   
plt.title('Original wave')

plt.subplot(122)
plt.plot(xf,yf,'r')
plt.xlim((0,700))
plt.title('FFT of Mixed wave',fontsize=7,color='#7A378B')  




plt.show()
