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
