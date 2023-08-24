'''
    Додаток для демонстрації роботи із Python-колекціями
    =====================================================
    Шснує 4 типи стандартних колекційЖ
    ----------------------------------------------
        1. - Списки (list) *
        2. - Кортежі (tuple)
        3. - Множини (set)
        4. - Словники (dict)
    ---------------------------------------------
    '''

from mylib.menu import *
from mylib.tuples_demo import *

if __name__ == '__main__':
    # 1

    while True:

        # 2
        start_program()

        # 3
        try:
            k = get_choice()
            if k == 1:
                tuples_create_demo()
                tuples_operations_demo()
                tuples_methods_demo()
                tuples_unpack_demo()

            elif k == 2:
                pass
            elif k == 3:
                pass
            elif k == 4:
                break
            else:
                print("  ВИ обрали неіснуючу операцію")

        except ValueError as err:
            print("  ", err)

        if not allow_continue():
            break


    finish_program()