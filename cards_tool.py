#coding=utf-8

#定义一个列表，用于存放字典（用于保存每一个名片信息的字典）
card_list = []




def show_menu():
    print("*" * 50)
    print("欢迎使用《名片管理系统V1.0》")
    print("")
    print("1.新建名片")
    print("2.显示全部")
    print("3.查询名片")
    print("")
    print("0.退出系统")
    print("*" * 50)

def create_card():
    """
    新建名片
    """
    print("-" * 50)
    name = input("请输入姓名:")
    phone = input("请输入电话:")
    wechat = input("请输入微信:")
    email = input("请输入邮箱:")

    #在新建一个名片时，同时创建一个字典，把用户输入的名片信息保存在一个字典中
    card_dict = {"name":name,"phone":phone,"wechat":wechat,"email":email}

    #把字典保存到card_list列表中
    card_list.append(card_dict)
    print("%s名片添加成功" % name)

def show_cards():
    """
    显示所有名片
    """
    print("-" * 50)
    #判断系统中是否有名片
    if len(card_list) == 0:
        print("系统中没有任何名片，请先添加名片")
        #函数结束，返回到调用函数的位置
        return

    for col_name in ["姓名","电话","微信","邮箱"]:
        print(col_name,end = "\t\t")
    print("")

    #遍历列表，取出每一个字典，把字典中的信息显示给用户
    for card_dict in card_list:
        #print(card_dict["name"] + "\t" + card_dict["phone"] + "\t" + card_dict["wechat"] + "\t" + card_dict["email"])
        print("%s\t\t%s\t\t%s\t\t%s"%(card_dict["name"],card_dict["phone"],card_dict["wechat"],card_dict["email"]))

def search_card():
    print("-" * 50)
    find_name = input("请输入要查找的姓名:")
    #遍历列表，取出每一个字典，通过key为name取出存放的姓名
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            for col_name in ["姓名", "电话", "微信", "邮箱"]:
                print(col_name, end="\t\t")
                print("")
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"], card_dict["phone"], card_dict["wechat"], card_dict["email"]))

            #提示用户做修改删除的操作
            action_str = input("请选择针对%s要做的操作：【1】修改；【2】删除；【3】返回" % find_name)
            if action_str == "1":
                update_card(card_dict)
            elif action_str == "2":
                delete_card(card_dict)
            break
    else:
        print("没有找到姓名为%s的名片" % find_name)


def update_card(card_dict):
    """
    修改指定的名片
    """
    card_dict["name"] = input_info(card_dict["name"],"姓名")
    card_dict["phone"] = input_info(card_dict["phone"],"电话")
    card_dict["wechat"] = input_info(card_dict["wechat"],"微信")
    card_dict["email"] = input_info(card_dict["email"],"邮箱")
    # if len(name) != 0:
    #     card_dict["name"] = name
    # if len(phone) != 0:
    #     card_dict["phone"] = phone
    # if len(wechat) != 0:
    #     card_dict["wechat"] = wechat
    # if len(email) != 0:
    #     card_dict["email"] = email
    #
    # print("成功修改%s的图片" % name)


    print("成功修改%s的图片" % card_dict["name"])

def input_info(old_info,tips):
    result = input("请输入新的%s" % tips)
    #判断如果用户输入了新的值，那么返回新的值，如果用户没有输入，那么返回旧的值
    if len(result) != 0:
        return result
    else:
        return old_info


def delete_card(card_dict):
    """
    删除指定名片
    """
    card_list.remove(card_dict)
    print("成功删除%s的名片" % card_dict["name"])








