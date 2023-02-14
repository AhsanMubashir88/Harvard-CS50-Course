import sys
from itertools import combinations

votes = []
candidates = []
pairs = []
margins = []


def main():

    global votes
    global candidates
    global pairs

    if len(sys.argv) < 2:
        print("No candidates entered")
        sys.exit()

    elif len(sys.argv) > 10:
        print("Candidates exceed max. limit of 9")
        sys.exit()

    else:
        candidates_count = len(sys.argv) - 1

        for i in range(candidates_count):
            candidates.append(sys.argv[i + 1])

    voters = int(input("No of voters: "))

    if voters > 100 or voters < 1:
        print("Voter Range: 1 - 100")
        sys.exit()

    for i in range(voters):
        ind_vote = []
        for j in range(candidates_count):
            name = input(f"Rank {j+1}: ")
            if check_vote(name):
                ind_vote.append(name)
            else:
                print("Invalid vote")
                sys.exit()
        votes.append(ind_vote)
        print()

    # Running the Tideman/Ranked Pairs Algorithm
    # Making pairs of candidates and stoting them in a list
    pairs = combinations(candidates, 2)
    record_margins()
    sort_pairs()
    get_winner()


def check_vote(name):

    global candidates

    for candidate in candidates:
        if name == candidate:
            return True
    return False


def record_margins():

    global pairs
    global votes
    global margins

    for pair in pairs:

        pair_0 = 0
        pair_1 = 0

        for vote in votes:
            for c in vote:
                if c not in pair:
                    pass
                else:
                    if c == pair[0]:
                        pair_0 += 1
                        break
                    elif c == pair[1]:
                        pair_1 += 1
                        break
                    else:
                        pass

        if pair_0 > pair_1:
            winner = pair[0]
            loser = pair[1]
            margin = pair_0
        elif pair_0 < pair_1:
            winner = pair[1]
            loser = pair[0]
            margin = pair_1
        else:
            winner = "tie"
            loser = "tie"
            margin = 0

        if winner == "tie":
            pass
        else:
            margins.append(
                {"pair": pair, "winner": winner, "loser": loser, "margin": margin}
            )


def sort_pairs():

    global margins
    margins.sort(key=lambda m: m["margin"], reverse=True)


def get_winner():

    global margins
    global candidates

    loser = []

    candidate_count = len(candidates)

    if margins:
        pass
    else:
        print("TIE")
        return 0

    for m in margins:
        loser.append(m["loser"])

    loser_count = 0
    winner = ""
    for c in candidates:
        for l in loser:
            if c in loser:
                loser_count += 1
            else:
                winner = c
                pass

    if winner:
        print(f"Winner: {winner}")
        return 0
    else:
        margins.pop()
        get_winner()


if __name__ == "__main__":
    main()
