class studentperfomance:
    def __init__(self,name,subject_scores):
        self.name=name
        self.subject_scores=subject_scores
    def add_sub(self,subject,score):
        self.subject_scores[subject] = score 
        return self.subject_scores
    def avg(self):
        avg=sum(self.subject_scores.value())/len(self.subject_scores.value())  
        return avg
sub1=studentperfomance(name="sasi",subject_scores={"maths":50,"eng":16})
print(sub1.avg())
    