import graphviz as gr 


class ANDNODE:
    def __init__(self, name):
        self.name = name
        self.nodes = []
    def add(self, node):
        self.nodes.append(node)
        return
    #???????????????????????????????????
    def topdown(self, mat):
        for a in self.nodes :
            mat = a.topdown
        return mat
   
 
 
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
    # Eingang gibt sich selbst zurück
    def topdown(self, mat):
        return [[self.name]]
 # alskdjajskld

def  maptree (dot, top):
    dot.node(top.name, top.name)
    # muss noch eckig werden
    if top.nodes :    
        for a in top.nodes :
            dot.edge(top.name + (top.nodes[a]).name)
            maptree(dot,top.nodes[a])
    print(dot.source)
    


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
    mat = [[TOP]]
    print(mat)
    dot = gr.Digraph('Baum')
    maptree(dot, TOP)
    dot.render('output')
    
if __name__ == "__main__":
    main()