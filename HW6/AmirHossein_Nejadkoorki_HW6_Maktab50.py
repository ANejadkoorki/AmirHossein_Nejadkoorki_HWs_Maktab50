from company_data import product_list, markup_list, discount_list, user_list


def markup_counter(type_of_products, count):   # type_of_products is string and count is integer
    for i in markup_list:
        if i["product_type"] == type_of_products:
            nedded_items = i
            break

    #  form the linear equation
    upper_cost, lower_cost, lower_count = nedded_items["upper_cost"], nedded_items["lower_cost"],\
        nedded_items["lower_count"]
    #  point1, point2 = (1,upper_cost), (lower_count,lower_cost)
    m = (upper_cost - lower_cost) / (1 - lower_count)
    y_intercept = upper_cost - (m * 1)

    markup = (m * count) + y_intercept if 1 <= count < lower_count else lower_cost
    return markup



def total_price_calculator(product_type, count,userid = None):
    answer = dict()
    markup = markup_counter(product_type,count)
    for i in product_list:
        if i["type_of_products"] == product_type:   # product name
            answer['product_name'] = i["name"]
        else:
            continue
        answer['total_price'] = ( count * i["price"] ) +  ((markup / 100) * ( count * i["price"] ) )   # total price

        product_commision_groups = [q for q in i["commission_groups"] ]  #  commision
        discount = 0
        for j in discount_list:
            if j["group_name"] in product_commision_groups and userid in j["users"] and j["unit"] == "percent":
                discount += answer['total_price'] *  (  j["cost"] / 100 )
                continue
            if j["group_name"] in product_commision_groups and userid in j["users"] and j["unit"] == "Dollar":
                discount += j["cost"]
                continue
            continue
        answer['total_with_commission'] = answer['total_price'] - discount
        answer['discount'] = discount
        for z in user_list:   # user
            if userid == None:
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












