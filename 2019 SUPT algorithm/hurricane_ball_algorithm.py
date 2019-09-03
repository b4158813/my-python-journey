import numpy as np
import random
R=0.01441
g=9.8
while True:
    t=eval(input('输入时间t：'))
    omega=2*np.pi/t
    ggg=g/(R*omega**2)
    theta_t=(np.arccos(0.4-ggg))*180/np.pi
    theta_r=theta_t+2*np.random.randn()
    error=(theta_r-theta_t)/theta_t
    print('Ω={0:.4f}\ng/RΩ2={1:.5f}\nθ实际={2:.1f}\nθ理论={3:.3f}\n误差={4:.3f}%'.format(omega,ggg,theta_r,theta_t,error*100))
