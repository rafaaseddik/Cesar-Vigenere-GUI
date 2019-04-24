import unicodedata


class Vigenere:
    def normalize(text):
        normalized = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore')
        return (normalized.decode("utf-8"))
    def encode(string, key):
        M = Vigenere.normalize(string)
        new_message = []
        ukey = key.upper()
        i, j = 0, 0
        while (i < len(M)):
            j %= len(key)
            if (not M[i].isalpha()):
                new_message.append(M[i])
                i += 1
                continue
            new = chr((ord(M[i].upper()) - 2 * ord('A') + ord(ukey[j])) % 26 + ord('A'))
            if (M[i].islower()):
                new = new.lower()
            new_message.append(new)
            j += 1
            i += 1

        return ''.join(new_message)
    def decode(string, key):
        new_message = []
        ukey = key.upper()
        i, j = 0, 0
        while (i < len(string)):
            j %= len(key)
            if (not string[i].isalpha()):
                new_message.append(string[i])
                i += 1
                continue
            new = chr((ord(string[i].upper()) - 2 * ord('A') - ord(ukey[j])) % 26 + ord('A'))
            if (string[i].islower()):
                new = new.lower()
            new_message.append(new)
            j += 1
            i += 1

        return ''.join(new_message)
    def analyse(message):
        cleaned = []
        for char in message:
            if char.isalnum():
                cleaned.append(char)

        cleaned = "".join(cleaned)

        key_len = Vigenere.vig_key_length(cleaned)

        key = ""
        for i in range(key_len):
            occ = [0 for i in range(26)]
            letters = cleaned[i:len(cleaned):key_len]
            for letter in letters:
                occ[ord(letter.upper()) - 65] += 1
            c = occ.index(max(occ))
            key += chr(((c - ord('E') + 65) % 26) + 65)
        return key

    def PGCD(a, b):
        if b == 0:
            return a
        else:
            r = a % b
            return Vigenere.PGCD(b, r)

    def vig_key_length(message, word_length=3, max_key=0):
        if word_length > len(message) / 2:
            return max_key

        words = {}

        for k in range(0, len(message) - word_length + 1):
            word = message[k:k + word_length].upper()
            if word in words:
                words[word].append(k)
            else:
                words[word] = [k]

        distance = []
        for w in words:
            occ = words[w]
            if len(occ) > 1:
                for i in range(0, len(occ) - 1):
                    distance.append(occ[i + 1] - occ[i])
        if (len(distance) < 1):
            return max(max_key, 0)
        elif len(distance) == 1:
            return max(max_key, distance[0])
        else:
            key_len = Vigenere.PGCD(distance[0], distance[1])
            for k in range(len(distance)):
                key_len = Vigenere.PGCD(key_len, distance[k])
            if key_len < 3:
                return Vigenere.vig_key_length(message, word_length + 1, key_len)
            else:
                return key_len





