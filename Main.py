import ProjectDeploy
import ConstSettings
import Common.Const
CONST = Common.Const


def main():
    print("Begin")

    ConstSettings.define()
    ConstSettings.insert_values()
    ProjectDeploy.print_info()

    print("End")
    # input("\n\nPress the enter key to exit.")


if __name__ == "__main__":
    main()
