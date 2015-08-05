import numpy as np
import matplotlib.pyplot as plt

A = np.array([
-0.232352941,
-1.112205882,
0.607941176,
0.928088235,
0.048235294,
-0.731617647,
0.688529412,
1.108676471,
-0.471176471,
-1.051029412,
0.669117647,
0.789264706,
-0.890588235,
-1.470441176,
0.449705882,
0.669852941])

sp = np.fft.fft(A,16,-1)
print (sp)

orig = np.fft.ifft(sp,16,-1)
print (orig.real)

plt.plot(A)
plt.plot(orig.real)
plt.show()