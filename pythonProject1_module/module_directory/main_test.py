from sys import path
print(path)
import test_module
print(test_module.__doc__)
help(test_module)

path.append("C:\\Users\\umesh\PycharmProjects\pythonProject1_module\my_packages")
import Extra.good.beta
print(Extra.good.beta.funB())
