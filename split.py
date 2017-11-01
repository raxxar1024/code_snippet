# -*- coding:utf-8 -*-


def get_legend_copy_name(old_id, db_id):
    lst_str = old_id.split("_")
    time_string = lst_str[0]
    user_id = lst_str[1]
    random_str = lst_str[2]
    return "%s_%s_%s_%d" % (time_string, user_id, random_str, db_id)


def get_table_template_legend_obj_copy_name(old_id, db_id):
    lst_str = old_id.split("_")
    time_string = lst_str[0]
    user_id = lst_str[1]
    random_str = lst_str[2]
    if len(lst_str) == 5:
        x = lst_str[3]
        y = lst_str[4]
    else:
        x = lst_str[4]
        y = lst_str[5]
    return "%s_%s_%s_%d_%s_%s" % (time_string, user_id, random_str, db_id, x, y)


def get_template_template_legend_obj_copy_name(old_id, db_id):
    lst_str = old_id.split("_")
    time_string = lst_str[0]
    user_id = lst_str[1]
    random_str = lst_str[2]
    if len(lst_str) == 4:
        template_legend_id = lst_str[3]
    else:
        template_legend_id = lst_str[4]
    return "%s_%s_%s_%d_%s" % (time_string, user_id, random_str, db_id, template_legend_id)


if __name__ == '__main__':
    print get_legend_copy_name("20171031083326464_4_CFDU4S68", 1)
    print get_legend_copy_name("20171031083326464_4_CFDU4S68_1", 2)

    print get_table_template_legend_obj_copy_name("20171031171444112_4_UZFES3UZ_0_3", 1)
    print get_table_template_legend_obj_copy_name("20171031171444112_4_UZFES3UZ_13_0_3", 2)

    print get_template_template_legend_obj_copy_name("20171031171444112_4_UZFES3UZ_14", 1)
    print get_template_template_legend_obj_copy_name("20171031171444112_4_UZFES3UZ_15_14", 2)
