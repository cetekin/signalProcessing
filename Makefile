all: 
	pyinstaller --additional-hooks-dir=/home/tekin/Desktop/gitRepos/signalProcessing --hidden-import sklearn.neighbors.typedefs --hidden-import sklearn.ensemble --hidden-import sklearn.neighbors.quad_tree --hidden-import sklearn.tree._utils projeV2.py
