class DisjointSetUnion():
    def __init__(self,size):
        # initially, each nod is an independent component
        self.parent = [i for i in range(size+1)]
        # keep the size of each component
        self.size = [1]* (size+1)

    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]

    def union(self,x,y):

        px,py = self.find(x),self.find(y)
        if px == py:
            return px

        if self.size[px]> self.size[py]:
            px,py = py,px 

        self.parent[px] = py 
        self.size[py]+= self.size[px]

        return py

if __name__ == "__main__":
    disj = DisjointSetUnion(10)
    print(disj.union(5,7))
    print('parent',disj.parent)
    print('size',disj.size)
    print(disj.union(6,7))
    print('parent',disj.parent)
    print('size',disj.size)

    disj.union(0,1)
    disj.union(2,1)
    disj.union(1,3)
    print('parent',disj.parent)
    print('size',disj.size)
    disj.union(1,6)
    print('parent',disj.parent)
    print('size',disj.size)

    disj.find(6)
    print('parent',disj.parent)
 
 