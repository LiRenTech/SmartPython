from .show import MyClass
import platform


class PersonFactory1:
    SYSTEM_PERFORMANCE = 100

    @staticmethod
    def _get_gender_by_name(name: str) -> bool:
        """如果长度大于5，则判断为男性，否则为女性"""
        return len(name) > 5

    @staticmethod
    def get_Bob():
        result = MyClass(
            name='Tom',
            age=20,
            score_list=[90, 80, 70],
            address='Beijing',
            phone='13800138000',
            email='tom@example.com',
            hobby='reading'
        )
        result.score_list = [int(i * PersonFactory1.SYSTEM_PERFORMANCE / 100) for i in result.score_list]
        result.gender = PersonFactory1._get_gender_by_name(result.name)
        return result

    @classmethod
    def get_Alice(cls):
        result = MyClass(
            name='Jane',
            age=25,
            score_list=[85, 95, 90],
            address='Shanghai',
            phone='13900139000',
            email='jane@example.com',
            hobby='swimming'
        )
        result.score_list = [int(i * cls.SYSTEM_PERFORMANCE / 100) for i in result.score_list]
        result.gender = cls._get_gender_by_name(result.name)
        return result


if platform.system() == 'Windows':
    PersonFactory1.SYSTEM_PERFORMANCE = 150
else:
    PersonFactory1.SYSTEM_PERFORMANCE = 100


class PersonFactory2(PersonFactory1):
    SYSTEM_PERFORMANCE = 120

    @staticmethod
    def get_Tom():
        result = MyClass(
            name='Bob',
            age=20,
            score_list=[90, 80, 70],
            address='Beijing',
            phone='13800138000',
            email='bob@example.com',
            hobby='reading'
        )
        result.score_list = [int(i * PersonFactory2.SYSTEM_PERFORMANCE / 100) for i in result.score_list]
        result.gender = PersonFactory2._get_gender_by_name(result.name)
        return result

    @classmethod
    def get_Jane(cls):
        result = MyClass(
            name='Alice',
            age=25,
            score_list=[85, 95, 90],
            address='Shanghai',
            phone='13900139000',
            email='alice@example.com',
            hobby='swimming'
        )
        result.score_list = [int(i * cls.SYSTEM_PERFORMANCE / 100) for i in result.score_list]
        result.gender = cls._get_gender_by_name(result.name)
