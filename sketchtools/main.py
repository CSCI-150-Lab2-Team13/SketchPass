import grid as gr
import rand_grid as rg
import display as disp
import numpy as np
from sklearn import svm

#from sklearn.naive_bayes import BernoulliNB

from sklearn.decomposition import PCA
from sklearn.ensemble import IsolationForest




# Further compute accuracy, precision and recall for the two predictions sets obtained
def main():
  SIZE = 6
  base = []
  base_flat = []
  y = []
  res = gr.create_grid(SIZE)
  if(res == 1):
    print("QUIT")
    return 1
  base.append(res)
  res = np.array(res)
  res = res.flatten()
  #y.append(1)
  base_flat.append(res)

if __name__ == "__main__":
    main()