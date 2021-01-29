def solution(participant, completion):
    people = {}
    for e in participant:
        if e in people:
            people[e] += 1
        else: people[e] = 1

    for e in completion:
        if e in people:
            people[e] -= 1

    for e in people:
        if people[e] == 1:
            return e

participant = ["leo","kiki","eden"]
completion = ["eden", "kiki"]

print(solution(participant, completion))

participant = ["mislav","stanko","mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

print(solution(participant, completion))
