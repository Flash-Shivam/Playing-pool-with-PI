import sympy
import numpy as np
import math
import matplotlib.pyplot as plt

number_of_digits = input()
m1 = 1
m2 = math.pow(100,int(number_of_digits)-1)
v1 = 0
v2 = -1
p = m2*v2
e = 1/2 * m2 * (v2 ** 2)
count = 0
points_x = []
points_y = []
points_x.append(math.sqrt(m2)*v2)
points_y.append(math.sqrt(m1)*v1)
# fig, ax = plt.subplots()
radius = math.sqrt(m2*(v2**2))
# print(radius)
# ax.add_artist(circle)

while not(v1 >= 0 and v2 > 0 and v2 >= v1):
    # collision between blocks
    if count % 2 ==0:
        V2 = sympy.Symbol('V2')
        f1 = 1/2 * m2 * (V2 ** 2) + 1/2 * m1 * (((p-m2*V2)/m1) ** 2) - e
        matrix_ans = sympy.solvers.solve(f1)
        v2 = matrix_ans[1]
        v1 = (p-m2*v2)/m1
        count += 1
        points_x.append(math.sqrt(m2)*v2)
        points_y.append(math.sqrt(m1)*v1)
        # print(matrix_ans)
        # print(v1, v2)
    else:
    # collision with wall
        v1 = -v1
        p = m1*v1+m2*v2
        count += 1
        points_x.append(math.sqrt(m2)*v2)
        points_y.append(math.sqrt(m1)*v1)
        # print(v1, v2, count)

print(count)

t = np.linspace(0,2*np.pi,max(count**2,100))
plt.axis("equal")
plt.grid()
x = radius*np.cos(t)
y = radius*np.sin(t)

plt.plot(x,y,color='blue')
plt.plot(points_x,points_y,marker='*',color='red',markerfacecolor='yellow',markersize = 15)

plt.show()
