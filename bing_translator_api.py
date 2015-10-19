
# make sure you install bing translator api before using this script
Client_secret = 'your secrete id'
CUSTOM_ID = 'your client id'

from microsofttranslator import Translator


file_path1 = ''

words =['car']




print'translate... \n '

for k in range(0, len(words)):
    word = words[k]
    grams = open(file_path1 + word + '.txt') # translate from a text file/ comment if you just have a single word
    gram2 = grams.readlines()
    grm = [w.replace('\n','') for w in gram2]

    translator = Translator(CUSTOM_ID, Client_secret)
    trns_word = translator.translate(word, "nl")
    trns_word = trns_word.encode('utf-8') # encode strange chars
    trns_word = trns_word.lower()

    print '{0} finnish translation: '  .format(word) + '{0}' .format(trns_word)

    if not trns_word:
        trns_word = word
    tran_grams = []
    for g in range(len(grm)):
        bg = grm[g].encode('utf-8')
        try:
            translator = Translator(CUSTOM_ID, Client_secret)
            gs = translator.translate(bg, "nl")
            tran_grams.append(gs)
        except:
            print 'no translation for: {0}'.format(bg)

    fl = open(file_path1 + word + '_'+ trns_word.replace(" ","")+ '_tran.txt', 'w') # save to a text file
    for i in range(len(tran_grams)):
        gs  = tran_grams[i].encode('utf-8')
        try:
            fl.write(gs + '\n')
        except:
           print "cant not read {0}" .format(gs)
    fl.close()
