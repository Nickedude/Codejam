import sys

def mural_cost(cj_cost: int, jc_cost: int, mural_state: str) -> int:
    cost = 0

    if len(mural_state) == 1:
        return cost

    pred = None
    mural_state = [c for c in mural_state]

    for i in range(len(mural_state) - 1):
        curr, succ = mural_state[i], mural_state[i+1]
        part = curr + succ

        if part == "JC":
            cost += jc_cost
        elif part == "CJ":
            cost += cj_cost
        elif part == "??":
            if pred is None:
                if cj_cost <= jc_cost:
                    mural_state[i] = "C"
                else:
                    mural_state[i] = "J"

            else:
                mural_state[i] = pred

        elif curr == "?":
            if pred is None:
                pass

            elif pred == succ:
                mural_state[i] = pred

            elif pred == "C" and succ == "J":
                mural_state[i] = "J"
                cost += cj_cost

            elif pred == "J" and succ == "C":
                mural_state[i] = "C"
                cost += jc_cost

        elif succ == "?":
            pass

        pred = curr

    return cost


if __name__ == "__main__":
    n_test_cases = int(sys.stdin.readline())

    for i in range(n_test_cases):
        inputs = sys.stdin.readline()
        inputs = inputs.split(" ")
        cj_cost, jc_cost = int(inputs[0]), int(inputs[1])

        print(f"Case #{i}: {mural_cost(cj_cost, jc_cost, inputs[2])}")
