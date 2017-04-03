s = "EBG KVVV vf n fvzcyr yrggre fhofgvghgvba pvcure gung ercynprf n yrggre jvgu gur yrggre KVVV yrggref nsgre vg va gur nycunorg. EBG KVVV vf na rknzcyr bs gur Pnrfne pvcure, qrirybcrq va napvrag Ebzr. Synt vf SYNTFjmtkOWFNZdjkkNH. Vafreg na haqrefpber vzzrqvngryl nsgre SYNT."
word_list = list(s)

word_answer = []
for word in word_list:
    if word == ' ' or word == '.':
        word_answer.append(word)
        continue

    if ord('a') <= ord(word) <= ord('z'):
        temp_number = ord(word)
        for i in range(13):
            temp_number -= 1
            if temp_number == ord('a')-1:
                temp_number = ord('z')
        word = chr(temp_number)
        word_answer.append(word)
        continue

    if ord('A') <= ord(word) <= ord('Z'):
        temp_number = ord(word)
        for i in range(13):
            temp_number -= 1
            if temp_number == ord('A')-1:
                temp_number = ord('Z')
        word = chr(temp_number)
        word_answer.append(word)
        continue

print(''.join(word_answer))
