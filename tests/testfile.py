class MethodList:
    def __init__(self, tokens, state):
        self.methods = {}
        for t in tokens:
            if type(t) is MethodList:
                for method in t.methods:
                    self.methods[method.name] = method
            elif type(t) is MethodDef:
                self.methods[t.name] = t
        exit()
        print("yay")
        test()

    @testmethod
    def get(self, name):
        return self.methods[name]

    def eval(self):
        pass

class ClassName(object):
    """docstring for . \b \n \c"""

    def __init__(self, arg):
        super(, self).__init__()
        self.arg = arg

        5 + 2 + 3 - 2
