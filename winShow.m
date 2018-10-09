function winShow(w1, w2, w3, w4, w5)
N = linspace(-pi, pi, 4096);%产生（-pi,pi）区间上等间距的4096个点.默认产生100个点。
i = 0;
for w = [w1, w2, w3, w4, w5]
    i = i + 1;
    [h1, w0] = freqz(w, 1, N);%数字滤波器频率响应函数。默认N为512
    %h1是离散系统频响在0-pi范围内N个频率等分点的值；
    %w0是0-pi范围内N个频率等分点
    %加上'whole'参数就是求系统频响
    subplot(5, 1, i);%将坐标系划分成5x1块，并在第i块作图
    plot(w0 / pi, 20 * log10(abs(h1 / max(h1))));%绘制对数幅度谱，将横坐标归一化
    axis([-1 1 -100 0]);%横坐标（-1,1），纵坐标（-100,0）
    xlabel('归一化频率/\pi');
    ylabel('20log10|W(e^{j\omega})|/dB');
    title('傅里叶变换');
    set(gca, 'YTick', [-100 -80 -60 -40 -20 0]);%给纵轴加标签
    set(gca, 'XTick', (-1 : 0.2 : 1));
    text(1, -124, '\pi');%在指定位置上显示字符串
end

