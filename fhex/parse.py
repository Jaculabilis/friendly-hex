import math

from fhex.words import ADJECTIVE, PARTICIPLE, NOUN, PHONETIC


DEFAULT_FORMAT_DEF = {
    "A": ADJECTIVE,
    "P": PARTICIPLE,
    "N": NOUN,
    "F": PHONETIC,
}


def hex_to_friendly(hex_str, format_str):
    hex_i, fmt_i = 0, 0
    words = []
    fmt_def = DEFAULT_FORMAT_DEF
    while hex_i < len(hex_str):
        if fmt_i >= len(format_str):
            raise Exception("Format string is too short")
        fmt_code = format_str[fmt_i]

        if fmt_code not in fmt_def:
            raise Exception(f"Unrecognized format code: {fmt_code}")
        fmt_list = fmt_def[fmt_code]

        fmt_len = math.log(len(fmt_list), 16)
        if fmt_len % 1 != 0:
            raise Exception(
                f"Word list for {fmt_code} must be a power of 16" +
                " (length: {len(fmt_list)})")
        fmt_len = int(fmt_len)

        if hex_i + fmt_len > len(hex_str):
            raise Exception(f"Not enough hex characters for format code {fmt_code}")

        hex_part = hex_str[hex_i:hex_i + fmt_len]
        fmt_list_i = int(hex_part, 16)
        word = fmt_list[fmt_list_i]
        words.append(word)

        hex_i += fmt_len
        fmt_i += 1

    if fmt_i != len(format_str):
        raise Exception("Format string is too long")

    return words

