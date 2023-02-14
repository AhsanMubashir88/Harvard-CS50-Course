import sys

votes = []
candidates = []
e_candidates =[]

def main():

    global votes
    global candidates

    if len(sys.argv) < 2:
        print("No candidates entered")
        sys.exit()

    elif len(sys.argv) > 10:
        print("Candidates exceed max. limit of 9")
        sys.exit()

    else:
        candidates_count = len(sys.argv) - 1
        
      
        for i in range(candidates_count):
            candidates.append({"name": sys.argv[i + 1], "votes": 0})


    voters = int(input("No of voters: "))
    winning_count = int(voters/2)+1

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


    #Running Runoff Election Algorithm
    while True:
        if is_winner(winning_count):
            break
        elif is_tie():
            break
        else:
            eliminate()
        

def is_winner(winning_count):
    #updating candidates votes by counting rank 1 votes
    global votes
    global candidates
    global e_candidates

    for vote in votes:
        for candidate in candidates:
            if vote[0] == candidate['name']:
                candidate['votes']+=1

    #checking and declaring a winner if there is one using rank 1 votes
    for candidate in candidates:
        if candidate['votes'] >= winning_count:
            print(f"Winner: {candidate['name']}")
            return True

    return False
            
      
def is_tie():
    #checking if it is a tie.
    global votes
    global candidates
    global e_candidates

    e_candidates =[]

    candidates.sort(key=lambda c: c['votes'], reverse=True)
    e_candidates.append(candidates[-1])

    for c in candidates[:-1]:
        if c['votes'] == candidates[-1]['votes']:
            e_candidates.append(c)
    
    if len(e_candidates) == len(candidates):
        print("TIE")
        for c in candidates:
            print(c['name'])
        return True
   
    return False

def eliminate():
    #eliminating the candidate with min number of votes
    global votes
    global candidates
    global e_candidates

    for e in e_candidates:
        for c in candidates:
            if e['name'] == c['name']:
                candidates.remove(c)

    for e in e_candidates:
        for vote in votes:
            if vote[0] == e['name']:
                vote.pop(0)


    for c in candidates:
        c['votes'] = 0

    return True


def check_vote(name):

    global candidates

    for candidate in candidates:
        if name == candidate["name"]:
            return True
    return False



if __name__ == "__main__":
    main()
