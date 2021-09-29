from sys import path
path.append("C:\\Users\\umesh\\PycharmProjects\\pythonProject1_module\\module_directory")
# print(path)
import test_module
print(test_module.__counter)

zeros = [i+2 for i in range(5)]
ones = [1 for j in range(5)]
print(test_module.suml(zeros))
print(test_module.prodl(ones))
print(test_module.__counter)
