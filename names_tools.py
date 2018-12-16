user_info =[]


def show_menu():
    print("-" * 50)
    print("欢迎使用用户注册系统V1.0")
    print("")
    print("1.注册用户名")
    print("2.修改密码")
    print("3.查询所有用户信息")
    print("")
    print("0.退出系统")
    print("-" * 50)


def user_register():
    user_name = input("用户名：")
    for user in user_info:
        if user_name == user["用户名"]:
            print("该用户已经存在")
            break
    else:
        user_code = input("密码：")
        user_dict = {"用户名": user_name, "密码": user_code}
        user_info.append(user_dict)
        print("用户名新建成功")


def user_correct():
    user_name = input("请输入用户名：")
    for user in user_info:
        if user_name == user["用户名"]:
            while True:
                code_output = input("请输入新的密码：")
                if len(code_output) == 0:
                    print("输入的密码不能为空，请重新输入密码")
                else:
                    break
            user["密码"] = code_output
            print("修改成功")
            break
    else:
        print("没有此用户名")


def show_info():
    for user in ["用户名", "密码"]:
        print(user, end="\t\t\t")
    print("")
    for user_id in user_info:
        print("%s\t\t\t%s" %(user_id["用户名"], user_id["密码"]))
