#frequency analysis of a given plain text
from collections import Counter

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def is_english(s):
    if (is_ascii(s)):
        text = ''.join(c for c in s if c.isalpha())
        if (text == ''):
            return False
        else:
            lext = text.lower()
            chk = 'etaoin'
            cnt = Counter(lext).most_common(3)
            cntn = [cnt[0][0],cnt[1][0],cnt[2][0]]
            cntjn = ''.join(cntn)
            print(cnt)
            for x in cntjn:
                if x not in chk:
                    return False
                else:
                    return True

        
