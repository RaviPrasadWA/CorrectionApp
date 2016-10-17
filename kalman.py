

class Kalman:

    def __init__(self):
        self.Q_angle = 0.01
        self.Q_bias = 0.001
        self.R_measure = 0.03

        self.angle = 0
        self.bias = 0

        self.P = [ [0,0], [0,0] ]

    def getAngle(self, newAngle, newRate, dt):
        rate = newRate - self.bias
        self.angle += dt*rate

        self.P[0][0] += dt * (dt*self.P[1][1] - self.P[0][1] - self.P[1][0] + self.Q_angle)
        self.P[0][1] -= dt * self.P[1][1];
        self.P[1][0] -= dt * self.P[1][1];
        self.P[1][1] += self.Q_bias * dt;

        # Compute Kalman Gain

        S = self.P[0][0] + self.R_measure;
        K = [ self.P[0][0] / S,
              self.P[1][0] / S
            ]

        y = newAngle - self.angle
        self.angle += K[0] * y
        self.bias += K[1] * y

        self.P[0][0] -= K[0] * self.P[0][0]
        self.P[0][1] -= K[0] * self.P[0][1]
        self.P[1][0] -= K[1] * self.P[0][0]
        self.P[1][1] -= K[1] * self.P[0][1]

        return self.angle

    def setAngle(self, newAngle):
        self.angle = newAngle
        


