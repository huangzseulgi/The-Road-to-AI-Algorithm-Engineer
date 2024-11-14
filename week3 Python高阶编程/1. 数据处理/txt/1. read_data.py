path = "resources/"

# 使用read方法读取数据
with open(path + "example_1.txt", "r") as f:
    content = f.read()
    print(content)

# 使用readline方法逐行读取数据
with open(path + "training_log.txt", "r") as f:
    line = f.readline()
    while line:
        print(line, end="")
        line = f.readline()

#  使用write方法读取数据
with open(path + "example_1.txt", "w") as f:
    f.write("hello")
with open(path + "example_1.txt", "a") as f:  # 追加
    f.write("word")

#  使用writelines方法读取数据
lines = ["hello world", "hello", "world"]
with open(path + "example_1.txt", "w") as f:
    f.writelines(line + '\n' for line in lines)




