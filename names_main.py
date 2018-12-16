import names_tools
while True:
    names_tools.show_menu()
    user_input = input("请输入需要的操作：")
    if user_input in ["1", "2", "3"]:
        if user_input == "1":
            names_tools.user_register()
        elif user_input == "2":
            names_tools.user_correct()
        elif user_input == "3":
            names_tools.show_info()
    elif user_input == "0":
        break
    else:
        print("输入错误，请重新输入")
