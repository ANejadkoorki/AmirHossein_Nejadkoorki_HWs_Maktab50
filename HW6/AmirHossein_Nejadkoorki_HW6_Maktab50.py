from company_data import product_list, markup_list, discount_list, user_list


def markup_calculator(type_of_products, count):  # type_of_products is string and count is integer
    for i in markup_list:
        if i["product_type"] == type_of_products:
            need_items = i
            break

    #  form the linear equation
    upper_cost, lower_cost, lower_count = need_items["upper_cost"], need_items["lower_cost"], \
        need_items["lower_count"]
    #  point1, point2 = (1,upper_cost), (lower_count,lower_cost)
    m = (upper_cost - lower_cost) / (1 - lower_count)
    y_intercept = upper_cost - (m * 1)

    markup = (m * count) + y_intercept if 1 <= count < lower_count else lower_cost
    return markup


def total_price_calculator(product_type, count, userid=None):
    answer = dict()
    markup = markup_calculator(product_type, count)
    for i in product_list:
        if i["type_of_products"] == product_type:  # product name
            answer['product_name'] = i["name"]
        else:
            continue
        answer['total_price'] = (count * i["price"]) + ((markup / 100) * (count * i["price"]))  # total price

        product_commission_groups = [q for q in i["commission_groups"]]  # commission
        list_of_discount = list()
        for j in discount_list:
            if j["group_name"] in product_commission_groups and userid in j["users"] and j["unit"] == "percent":
                list_of_discount.append(answer['total_price'] * (j["cost"] / 100))
                continue
            if j["group_name"] in product_commission_groups and userid in j["users"] and j["unit"] == "Dollar":
                list_of_discount.append((j["cost"] * count))
                continue
            continue
        if len(list_of_discount) != 0:
            product_finally_discount = min(list_of_discount)
        else:
            product_finally_discount = 0
        answer['total_with_commission'] = answer['total_price'] - product_finally_discount
        answer['discount'] = product_finally_discount
        for z in user_list:  # user
            if userid is None:
                answer['username'] = dict()
                answer['username']['first_name'] = ''
                answer['username']['last_name'] = ''
                break
            elif z["userid"] == userid:
                answer['username'] = dict()
                answer['username']['first_name'] = z["first_name"]
                answer['username']['last_name'] = z["last_name"]
                break
            else:
                continue
        break
    return answer
# code by AmirHossein Nejadkoorki
