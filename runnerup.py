"""Task 3: Runner-up Score | Soumen Kumar Dutta | URN: 2481248"""
n = int(input().strip())
scores = list(map(int, input().split()))
# A set removes duplicates; sorting puts the runner-up at index -2.
distinct_scores = sorted(set(scores))
print(distinct_scores[-2])
