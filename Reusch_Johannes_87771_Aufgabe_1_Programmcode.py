import graphviz as gr 


class ANDNODE:
    def __init__(self, name):
        self.name = name
        self.nodes = []
    def add(self, node):
        self.nodes.append(node)
        return
    #???????????????????????????????????
#    def topdown(self, mat):
 #       return mat
   
 
 
class ORNODE:
    def __init__(self, name):
        self.name = name
        self.nodes = []
    def add(self, node):
        self.nodes.append(node)
        return
    #????????????????????????????
  #  def topdown(self, mat):
   #     return mat
   
class EVENT: # EVENT = Eingang
    def __init__(self, name):
        self.name = name
        return
    #??????
   # def topdown(self, mat):
    #    return mat
 # alskdjajskld
def  maptree (dot, top):
    dot.node(top.name, top.name)
    if top.nodes :    
        for a in top.nodes :
            dot.edge(top.name + (top.nodes[a]).name)
            maptree(dot,top.nodes[a])
    




def main():
    TOP = ANDNODE('TOP')
    A = ORNODE('A')
    B = ORNODE('B')
    D = ANDNODE('D')
    TOP.add(A)
    TOP.add(B)
    B.add(D)
    A.add("input 1")
    print(A.name)
    dot = gr.Digraph('Baum')
    maptree(dot, TOP)
    print(dot.source)
    dot.render('output')
if __name__ == "__main__":
    main()