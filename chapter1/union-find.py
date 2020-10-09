# Rough code, not able to run directly. 

"""quick-find"""

def find(x, list_root):
	return list_root[x]
	
def connected(pointa, pointb, list_root):
	return list_root[pointa]==list_root[pointb]
	
def union(pointa, pointb, list_root):
	roota = list_root[pointa]
	rootb = list_root[pointb]
	for root in list_root:
		if root == roota:
			root = rootb

# find : O(1) ; union : O(n)

"""quick-union"""

def find(x, list_root):
	while x != list_root[x]:
		x = list_root[x]
	return x

def connected(pa, pb, list_root):
	return list_root[pa]==list_root[pb]

def union(pa, pb, list_root):
	list_root[pa] = list_root[pb]

# find: O(n) ; union: O(n)   in worst case

"""weighted quick-union"""

def find(x, list_root):
	while x != list_root[x]:
		x = list_root[x]
	return x

def connected(pa, pb, list_root):
	return list_root[pa]==list_root[pb]

def union(pa, pb, list_root, weight):
	if weight[pa] < weight[pb]:
		list_root[pa] = list_root[pb]
		weight[pb] += weight[pa]
	else:
		list_root[pb] = list_root[pa]
		weight[pa] = weight[pb]

# eliminate bad cases for quick-union, decrease the height of tree
# find: O(lgn) ; union: O(lgn)

"""path compression"""

# could be done to make the tree shorter, make the algorithm even faster.
