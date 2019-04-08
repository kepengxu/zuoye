# -*- coding: utf-8 -*-
import cv2
import numpy as np

def get_image(path):
    image=cv2.imread(path,cv2.IMREAD_GRAYSCALE)
    return image
def length(t):
    #  求对数
    tk=1
    while t>2:
        t=t/2
        tk=tk+1
    return tk
def encode(image):
    L=np.reshape([-1])


# function[S, s_min] = compress(p)
# n = length(p);
# s = zeros(1, n);
# l = zeros(1, n);
# b = zeros(1, n);
# % compression
# process
# b(1) = bmax(p, 1, 1);
# l(1) = 1;
# s(1) = 1 * b(1) + 11;
# for i=2:n
# b(i) = bmax(p, i, i);
# l(i) = 1;
# s(i) = s(i - 1) + 1 * b(i);
# for k=2:min(i, 256)
# if i - k == 0
#     temp_b = bmax(p, i - k + 1, i);
#     temp_l = k;
#     temp_s = k * temp_b;
# else
#     temp_b = bmax(p, i - k + 1, i);
#     temp_l = k;
#     temp_s = s(i - k) + k * temp_b;
# end
# if temp_b~=8
# % fprintf('%d\n', temp_b);
# end
#
# if temp_s < s(i)
#     % fprintf('%d,%d,%d，%d,%d\n', k, temp_s, s(i), temp_b, temp_l);
# b(i) = temp_b;
# l(i) = temp_l;
# s(i) = temp_s;
# end
# end
# s(i) = s(i) + 11;
# end
# s_min = s(n);
# % disp(s);
# % disp(l);
# % disp(b);
# % trace
# back
# process
# S = [n - l(n) + 1, n, l(n), b(n)];
# left = n - l(n);
# while left > 0
#     S = [left - l(left) + 1, left, l(left), b(left);
#     S];
#     left = left - l(left);
# end
# % function
# bmax
# function
# y = bmax(p, i, j)
# y = ceil(log2(double(max(p(i:j))+1)));