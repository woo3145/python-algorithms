
# 두 문자열 간의 공통 부분 수열 중 가장 긴 것을 찾는 알고리즘
# 시간복잡도 - O(mn)
def lcs(string1, string2):
    len1 = len(string1)
    len2 = len(string2)

    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if string1[i - 1] == string2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # LCS를 역으로 추적하여 출력
    lcs_length = dp[len1][len2]
    lcs_sequence = [""] * (lcs_length)
    i = len1
    j = len2
    while i > 0 and j > 0:
        if string1[i - 1] == string2[j - 1]:
            lcs_sequence[lcs_length - 1] = string1[i - 1]
            i -= 1
            j -= 1
            lcs_length -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs_sequence)


string1 = "AGGTAB"
string2 = "GXTXAYB"
print("Longest Common Subsequence:", lcs(string1, string2))
