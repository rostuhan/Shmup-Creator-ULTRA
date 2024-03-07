import xmlStuff
Tree = xmlStuff.UltraTree
with open("Tree.txt", "wb") as f:
	Tree.write(f)