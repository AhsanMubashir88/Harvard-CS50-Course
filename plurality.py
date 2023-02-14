import sys


def main():

    if (len(sys.argv)<2):

        print("No candidates entered")
        sys.exit()

    elif (len(sys.argv)>10):

        print("Candidates exceed max. limit of 9")
        sys.exit()

    else:

        candidates=[]
        canididate_count = len(sys.argv)-1

        for i in range(canididate_count):
            candidates.append({'name':sys.argv[i+1],'votes':0})

    voters = int(input("No of voters: "))

    if (voters>100 or voters<1):
        print("Voter Range: 1-100")
        sys.exit()
    
    vote_list = []
    
    while(voters>0):
        vote = input("Vote: ")
        if is_valid(vote,candidates):
            vote_list.append(vote)
        else:
            print("Invalid vote")
        voters-=1


    #Upodating candidates list with votes casted
    for vote in vote_list:
        for candidate in candidates:
            if vote == candidate['name']:
                candidate['votes']+=1
    
    print()
    for candidate in sorted(candidates, key=lambda s: s['votes'], reverse=True):
        print(f"{candidate['name']} got {candidate['votes']} votes ")

    candidates.sort(key=lambda s: s['votes'], reverse=True)

    print()

    winner = candidates[0]

    print(f"Winner: {winner['name']}")

    for candidate in candidates:

        if (candidate['name'] != winner['name'] and candidate['votes'] == winner['votes']):
            print(f"Also Winner: {candidate['name']}")


def is_valid(vote,candidates):
    for candidate in candidates:
        if vote == candidate['name']:
            return True
    
    return False

      
if __name__ == "__main__":
    main()
