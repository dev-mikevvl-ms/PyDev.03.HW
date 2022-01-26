# Mod:hw_02.py

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
