import unicodedata
import collections


class Cesar:
    def encode(string, key):
        new_message = []
        uKey = key % 26
        nkey = key % 10
        newText = Cesar.normalize(string)
        for c in newText:
            if (c.isalpha()):
                a = chr(((ord(c.upper()) + uKey)))
                if (not a.isupper()):
                    a = chr(ord(a) - 26 * (abs(uKey) // uKey))
                if (c.islower()):
                    a = a.lower()
                new_message.append(a)
            elif (c.isnumeric()):
                a = int(c) + nkey
                new_message.append(str(a))
            else:
                new_message.append(c)
        return ''.join(new_message)
    def decode(string, key):
        return Cesar.encode(string, -key)
    def analyse(string):
        statement = string.replace(" ", "")
        statement = statement.replace(".", "")
        count = collections.Counter(statement)
        key = ord(count.most_common(1)[0][0].upper()) - ord('E')
        return key

    def normalize(text):
        normalized = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore')
        return (normalized.decode("utf-8"))
    def histogram(string):
        hist = collections.Counter(list(filter(lambda x:x.isalpha() and ord(x)>=ord('a') and  ord(x)<=ord('z'),sorted(list(string.lower())))))
        # Histogram
        return {'char': list([i for i in hist]),
                           'frequency': [hist[i]/len(string) for i in hist]}

    def french_histo(s):
        return [['a','b',  'c',  'd',  'e',  'f',  'g',  'h',  'i',  'j',  'k',  'l',  'm',  'n',  'o',  'p',  'q',  'r',  's',  't',  'u',  'v',  'x',  'y',  'z'],[0.06341812970261555,  0.004657828735220351,  0.031171623074166967,  0.04192045861698316,  0.10426370476531709,  0.011286277319957004,  0.00895736295234683,  0.007524184879971337,  0.061268362594052314,  0.004657828735220351,  0.00017914725904693657,  0.0474740236474382,  0.01934790397706915,  0.059656037262629885,  0.042816194912217845,  0.023468290935148694,  0.005911859548548907,  0.0553565030455034,  0.05481906126836259,  0.04854890720171982,  0.03636689358652813,  0.007165890361877463,  0.002866356144750985,  0.003045503403797922,  0.0008957362952346829]]


