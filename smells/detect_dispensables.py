import inspect
from inspect import signature
import gc


class detectdispensables:

    def get_all_classes(self, module_name):
        for a, b in inspect.getmembers(module_name, predicate=inspect.isclass):
            class_list.append(a)
        return class_list

    def lazyclass_check(self, module_name):
        for a, b in inspect.getmembers(module_name, predicate=inspect.isclass):
            obj_count = sum(1 for o in gc.get_referrers(b) if o.__class__ is b)
            if obj_count < 1:
                print(a + '() is a Lazy class. Consider using it or removing it')

    def dataclass_check(self, module_name):
        for a, b in inspect.getmembers(module_name.Math(), predicate=inspect.isclass):
            dc_check = inspect.getmembers(b, predicate=inspect.ismethod)
            if (len(dc_check)) < 1:
                print("No methods defined in the class : " + a)

    def comment_check(self, module_name, min_words):
        for a, b in inspect.getmembers(module_name.Math(), predicate=inspect.ismethod):
            cmt = [line for line in inspect.getsourcelines(b)[0] if line.strip().startswith('#')]
            for i in cmt:
                if(len(i.split()))<min_words:
                    print("Use meaningful comments. Short comments found in the method: " + a)