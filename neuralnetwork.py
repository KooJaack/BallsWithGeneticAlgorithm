import numpy as np
from settings import *
import copy


class LearningBot:

    def __init__(self, x, y):
        self.l_out = []
        self.food = [0, 0]
        self.w = [np.array([1,1,1,1,1,1,1,1,1]), np.array([1,1,1,1,1,1,1,1])]
        #self.w = [np.array([ 1.18908255e+01, -4.93644596e-04,  7.08184025e+00, -1.15698482e+01,
       #-7.54297826e-03,  6.91088913e+00,  1.65197745e+01,  1.39812351e-02,
       #-1.55450533e-02]), np.array([ 6.36604940e+00,  6.34521680e+00,  1.37731248e-02, -9.61358053e+00,
       #-2.74253753e-01,  2.66726556e-01, -2.80721495e+00,  3.32566233e-04])]

        self.w.append(np.random.randn((N_INPUT * N_HIDDEN)+2))
        self.w.append(np.random.randn((N_HIDDEN * N_OUTPUT)+1))
        self.pc = np.random.random_sample()

        def cross(self, a):
            _temp = N_INPUT * N_HIDDEN + N_HIDDEN * N_OUTPUT - 1
            _x1 = np.random.randint(0, _temp)
            if _x1 < N_INPUT * N_HIDDEN - 1:
                for i in range(_x1 + 1, N_INPUT * N_HIDDEN):
                    _tempw = copy.copy(a.w[0][i])
                    a.w[0][i] = copy.copy(self.w[0][i])
                    self.w[0][i] = copy.copy(_tempw)
                _tempw = copy.copy(a.w[1])
                a.w[1] = copy.copy(self.w[1])
                self.w[1] = copy.copy(_tempw)
            elif _x1 == N_INPUT * N_HIDDEN - 1:
                _tempw = copy.copy(a.w[1])
                a.w[1] = copy.copy(self.w[1])
                self.w[1] = copy.copy(_tempw)
            else:
                for i in range(_x1 % N_INPUT * N_HIDDEN, N_HIDDEN * N_OUTPUT - 1):
                    _tempw = copy.copy(a.w[1][i])
                    a.w[1][i] = copy.copy(self.w[1][i])
                    self.w[1][i] = copy.copy(_tempw)
                _tempw = copy.copy(a.w[0])
                a.w[0] = copy.copy(self.w[0])
                self.w[0] = copy.copy(_tempw)

        def mutation(self):
            for i in range(len(self.w)):
                for j in range(len(self.w[i])):
                    if np.random.random_sample() < MUTATION_CHANCE:
                        self.w[i][j] = np.random.randn()

    def calculate_layers(self):
        new_hidden_out = []
        self.l_out = []

        _feed = self.food[0]*self.w[0][0] + self.food[1] * self.w[0][1]+1*self.w[0][2]
        _out = (1 - np.exp(-_feed)) / (1 + np.exp(-_feed))
        new_hidden_out.append(_out)

        _feed2 = self.food[0]*self.w[0][3] + self.food[1] * self.w[0][4]+1*self.w[0][5]
        _out2 = (1 - np.exp(-_feed2)) / (1 + np.exp(-_feed2))
        new_hidden_out.append(_out2)

        _feed3 = self.food[0]*self.w[0][6] + self.food[1] * self.w[0][7]+1*self.w[0][8]
        _out3 = (1 - np.exp(-_feed3)) / (1 + np.exp(-_feed3))
        new_hidden_out.append(_out3)

        _feed_out = new_hidden_out[0]*self.w[1][0]+new_hidden_out[1]*self.w[1][1]+new_hidden_out[2]*self.w[1][2]+1*self.w[1][3]
        self.l_out.append((1 - np.exp(-_feed_out)) / (1 + np.exp(-_feed_out)))

        _feed_out2 = new_hidden_out[0]*self.w[1][4]+new_hidden_out[1]*self.w[1][5]+new_hidden_out[2]*self.w[1][6]+1*self.w[1][7]
        self.l_out.append((1 - np.exp(-_feed_out2)) / (1 + np.exp(-_feed_out2)))

        return self.l_out

    def feed_network(self, distance_in, angle_in):
        self.food = [distance_in, angle_in]
