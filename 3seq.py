import sys
import MVVlStd
from MVVlStd import teSep_s, teInPWTypedWVali_fif
from hw_02 import tGetIsValiSep_fef, tCreTIfAllElIsDig_fef

tTskMsg_s = '''
Задача 6

(МОДУЛЬ 3) В проекте создать новый модуль 3seq.py. Задание:
Пользователь вводит элементы 1-го списка (по очереди как в МОДУЛЬ 1 или вместе как в МОДУЛЬ 2)
Затем он вводит элементы 2-го списка
Удалить из первого списка элементы присутствующие во 2-ом и вывести результат на экран
Пример работы: Введите элементы 1-го списка: 1,2,3,4,5
Введите элементы 2-го списка: 2,5
Результат: 1,3,4
'''
print(teSep_s, tTskMsg_s, f'{sys.version=}', teSep_s, 'Result:', '',  sep='\n')

tSrc_l = list(teInPWTypedWVali_fif(f' 1-ый список - любые цифры через запятую',
    laInPType_cll=lambda _s: tCreTIfAllElIsDig_fef(_s, tGetIsValiSep_fef(_s)),
    )[0])
tSrc_set = set(tSrc_l)
tRm_l = list(teInPWTypedWVali_fif(f' 1-ый список - любые цифры через запятую',
    laInPType_cll=lambda _s: tCreTIfAllElIsDig_fef(_s, tGetIsValiSep_fef(_s)),
    )[0])
tRm_set = set(tRm_l)
print(f'(Fr:{tSrc_l} remove El exist in2:{tRm_l})\n(Unstable & UniqOnlyEl)=> {list(tSrc_set - tRm_set)}')
print('(Stable)=> ', list(_el for _el in tSrc_l if _el not in tRm_set))

print(teSep_s)
