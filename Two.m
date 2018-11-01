audio = audioread('Counting-16-44p1-mono-15secs.wav');
twoStart = 110e3;
twoStop = 135e3;
audioIn = audioIn(twoStart:twoStop);
timeVector = linspace((twoStart/fs),(twoStop/fs),numel(audioIn));
figure;
plot(timeVector,audioIn);
axis([(twoStart/fs) (twoStop/fs) -1 1]);
ylabel('Amplitude');
xlabel('Time (s)');
title('Utterance - Two')
sound(audioIn,fs);