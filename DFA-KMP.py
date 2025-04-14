import sys
txt = input("사용할 텍스트를 입력하세요 : ").strip()
pattern = input("찾을 패턴을 입력하세요 : ").strip()

# txt = "aba"
# pattern = "ababac"

pattern_set = set(list(pattern))
alpha = list(pattern_set)

DFA = [[0] * len(pattern) for _ in range(len(alpha) + 1)]

X = len(alpha)


def make_dfa():
    first_char = pattern[0]
    alpha_idx = alpha.index(first_char)
    DFA[alpha_idx][0] = 1

    for i in range(1, len(pattern)):
        previous_x = DFA[X][i - 1]
        for j in range(len(alpha)):
            DFA[j][i] = DFA[j][previous_x]
        cur_idx = alpha.index(pattern[i])
        DFA[X][i] = DFA[cur_idx][previous_x]
        DFA[cur_idx][i] = i + 1


def search():
    cur_state = 0
    for c in txt:
        if c not in pattern_set:
            cur_state = 0
            continue
        cur_state = DFA[alpha.index(c)][cur_state]
        if cur_state == len(pattern):
            print("매칭되는 문자열을 확인했습니다 !")
            sys.exit()

    print("매칭되는 문자열이 존재하지 않습니다")


make_dfa()
search()
