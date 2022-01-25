import sys
# from MVVlStd import teSep_s, teInPWTypedWVali_fif
import MVVlStd

tTskMsg_s = '''
Задача 4

(МОДУЛЬ 1) Создать новый проект, в нем создать модуль 1seq.py. Задание:
Пользователь вводит количество элементов будущего списка
После этого по очереди по одной вводит любые цифры
Сохранить цифры в список
Отсортировать список по возрастанию и вывести на экран
Пример работы: Введите количество элементов: 3
Введите 1 элемент: 5
Введите 2 элемент: 2
Введите 3 элемент: 43
Вывод: [2, 4, 5]
'''
print(MVVlStd.teSep_s, tTskMsg_s, f'{sys.version=}', MVVlStd.teSep_s, 'Result:', '',  sep='\n')

tResLLen_co = int(MVVlStd.teInPWTypedWVali_fif(
    laWhatInPMsg_s=' Количество элементов будущего списка',
    laVali_cll=lambda _i: 0 < _i < 10,
    laValiInPMsg_s=' a Integer 0 < _i < 10')[0])
print(f'MSG: В списке будет {tResLLen_co} элементов.')

tValiV_t = tuple(range(0, 10))
# tCndInPMsg_s = f' (по очереди по одной вводите любые цифры) a Integer OneOf{tValiV_t}'
# tRes_l = list(MVVlStd.teInPWTypedWVali_fif(f' по очереди по одной любые цифры {tResLLen_co} раза',
tRes_l = list(MVVlStd.teInPWTypedWVali_fif(
    f' по очереди по одной любые цифры', laInPValues_co=tResLLen_co,
    laValiInPMsg_s=f'a Integer OneOf{tValiV_t}',
    laVali_cll=lambda x: x in tValiV_t))
tRes_l.sort()
print(tRes_l)

print(MVVlStd.teSep_s)