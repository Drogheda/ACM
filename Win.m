wn0 = rectwin(51);%N=51得矩形窗
wn1 = bartlett(51);%N=51得三角窗
wn2 = hanning(51);%N=51得汉宁窗
wn3 = hamming(51);%N=51得汉明窗
wn4 = blackman(51);
winShow(wn0, wn1, wn2, wn3, wn4);