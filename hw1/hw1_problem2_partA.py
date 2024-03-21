import matplotlib.pyplot as plt

H = 2
h = 1
T_0 = [-6,-5,-4.00001, -4, -3, -2.00001,-2,-1,0.00001,0,1,1.9999,2,3,3.9999,4,5,5.9999,6,7]
x_t = [h,h,H,h,h,H,h,h,H,h,h,H,h,h,H,h,h,H,h,h]

plt.plot(T_0, x_t)
plt.title('HW#1 Problem #2')
plt.xlabel('Time t')
plt.ylabel('x(t)')
plt.show()