#/content/MeloTTS/melo/text/symbols.py
# punctuation = ["!", "?", "…", ",", ".", "'", "-"]
punctuation = ["!", "?", "…", ",", ".", "'", "-", "¿", "¡"]
pu_symbols = punctuation + ["SP", "UNK"]
pad = "_"

# chinese
zh_symbols = [
    "E",
    "En",
    "a",
    "ai",
    "an",
    "ang",
    "ao",
    "b",
    "c",
    "ch",
    "d",
    "e",
    "ei",
    "en",
    "eng",
    "er",
    "f",
    "g",
    "h",
    "i",
    "i0",
    "ia",
    "ian",
    "iang",
    "iao",
    "ie",
    "in",
    "ing",
    "iong",
    "ir",
    "iu",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "ong",
    "ou",
    "p",
    "q",
    "r",
    "s",
    "sh",
    "t",
    "u",
    "ua",
    "uai",
    "uan",
    "uang",
    "ui",
    "un",
    "uo",
    "v",
    "van",
    "ve",
    "vn",
    "w",
    "x",
    "y",
    "z",
    "zh",
    "AA",
    "EE",
    "OO",
]
num_zh_tones = 6

# japanese
ja_symbols = [
    "N",
    "a",
    "a:",
    "b",
    "by",
    "ch",
    "d",
    "dy",
    "e",
    "e:",
    "f",
    "g",
    "gy",
    "h",
    "hy",
    "i",
    "i:",
    "j",
    "k",
    "ky",
    "m",
    "my",
    "n",
    "ny",
    "o",
    "o:",
    "p",
    "py",
    "q",
    "r",
    "ry",
    "s",
    "sh",
    "t",
    "ts",
    "ty",
    "u",
    "u:",
    "w",
    "y",
    "z",
    "zy",
]
num_ja_tones = 1

# English
en_symbols = [
    "aa",
    "ae",
    "ah",
    "ao",
    "aw",
    "ay",
    "b",
    "ch",
    "d",
    "dh",
    "eh",
    "er",
    "ey",
    "f",
    "g",
    "hh",
    "ih",
    "iy",
    "jh",
    "k",
    "l",
    "m",
    "n",
    "ng",
    "ow",
    "oy",
    "p",
    "r",
    "s",
    "sh",
    "t",
    "th",
    "uh",
    "uw",
    "V",
    "w",
    "y",
    "z",
    "zh",
]
num_en_tones = 4

#language_tone_start_map
# Korean
kr_symbols = ['ᄌ', 'ᅥ', 'ᆫ', 'ᅦ', 'ᄋ', 'ᅵ', 'ᄅ', 'ᅴ', 'ᄀ', 'ᅡ', 'ᄎ', 'ᅪ', 'ᄑ', 'ᅩ', 'ᄐ', 'ᄃ', 'ᅢ', 'ᅮ', 'ᆼ', 'ᅳ', 'ᄒ', 'ᄆ', 'ᆯ', 'ᆷ', 'ᄂ', 'ᄇ', 'ᄉ', 'ᆮ', 'ᄁ', 'ᅬ', 'ᅣ', 'ᄄ', 'ᆨ', 'ᄍ', 'ᅧ', 'ᄏ', 'ᆸ', 'ᅭ', '(', 'ᄊ', ')', 'ᅲ', 'ᅨ', 'ᄈ', 'ᅱ', 'ᅯ', 'ᅫ', 'ᅰ', 'ᅤ', '~', '\\', '[', ']', '/', '^', ':', 'ㄸ', '*']
num_kr_tones = 1

# Spanish
es_symbols = [
        "N",
        "Q",
        "a",
        "b",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "ɑ",
        "æ",
        "ʃ",
        "ʑ",
        "ç",
        "ɯ",
        "ɪ",
        "ɔ",
        "ɛ",
        "ɹ",
        "ð",
        "ə",
        "ɫ",
        "ɥ",
        "ɸ",
        "ʊ",
        "ɾ",
        "ʒ",
        "θ",
        "β",
        "ŋ",
        "ɦ",
        "ɡ",
        "r",
        "ɲ",
        "ʝ",
        "ɣ",
        "ʎ",
        "ˈ",
        "ˌ",
        "ː"
    ]
num_es_tones = 1

