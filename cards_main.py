#coding=utf-8

from cards_tool import show_menu
from cards_tool import create_card
from cards_tool import show_cards
from cards_tool import search_card

#循环永远成立，知道用户输入0，否则永远回到首页面
while True:
    # todo 添加欢迎界面（首页）
    show_menu()

    action_str = input("请输入您要执行的操作:")

    #判断用户输入的操作是什么
    if action_str in ["1","2","3"]:   #1,2,3之所以是字符串，而不是数字，因为input输入的是字符串
        #操作名片
        if action_str == "1":
            print("您选择的操作是【1】，新建名片")
            create_card()

        if action_str == "2":
            print("您选择的操作是【2】，显示全部名片")
            show_cards()


        if action_str == "3":
            print("您选择的操作是【3】，查询指定名片")
            search_card()


    elif action_str == "0":
        #退出程序
        print("欢迎再次使用本系统，再见")
        break
    else:
        print("您的输入有误，请重新输入")