import grid as gr
import rand_grid as rg
import display as disp

def main():
	SIZE = 50
	base = []
	#for i in range(10):
	for i in range(2): #2 
		res = gr.create_grid()
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
	for grid in base:
		for i in range(100):
			train_grids_pos.append(rg.create_pos_grid(grid))
			train_grids_neg.append(rg.create_rand_grid(0.5))
	
if __name__ == "__main__":
    main()