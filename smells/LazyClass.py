import ast
import sys

sys.path.insert(1, 'C:\\Users\\jgatte\\Desktop\\SW Arch and Design\\Course Project\\my_cs_detector\\Test')

#import mymath

class Visitor(ast.NodeVisitor):

    def visit_Assign(self, node:ast.Assign):
        print("=======Inside Assign Class========")
        d=[]
        d=node.targets[0]
        v=node.value
        print("target print", d.id)
        print("target print", v.func.id)

def main():
    with open('C:\\Users\\jgatte\\Desktop\\SW Arch and Design\\Course Project\\my_cs_detector\\Test\\Experiment.py') as f:
        code = f.read()
        node = ast.parse(code)
        Visitor().visit(node)


if __name__ == '__main__':
    main()