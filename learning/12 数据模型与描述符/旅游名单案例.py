# 去过普吉岛的人员数据
users_visited_phuket = [
    {
        "first_name": "Sirena",
        "last_name": "Gross",
        "phone_number": "650-568-0388",
        "date_visited": "2018-03-14"
    },
    {
        "first_name": "Shally",
        "last_name": "Pinkman",
        "phone_number": "120-434-8768",
        "date_visited": "2016-12-11"
    }
]

# 去过新西兰的人员数据
users_visited_nz = [
    {
        "first_name": "Justin",
        "last_name": "Malcom",
        "phone_number": "267-282-1964",
        "date_visited": "2011-03-13"
    },
    {
        "first_name": "Sirena",
        "last_name": "Gross",
        "phone_number": "650-568-0388",
        "date_visited": "2018-03-14"
    }
]


def find_potential_customers_v1():
    """找到去过普吉岛但是没去过新西兰的人

    :return :通过 Generator 返回符合条件的旅客记录
    """

    for puket_record in users_visited_phuket:
        is_potential = True
        for nz_record in users_visited_nz:
            if (puket_record["first_name"] == nz_record["first_name"]
                and puket_record["last_name"] == nz_record["last_name"]
                    and puket_record["phone_number"] == nz_record["phone_number"]):
                is_potential = False
                break

        if is_potential:
            yield puket_record


for user in find_potential_customers_v1():
    print('find_potential_customers_v1 >>')
    print(user)


def find_potential_customers_v2():
    """找到去过普吉岛但是没去过新西兰的人，性能改进版

    :return :通过 Generator 返回符合条件的旅客记录
    """
    # 首先，遍历所有新西兰旅客记录，创建查找索引
    nz_record_idx = {
        (rec['first_name'], rec['last_name'], rec['phone_number'])
        for rec in users_visited_nz
    }

    for rec in users_visited_phuket:
        key = (rec['first_name'], rec['last_name'], rec['phone_number'])
        if key not in nz_record_idx:
            yield rec


for user in find_potential_customers_v2():
    print('find_potential_customers_v2 >>')
    print(user)


# 利用集合的游戏规则
class VisitRecod:
    """旅客记录
    :param first_name: 名
    :param last_name: 姓
    :param phone_number: 电话
    :param date_visited: 旅游时间
    """

    def __init__(self, first_name, last_name, phone_number, date_visited):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.date_visited = date_visited

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.comparable_fields == other.comparable_fields
        return False

    @property
    def comparable_fields(self):
        """获取用于对比对象的字段值"""
        return (self.first_name, self.last_name, self.phone_number)
