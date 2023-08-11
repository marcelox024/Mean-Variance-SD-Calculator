import numpy as np


def calculate(list):
  if len(list)  == 9:
    calculations = {}

    m = np.array(list)
    m = m.reshape((3,3))

    mMean = []
    mMean.append(m.mean(axis=0).tolist())
    mMean.append(m.mean(axis=1).tolist())
    mMean.append(m.mean())
    calculations["mean"] = mMean

    mVariance = []
    mVariance.append(m.var(axis=0).tolist())
    mVariance.append(m.var(axis=1).tolist())
    mVariance.append(m.var())
    calculations["variance"] = mVariance

    mSD = []
    mSD.append(m.std(axis=0).tolist())
    mSD.append(m.std(axis=1).tolist())
    mSD.append(m.std())
    calculations["standard deviation"] = mSD

    mMax = []
    mMax.append(m.max(axis=0).tolist())
    mMax.append(m.max(axis=1).tolist())
    mMax.append(m.max())
    calculations["max"] = mMax

    mMin = []
    mMin.append(m.min(axis=0).tolist())
    mMin.append(m.min(axis=1).tolist())
    mMin.append(m.min())
    calculations["min"] = mMin

    mSum = []
    mSum.append(m.sum(axis=0).tolist())
    mSum.append(m.sum(axis=1).tolist())
    mSum.append(m.sum())
    calculations["sum"] = mSum
    
  else:
    raise ValueError("List must contain nine numbers.")
  
  return calculations
