import grid as gr
import rand_grid as rg
import display as disp
import numpy as np
from sklearn.naive_bayes import BernoulliNB

def main():
	SIZE = 50
	base = []
	for i in range(1):
	#for i in range(2): #2 
		res = gr.create_grid(SIZE)
		if(res == 1):
			print("QUIT")
			return 1
		base.append(res)



	#disp.display_grid(grid = base[0])							#Display base grid
	#disp.display_grid(grid = rg.create_pos_grid(base[0]))		#Display modified grid
	#disp.display_grid(grid = base[1])							#Display base grid 2
	#disp.display_grid(grid = rg.create_pos_grid(base[1]))		#Display modified grid 2

	train_grids_pos = []
	train_grids_neg = []
	y = []
	for grid in base:
		for i in range(50):
			y.append(1)
			temp = rg.create_pos_grid(grid)
			train_grids_pos.append(','.join(str(col) for row in temp for col in row))
		for i in range(100):
			y.append(0)
			temp = rg.create_rand_grid(0.5, SIZE)
			train_grids_neg.append(','.join(str(col) for row in temp for col in row))

	X = train_grids_pos + train_grids_neg
	X = np.array(X).reshape(-1, 1)
	y= np.array(y)

	clf = BernoulliNB(alpha = 1.0, binarize = 0.0, class_prior=None,fit_prior=True)
	clf = clf.fit(X,y)

	test = gr.create_grid(SIZE)
	test = ','.join(str(col) for row in temp for col in row)
	print (clf.predict(gr))

if __name__ == "__main__":
    main()