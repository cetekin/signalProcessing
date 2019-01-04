all: 
	pyinstaller --additional-hooks-dir=C:\Users\Çetin\Desktop\signalprocessing\gitHub\signalProcessing --hidden-import sklearn.neighbors.typedefs --hidden-import sklearn.ensemble --hidden-import sklearn.neighbors.quad_tree --hidden-import sklearn.tree._utils projeV2.py
