import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler


def decimalNormalize(x):
  return (x / 10^np.log10(max(x)))

def decimalDenormalize (x,maxvec):
  return (x*(10^log10(maxvec)))

def minMaxNormalize(x):
    scaler = MinMaxScaler(feature_range=(-1, 1))
    scaler.fit(x)
    return scaler.transform(x), scaler

def minMaxNormalizeOver(x, scaler):
    X = scaler.transform(x)
    #X[X>1.0] = 1.0 # limit top
    #X[X<-1.0] = -1.0 #limit bottom
    return X


def minMaxDenormalize(x, scaler):
    return scaler.inverse_transform(x)


def zNormalize(x):
    scaler = StandardScaler()
    scaler.fit(x)
    return scaler.transform(x), scaler

def zNormalizeOver(x, scaler):
    return scaler.transform(x)

def zDenormalize(x, scaler):
    return scaler.inverse_transform(x)