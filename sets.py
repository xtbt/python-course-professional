def remove_duplicates_manual(my_list: list) -> list:
    resultant_list: list = []
    for element in my_list:
        if element not in resultant_list:
            resultant_list.append(element)
    return resultant_list


def remove_duplicates_with_sets(my_list: list) -> list:
    return list(set(my_list))


def main():
    original_list = [1,1,2,2,3,4]
    print(remove_duplicates_manual(original_list))
    print(remove_duplicates_with_sets(original_list))


if __name__ == '__main__':
    main()