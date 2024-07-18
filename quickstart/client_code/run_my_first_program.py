from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    list1 = [SecretInteger(Input(name=f"list1_int{i}", party=party1)) for i in range(3)]
    list2 = [SecretInteger(Input(name=f"list2_int{i}", party=party1)) for i in range(3)]

    results = []
    for i in range(3):
        result = list1[i] * list2[i] + list1[i]
        results.append(result)

    return [Output(results[i], f"result{i}", party=party1) for i in range(3)]
