import ProjectDeploy
import ConstSettings
import Common.Const
CONST = Common.Const


def main():
    print("Begin")

    # 加载自定义值
    ConstSettings.define()
    # 加载计算值
    ConstSettings.insert_values()
    # 在控制台打印配置内容
    ProjectDeploy.print_info()

    print("End")
    # input("\n\nPress the enter key to exit.")


if __name__ == "__main__":
    main()
