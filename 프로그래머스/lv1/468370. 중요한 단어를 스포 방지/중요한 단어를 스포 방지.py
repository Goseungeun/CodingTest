def get_is_spoiler(spoiler_ranges, start_idx, end_idx):
    for start, end in spoiler_ranges:
        if start_idx <= end and end_idx >= start:
            return True

    return False

def solution(message, spoiler_ranges):
    answer = 0

    words = {}  # key: (start_idx, end_idx, is_spoiler), value: word

    w_start_idx = 0

    for i in range(len(message)):
        if message[i] == ' ' or i == len(message) - 1:
            if i == len(message) - 1:
                w_end_idx = i
            else:
                w_end_idx = i - 1

            is_spoiler = get_is_spoiler(spoiler_ranges, w_start_idx, w_end_idx)

            word = message[w_start_idx:w_end_idx + 1]
            words[(w_start_idx, w_end_idx, is_spoiler)] = word

            w_start_idx = i + 1

    not_spoiler_words = [
        word for (start, end, is_spoiler), word in words.items()
        if not is_spoiler
    ]

    import_words = [
        word for (start, end, is_spoiler), word in words.items()
        if is_spoiler and word not in not_spoiler_words
    ]
    
    import_words = list(set(import_words))
    answer = len(import_words)

    return answer


