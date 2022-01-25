import sys
import MVVlStd
from MVVlStd import teSep_s, teInPWTypedWVali_fif
from hw_02 import tGetIsValiSep_fef, tCreTIfAllElIsDig_fef

tTskMsg_s = '''
Задача 5

(МОДУЛЬ 2) Создать модуль 2seq.py. Задание:
Пользователь вводит любые цифры через запятую
Сохранить цифры в список
Получить новый список в котором будут только уникальные элементы исходного (уникальным считается символ, который встречается в исходном списке только 1 раз)
Вывести новый список на экран
Порядок цифр в новом списке не важен
Пример работы: Введите элементы списка через запятую: 2,3,4,5,5,6,5,3,9
Результат: 2, 4, 6, 9
'''
print(teSep_s, tTskMsg_s, f'{sys.version=}', teSep_s, 'Result:', '',  sep='\n')

tRes_l = list(teInPWTypedWVali_fif(f' любые цифры через запятую',
    laInPType_cll=lambda _s: tCreTIfAllElIsDig_fef(_s, tGetIsValiSep_fef(_s)))[0])

print('Raw:', tRes_l)
print('Uniq:', list(set(tRes_l)))

print(teSep_s)
