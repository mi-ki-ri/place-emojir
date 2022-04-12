import re

def convert(arg: str):
    pattern_before = r'(.)'
    pattern_after = r'\1 '
    s = arg
    s = re.sub(pattern_before, pattern_after, s)

    pattern_before = r'\s(ゃ|ゅ|ょ|ぁ|ぃ|ぅ|ぇ|ぉ|ャ|ュ|ョ|ァ|ィ|ゥ|ェ|ォ)'
    pattern_after = r'\1'
    s = re.sub(pattern_before, pattern_after, s)

    pattern_before = r'\s{2,}'
    pattern_after = r' '
    s = re.sub(pattern_before, pattern_after, s)

    return s