import matplotlib.pyplot as plt
 
H = 2
h = 1
t = [-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12]
h_2 = -2 * h * ((t+1) / 3)  
H_2 = -2 * H * ((t+1) / 3) 

T_0 = [-6,-5,-4.00001, -4, -3, -2.00001,-2,-1,0.00001,0,1,1.9999,2,3,3.9999,4,5,5.9999,6,7]
x_t = [h_2,h_2,H_2,h_2,h_2,H_2,h_2,h_2,H_2,h_2,h_2,H_2,h_2,h_2,H_2,h_2,h_2,H_2,h_2,h_2]


plt.plot(t, x_t)
plt.title('HW#1 Problem #2')
plt.xlabel('Time t')
plt.ylabel('x(t)')
plt.show()