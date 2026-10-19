# shutil标准库:
# 1、文件和目录的复制
#   (1)文件的复制
#   (2)目录的复制
# 2、文件和目录的移动和重命名
#   (1)文件的移动和重命名
#   (2)目录的移动和重命名
# 3、目录的删除
# 以递归删除目录
# 4、压缩包操作
# 创建压缩包
# 解压压缩包

import shutil

#文件的复制
#不复制元数据（创建时间，权限，所有者等）
#shutil.copy("pi.txt", "pi_copy1.txt")
#复制元数据 
#shutil.copy2("pi.txt", "pi_copy2.txt")


#目录的复制(默认递归复制)  存在则报错
#shutil.copytree("test.dir", "copy_test_dir")

#文件和目录的移动和重命名
#shutil.move("move.txt", "copy_test_dir/")
#shutil.move("copy_test_dir/move.txt", "new_name.txt")

#目录的删除  递归从外到内
#shutil.rmtree("./copy_test_dir")

#压缩包处理
#创建压缩包
#make_archive("压缩包名"，“压缩包格式”，“压缩对象”)
#shutil.make_archive("tarball", "zip", "test_dir")
#shutil.unpack_archive("压缩包。zip"，“解压路径”)
shutil.unpack_archive("tarball.zip", "some")
 


