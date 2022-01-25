import sys
import MVVlStd
from MVVlStd import teSep_s, teInPWTypedWVali_fif

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

def tGetIsValiSep_fef(laTs_s, laSep_t=(',', ';', '/')):
  # if not isinstance(laTs_s, str):
  #   raise TypeError(f"laTs_s should be string, but NOW {type(laTs_s).__name__}.")
  loCoSepIt2S_t = tuple(laTs_s.count(_el) for _el in laSep_t)
  loAllSepCoSum_i = sum(loCoSepIt2S_t)
  if loAllSepCoSum_i == 0: return None
  else:
    for l_s, l_co in zip(laSep_t, loCoSepIt2S_t):
      if l_co == 0: continue
      elif l_co != loAllSepCoSum_i:
        raise ValueError(f"In str:'{laTs_s}' there should be used only one of {laSep_t} separator.")
      else: return l_s

def tCreTIfAllElIsDig_fef(laTs_s, laSep_s1):
  if not laTs_s.strip(): return ()
  lo_t = tuple(int(_el) for _el in laTs_s.split(laSep_s1))
  if all(0<= _el <=9 for _el in lo_t): return lo_t
  else: raise ValueError(f"In str:'{laTs_s}' at least one of El NOT (0<= _el <=9).")

tValiV_t = tuple(range(0, 10))
tRes_l = list(teInPWTypedWVali_fif(f' любые цифры через запятую',
    laInPType_cll=lambda _s: tCreTIfAllElIsDig_fef(_s, tGetIsValiSep_fef(_s)))[0])

print('Raw:', tRes_l)
print('Uniq:', list(set(tRes_l)))

print(teSep_s)
