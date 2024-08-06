my_dict = {"Alexey": 25,
           "Tatyana": 48,
           "Nikolay": 16,
           "Yulia": 31}
print("Dict: ", my_dict)
print("Existing value: ", my_dict.get("Yulia"))
print("Not existing value: ", my_dict.get("Andrey"))
my_dict.update({"Petr": 36,
                "Stanislav": 18,})
print("Deleted value: ", my_dict.pop("Nikolay"))
print("Modified dict: ", my_dict)

my_set = {1, 9.2, "Yes", True, 9.2, "Petr", "Yes"}
print("Set: ", my_set)
my_set.update(["Windows", 354])
my_set.remove(1)
print("Modified set: ", my_set)
