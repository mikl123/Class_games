"""
My game
"""
import random
import my_game_classes

Striyska = my_game_classes.Street("вулиця Стрийська")
Striyska.set_description("Неперевершена вулиця Стрийська")
Striyska.add_available_actions("писати іспит")

Kozelnitska = my_game_classes.Street("вулиця Козельницька")
Kozelnitska.set_description("Неповторна вулиця Козельницька")
Kozelnitska.add_available_actions("протистояти")

Franka = my_game_classes.Street("вулиця Франка")
Franka.set_description("Найгарніша вулиця Франка")
Franka.add_available_actions("вчитися")

Shevchenka = my_game_classes.Street("вулиця Шевченка")
Shevchenka.set_description("Романтична вулиця Шевченка")
Shevchenka.add_available_actions("протистояти")

Krakivska = my_game_classes.Street("вулиця Краківська")
Krakivska.set_description("Квітуча вулиця Краківська")
Krakivska.add_apple_tree()
Krakivska.available_actions.remove("вліво")
Krakivska.link_room(Shevchenka, "вправо")
Shevchenka.link_room(Franka, "вправо")
Franka.link_room(Kozelnitska, "вправо")
Kozelnitska.link_room(Striyska, "вправо")

Striyska.link_room(Kozelnitska, "вліво")
Kozelnitska.link_room(Franka, "вліво")
Franka.link_room(Shevchenka, "вліво")
Shevchenka.link_room(Krakivska, "вліво")

Ucu_diplom = my_game_classes.Item("диплом уку", "Це легендарний предмет")
Ucu_diplom.set_action("Побудуй діаграму Гассе на булеані!!!")
Apple = my_game_classes.Item("яблучко", "Це звичайне яблучко")
Apple.set_action("Візьми яблучко")
Knowledge = my_game_classes.Item("Знання", "Це твої зання")
Knowledge.set_action("Я складу цей іспит")


Gopnik = my_game_classes.Enemy("Лотр", "Негідник і розбійник")
Gopnik.set_weakness(Apple)
Gopnik.set_conversation("Відавай все що маєш!!!")
Gopnik2 = my_game_classes.Enemy("Розбійник", "Не дуже хороший хлопчик")
Gopnik2.set_weakness(Apple)
Gopnik2.set_conversation("Давай гроші")
Seminar = my_game_classes.Enemy("Семінар з Мат. Аналізу", "Спосіб здобути знання")
Session = my_game_classes.MathExam("Сесія з Мат. Аналізу", "Легендарний босс", 2)
Session.set_weakness(Knowledge)

Striyska.set_character(Session)
Kozelnitska.set_character(Gopnik2)
Franka.set_character(Seminar)
Shevchenka.set_character(Gopnik)
avoska = []
continue_game = True
current_street = Krakivska
while continue_game:
    current_street.get_details()
    inh = (
        current_street.get_character()
        if (
            current_street.get_character()
            and not current_street.get_character().get_defeated()
        )
        else None
    )
    if inh:
        inh.describe()
        inh.talk()
    action = input("> ")
    if action in current_street.get_available():
        if action == "зірвати яблучко":
            if random.randint(1, 2) == 1:
                print("Тобі поталанило і ти зірвав яблучко")
                avoska.append("яблучко")
            else:
                print("Тобі не поталанило зірвати яблучко")
        elif action == "вліво" or action == "вправо":
            current_street = current_street.linked_sides[action]
            continue
        elif action == "вчитися":
            while True:
                v_1 = random.randint(1, 100)
                v_2 = random.randint(1, 100)
                try:
                    summary = int(input(f"введи {v_1} + {v_2} > "))
                    if summary == v_2 + v_1:
                        break
                    else:
                        print("Не правильно, спробуй ще раз")
                except ValueError:
                    print("Не правильний формат відповіді")
            print("Ти отримав знання")
            inh.fight()
            current_street.del_available("вчитися")
            avoska.append("знання")
        elif action == "писати іспит":
            print("Ось це й час і прийшов.")
            item = input("Що ви хочете використати щоб скласти іспит > ")
            if item != "знання":
                print("Ха-Ха-Ха тобі це не допоможе, але ти маєш все ще шанси!!!")
                equations=inh.get_equations()
                for equation in equations:
                    res= input(f"Скільки буде {equation[0]} + {equation[1]}  > ")
                    try:
                        if int(res)!=equation[0] + equation[1]:
                            print("Не правильна відповідь")
                            print("Ти програв")
                            continue_game = False
                            break
                    except ValueError:
                        print("Не правильний формат відповідь")
                        print("Ти програв")
                        continue_game = False
                        break
                if continue_game:
                    print("Хоч це були і не легкі приклади але ти зміг")
                    print("Ти переміг")
                    continue_game = False
            else:
                print("Добре що ти підготувався до іспиту")
                print(
                    "Ти успішно склав іспит і отримав легендарний предмет - ДИПЛОМ УКУ"
                )
                print("Далі ти сам маєш визначити що з ним робити")
                print("Ти переміг")
                continue_game = False
        elif action == "протистояти":
            item = input(
                "Що ви хочете використати щоб протистояти поганому хлопчику > "
            )
            if item in avoska:
                if item != inh.weakness.name:
                    inh.weakness.describe()
                    print("А нащо мені це???")
                    print("Ти програв")
                    continue_game = False
                else:
                    inh.weakness.describe()
                    print("Ти віддав хулігану яблучко, він ввічливо подякуав і пішов.")
                    inh.fight()
                    avoska.remove("яблучко")
                    current_street.del_available("протистояти")
            else:
                print(f"Ти не маєш {item} в авосьці")
                inh.add_patience()
                if inh.get_patience() == 1:
                    print(f"У {inh.name} вичерпується терпіння.")
                elif inh.get_patience() == 2:
                    print(f"У {inh.name} закінчилося терпіння.")
                    print("Ви програли")
                    continue_game = False
    else:
        print(f"Я не можу {action}")
