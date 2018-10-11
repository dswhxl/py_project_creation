#! /usr/bin/env python
# coding=utf-8
"""
desc: project生成脚本, 生成具有指定结构的project
      包含log/, conf/, data/, src/, src/lib等
      统一在项目根目录下运行python -m {package.path.module.name}即可，所有的包引用使用根目录全路径模式
"""

import sys
import os


def generate_project(project_name, where="./"):
    """
    desc: 在{where}位置创建名为{project_name}的project
    """
    root_path = "%s/%s" % (where, project_name)
    print "create project at: '%s'" % root_path
    os.system("mkdir -p '%s'" % root_path)
    os.system("cp -fr backup/* '%s'" % root_path)


def print_usage():
    """
    desc: 打印帮助信息
    """
    print "usage: python generate_project {project_name} {where}"
    print "       {project_name} is the name of the project that you want to create."
    print "       {where} specifies the location where you want to create your project. \
leave it empty if you take the current workspace directory as the root path."


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(0)
    if sys.argv[1] in ["-h", "--help"]:
        print_usage()
        sys.exit(0)

    project_name = sys.argv[1]
    root_path = "./"
    if (len(sys.argv)) >= 3:
        root_path = sys.argv[2]
    generate_project(project_name, root_path)
