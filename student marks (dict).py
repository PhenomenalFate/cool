print("student and score")

stud_score={}
data = [("Alice", 85), ("Bob", 75), ("Alice", 92),
        ("Bob", 80), ("Charlie", 90), ("Alice", 78)]

for name , score in data:
    if name not in stud_score:
        stud_score[name]=[]
    stud_score[name].append(score)


print(stud_score)


avg_score={}
for name , score in stud_score.items():
    avg_score[name]=sum(score)/len(score)



top_stud=""
highest_avg=0
for name,avg in avg_score.items():
    if avg>highest_avg:
        highest_avg=avg
        top_stud=name

min_stud=""
lowest_avg=100
for name,avg in avg_score.items():
    if avg<lowest_avg:
        lowest_avg=avg
        min_stud= name

print(avg_score)
print("top student are" ,top_stud, "with avg of" ,highest_avg)
print("min student are" ,min_stud, "with avg of" ,lowest_avg)

