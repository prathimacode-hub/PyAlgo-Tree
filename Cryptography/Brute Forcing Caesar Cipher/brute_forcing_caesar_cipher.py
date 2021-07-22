# -*- coding: utf-8 -*-
"""Hacking Caeser cipher
"""

# Code to use Brute force on Caesar cipher if you don't have the key.
msg=input("Enter encrypted message: ")
msg=msg.upper()
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# loop through every possible key
for key in range(len(LETTERS)):

    # Set translated to the blank string so that the previous iteration's value for translated is cleared.
    translated = ''

    # run the encryption/decryption code on each symbol in the message
    for i in msg:
        if i in LETTERS:
            num = LETTERS.find(i) # get the number of the symbol
            num = num - key  #to get the orignal letter (before the shifting)

            # handle the wrap-around if num is 26 or larger or less than 0
            if num < 0:
                num = num + len(LETTERS)

            # add number's symbol at the end of translated
            translated = translated + LETTERS[num]

        else:
            # just add the letter(i) without encrypting/decrypting. (For spaces or chars other than alphabets)
            translated = translated + i

    # display the current key being tested, along with its decryption
    print('Key %s: %s' % (key, translated))


''' test cases:
encrypted string: 'Rcb Vjprl'
Output:
Key 0: RCB VJPRL
Key 1: QBA UIOQK
Key 2: PAZ THNPJ
Key 3: OZY SGMOI
Key 4: NYX RFLNH
Key 5: MXW QEKMG
Key 6: LWV PDJLF
Key 7: KVU OCIKE
Key 8: JUT NBHJD
Key 9: ITS MAGIC
Key 10: HSR LZFHB
Key 11: GRQ KYEGA
Key 12: FQP JXDFZ
Key 13: EPO IWCEY
Key 14: DON HVBDX
Key 15: CNM GUACW
Key 16: BML FTZBV
Key 17: ALK ESYAU
Key 18: ZKJ DRXZT
Key 19: YJI CQWYS
Key 20: XIH BPVXR
Key 21: WHG AOUWQ
Key 22: VGF ZNTVP
Key 23: UFE YMSUO
Key 24: TED XLRTN
Key 25: SDC WKQSM

'''


