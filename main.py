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
	SIZE = 18
	base = []
	base_flat = []
	y = []
	for i in range(10):
	#for i in range(2): #2 
		res = gr.create_grid(SIZE)
		if(res == 1):
			print("QUIT")
			return 1
		base.append(res)
		res = np.array(res)
		res = res.flatten()
		#y.append(1)
		base_flat.append(res)


	#disp.display_grid(grid = base[0])							#Display base grid
	#disp.display_grid(grid = rg.create_pos_grid(base[0]))		#Display modified grid
	#disp.display_grid(grid = base[1])							#Display base grid 2
	#disp.display_grid(grid = rg.create_pos_grid(base[1]))		#Display modified grid 2

	train_grids_pos = []
	#train_grids_neg = []
	
	for grid in base:
		for i in range(300):
			#y.append(1)
			temp = rg.create_pos_grid(grid)
			temp = np.array(temp)
			temp = temp.flatten()
			train_grids_pos.append(temp)
	#for i in range(200):
	#	y.append(0)
	#	if (i <= 50):
	#		temp = rg.create_rand_grid(0.15, SIZE)
	#	elif (i > 50 and i <= 100):
	#		temp = rg.create_rand_grid(0.35, SIZE)
	#	elif (i > 100 and i <= 150):
	#		temp = rg.create_rand_grid(0.55, SIZE)
	#	else:
	#		temp = rg.create_rand_grid(0.75, SIZE)
	#	temp = np.array(temp)
	#	temp = temp.flatten()
	#	train_grids_neg.append(temp)

	

	X = base_flat + train_grids_pos #+ train_grids_neg
	X = np.array(X)

	
	#X = X.reshape(-1, 1)

	#y = np.array(y)

	# Create Bernoulli Naive Bayes object with prior probabilities of each class
	#
	#	Gave many false positives, no point in using bc only 1 feature 
	#
	#	clf = BernoulliNB(class_prior=[0.9999, 0.0001])




	# USE PCA?
	#pca = PCA(n_components=250)#, whiten=True)
	#pca = pca.fit(X)
	#print('Explained variance percentage = %0.2f' % sum(pca.explained_variance_ratio_))
	#X_train = pca.transform(X)

	# Train classifier and obtain predictions for OC-SVM
	oc_svm_clf = svm.OneClassSVM(gamma=0.0002, kernel='rbf', nu=0.0001) 
	#if_clf = IsolationForest(contamination=0.08, max_features=1.0, max_samples=1.0, n_estimators=40)  # Obtained using grid search
	oc_svm_clf.fit(X)
	#oc_svm_clf.fit(X_train)
	#oc_svm_clf.fit(X_train)
	#if_clf.fit(X_train)

	
	#if_preds = if_clf.predict(X_test)

	#clf = svm.SVC()
	#model = clf.fit(X, y)

	test = np.array(gr.create_grid(SIZE))
	test = test.flatten()
	test = test.reshape(1,-1)
	#test = pca.transform(test)

	#print (model.predict(test))
	print(oc_svm_clf.predict(test))

	temp = rg.create_rand_grid(0.15, SIZE)
	disp.display_grid(temp)
	temp = np.array(temp)
	temp = temp.flatten()
	temp = temp.reshape(1,-1)
	#temp = pca.transform(temp)
	

	print(oc_svm_clf.predict(temp))
	#print (model.predict(temp))
if __name__ == "__main__":
    main()