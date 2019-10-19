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
 #asdasd

def  maptree (dot, punkt):
    dot.node(punkt.name, punkt.name)
    # muss noch eckig werden
    for a in punkt.nodes :
        type(self).__name__ 
        maptree(dot,punkt.nodes[a])
        dot.edge(punkt.name + (punkt.nodes[a]).name)
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
    dot.render('output',view=True)
    
if __name__ == "__main__":
    main()