# Portuguese
es_symbols = [
    "N",      # Letra maiúscula 'N'
    "Q",      # Letra maiúscula 'Q'
    "a",      # Letra minúscula 'a'
    "b",      # Letra minúscula 'b'
    "d",      # Letra minúscula 'd'
    "e",      # Letra minúscula 'e'
    "f",      # Letra minúscula 'f'
    "g",      # Letra minúscula 'g'
    "h",      # Letra minúscula 'h'
    "i",      # Letra minúscula 'i'
    "j",      # Letra minúscula 'j'
    "k",      # Letra minúscula 'k'
    "l",      # Letra minúscula 'l'
    "m",      # Letra minúscula 'm'
    "n",      # Letra minúscula 'n'
    "o",      # Letra minúscula 'o'
    "p",      # Letra minúscula 'p'
    "s",      # Letra minúscula 's'
    "t",      # Letra minúscula 't'
    "u",      # Letra minúscula 'u'
    "v",      # Letra minúscula 'v'
    "w",      # Letra minúscula 'w'
    "x",      # Letra minúscula 'x'
    "y",      # Letra minúscula 'y'
    "z",      # Letra minúscula 'z'
    "ɑ",      # Letra minúscula 'ɑ' (vogal aberta posterior não arredondada)
    "æ",      # Letra minúscula 'æ' (vogal aberta dianteira)
    "ʃ",      # Letra minúscula 'ʃ' (consoante fricativa pós-alveolar surda)
    "ʑ",      # Letra minúscula 'ʑ' (consoante fricativa pós-alveolar sonora)
    "ç",      # Letra minúscula 'ç' (consoante fricativa palatal surda)
    "ɯ",      # Letra minúscula 'ɯ' (vogal fechada posterior não arredondada)
    "ɪ",      # Letra minúscula 'ɪ' (vogal fechada anterior não arredondada)
    "ɔ",      # Letra minúscula 'ɔ' (vogal aberta média posterior arredondada)
    "ɛ",      # Letra minúscula 'ɛ' (vogal aberta dianteira)
    "ɹ",      # Letra minúscula 'ɹ' (consoante líquida retroflexa)
    "ð",      # Letra minúscula 'ð' (consoante fricativa dental sonora)
    "ə",      # Letra minúscula 'ə' (vogal média central)
    "ɫ",      # Letra minúscula 'ɫ' (consoante líquida retroflexa escura)
    "ɥ",      # Letra minúscula 'ɥ' (consoante aproximante palatal)
    "ɸ",      # Letra minúscula 'ɸ' (consoante fricativa bilabial surda)
    "ʊ",      # Letra minúscula 'ʊ' (vogal fechada posterior arredondada)
    "ɾ",      # Letra minúscula 'ɾ' (consoante vibrante simples)
    "ʒ",      # Letra minúscula 'ʒ' (consoante fricativa pós-alveolar sonora)
    "θ",      # Letra minúscula 'θ' (consoante fricativa dental surda)
    "β",      # Letra minúscula 'β' (consoante fricativa bilabial sonora)
    "ŋ",      # Letra minúscula 'ŋ' (consoante nasal velar)
    "ɦ",      # Letra minúscula 'ɦ' (consoante fricativa glotal sonora)
    "ɡ",      # Letra minúscula 'ɡ' (consoante oclusiva velar sonora)
    "r",      # Letra minúscula 'r'
    "ɲ",      # Letra minúscula 'ɲ' (consoante nasal palatal)
    "ʝ",      # Letra minúscula 'ʝ' (consoante fricativa palatal sonora)
    "ɣ",      # Letra minúscula 'ɣ' (consoante fricativa velar sonora)
    "ʎ",      # Letra minúscula 'ʎ' (consoante lateral palatal)
    "ˈ",      # Sinal de acentuação primária (estresse)
    "ˌ",      # Sinal de acentuação secundária
    "ː"       # Sinal de prolongamento (longa duração de fonema)
]
num_pt_tones = 1

# French
fr_symbols = [
    "\u0303",
    "œ",
    "ø",
    "ʁ",
    "ɒ",
    "ʌ",
    "ɜ",
    "ɐ"
]
num_fr_tones = 1

# German
de_symbols = [
    "ʏ",
    "̩"
  ]
num_de_tones = 1

# Russian
ru_symbols = [
    "ɭ",
    "ʲ",
    "ɕ",
    "\"",
    "ɵ",
    "^",
    "ɬ"
]
num_ru_tones = 1

# combine all symbols
normal_symbols = sorted(set(zh_symbols + ja_symbols + en_symbols + kr_symbols + es_symbols + fr_symbols + de_symbols + ru_symbols + pt_symbols))
symbols = [pad] + normal_symbols + pu_symbols
sil_phonemes_ids = [symbols.index(i) for i in pu_symbols]

# combine all tones
num_tones = num_zh_tones + num_ja_tones + num_en_tones + num_kr_tones + num_es_tones + num_fr_tones + num_de_tones + num_ru_tones + num_pt_tones

# language maps
language_id_map = {"ZH": 0, "JP": 1, "EN": 2, "ZH_MIX_EN": 3, 'KR': 4, 'ES': 5, 'SP': 5 ,'FR': 6, 'PT': 7}
num_languages = len(language_id_map.keys())

language_tone_start_map = {
    "ZH": 0,
    "ZH_MIX_EN": 0,
    "JP": num_zh_tones,
    "EN": num_zh_tones + num_ja_tones,
    'KR': num_zh_tones + num_ja_tones + num_en_tones,
    "ES": num_zh_tones + num_ja_tones + num_en_tones + num_kr_tones,
    "SP": num_zh_tones + num_ja_tones + num_en_tones + num_kr_tones,
    "FR": num_zh_tones + num_ja_tones + num_en_tones + num_kr_tones + num_es_tones,
    "PT": num_zh_tones + num_ja_tones + num_en_tones + num_kr_tones + num_es_tones + num_fr_tones,
}

if __name__ == "__main__":
    a = set(zh_symbols)
    b = set(en_symbols)
    print(sorted(a & b))
