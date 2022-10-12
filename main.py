from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", "r", encoding='utf8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ

def sort_names(list):
  for n in range(2, len(list)):
      value = list[n][0] + " " + list[n][1] + " " + list[n][2]
      res = value.split(' ', maxsplit=2)
      for i in range(len(res)):
          list[n].pop(i)
          list[n].insert(i, res[i])

def sort_phone_numbers(list):
    pattern = r"+7(\2)\3-\4-\5"
    pattern_2 = r" доб.\1"

    pattern_phone = r"(\+7|8)?\s*?(\(\d+\)|\d{3})[-\s]?(\d{3})[-\s]*(\d{2}|\d{4})[-\s]*(\d{2})"
    add_phone_pattern = r"\s\(?доб\.\s*(\d+)\)?"

    for row in range(2, len(list)):
        target = list[row][-2]
        res = re.sub(pattern_phone, pattern, target)
        res = re.sub(add_phone_pattern, pattern_2, res)
        list[row].remove(list[row][-2])
        list[row].insert(-1, res)
    return list

def join_records(list):
    index = []
    new_lists = []
    for n in range(len(list)):
        required = list[n][0]
        for searching in range((n + 1), len(list)):
            if required == list[searching][0]:
                first = list[n]
                second = list[searching]
                for item in range(len(first)):
                    if (first[item] == "") or (first[item] == " "):
                        if (second[item] != "") or (second[item] != " "):
                            first.remove(first[item])
                            first.insert(item, second[item])
                new_lists.append(first)
                index.append(n)
    for i in index:
        contacts_list.pop(i)
    contacts_list.pop(4)
    contacts_list.pop()
    contacts_list.extend(new_lists)
    pprint(contacts_list)

def datawriter():
    # TODO 2: сохраните получившиеся данные в другой файл
    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)

if __name__ == "__main__":
    sort_names(contacts_list)
    sort_phone_numbers(contacts_list)
    join_records(contacts_list)
    datawriter()



