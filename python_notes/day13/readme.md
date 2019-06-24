* python标准库 第三方模块 应用程序自定义模块
* 搜索路径: 存放在sys.path中
* 包：为了按目录来组织模块 python package
* 模块：为了组织函数
* 项目目录:web/{bin,conf,mode,etc}
* basedir:os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
* __name__ == "__main__" 谁去调用 __name__就是谁的名字 可用于屏蔽掉自己的测试代码