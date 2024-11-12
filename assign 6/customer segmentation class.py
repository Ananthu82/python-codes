class customersegmentation:
    def __init__(self,customers,spending_scores):
        self.customers=customers
        self.spending_scores=spending_scores
    def __str__(self):
        return(f"customersegmentation {self.customers},{self.spending_scores}")
    def customer_seg(self):
     seg=[]
        for i in self.spending_scores.value():
            if i<100:
              seg.append("low")
            elif 50<i<100:
               seg.append("medium")
            else:
               seg.append("high")
            return seg
customers1=customersegmentation(customer={"sasi","shock","hari"},spending_scores={100,102,45})
print.(customer)
     
       
            


            

