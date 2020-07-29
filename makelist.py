import googletrans

translator = googletrans.Translator()

print("var langs = new Array();")
idx = 0

for code,lang in googletrans.LANGUAGES.items():
    t = translator.translate("I love you", dest=code)
    print("langs[" + str(idx) + "]=\"", end = "")
    print(t.text, end = ", ")
    print(lang, end = "\"")
    print(";")
    idx += 1