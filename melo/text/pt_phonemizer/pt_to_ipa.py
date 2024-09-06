from .cleaner import spanish_cleaners
from .gruut_wrapper import Gruut

def pt2ipa(text):
    e = Gruut(language="pt-pt", keep_puncs=True, keep_stress=True, use_espeak_phonemes=True)
    # text = spanish_cleaners(text)
    phonemes = e.phonemize(text, separator="")
    return phonemes


if __name__ == '__main__':
  print(pt2ipa('Eae gente boa, como você está?'))