"""
@Author: Arshitha Basavaraj
@Modified date: 2024-11-11
Problem statement: https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
"""


def counting_valleys(step_ct, path):
    elevation = 0  # starting at sea level
    valleys = 0
    for step in path:
        if step == "D":
            elevation -= 1
        elif step == "U":
            elevation += 1

        if step == "U" and elevation == 0:
            valleys += 1

    return valleys


if __name__ == "__main__":
    path = "UDDDUDUU"
    step_ct = len(path)
    result = counting_valleys(step_ct, path)

    print(result)
