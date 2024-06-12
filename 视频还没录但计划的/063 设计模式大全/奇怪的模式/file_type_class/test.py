import file_type_object


def main():
    print(file_type_object)
    print(file_type_object.value)

    print(file_type_object._value3)  # 警告但可以访问
    print(file_type_object.__value4)  # 反而又没有警告了

    pass


if __name__ == '__main__':
    main()
