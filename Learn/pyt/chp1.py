from numpy import sort
 
class Medical:
    def __init__(self):
        self.diagnosis = {
        123:['dolo','Covid',{'Do you have chest pain?':'Contact your Doctor immediately'}], 
        1:['crocin','Viral',{'Do you have high fever (>100C)?':'If fever does not subside, admit yourself.'}], 
        2:['claribid','Common Cold'], 
        3:['benadryl','Common Cold'],
        12:['combiflam','Flu'],
        13:['tylenol','Flu'],
        23:['benylin','Common Cold']
    }
 
    def user_data(self):
        self.user_name = input("Enter your name: ")
        self.user_age = input("Enter your age: ")
        self.user_weight = input("Enter your weight: ")
 
    def user_diagnosis (self):
        while True:
            print("\nTell your symptoms:")
            print("1. Fever\n2. Cold\n3. Cough\n4. Exit")
            self.symptoms = int(input("Enter your symptom (with a comma and without spaces): "))
            if self.symptoms == 4:
                break
            medicine_list = sorted([int(symptom) for symptom in str(self.symptoms)])
            self.symptoms = int(''.join(map(str,medicine_list)))
            try:
                print(f"For {self.user_name}: ")
                print("-"*40)
                print('Medicines suggested-> ',str(self.diagnosis[self.symptoms][0]).capitalize())
                print('You may be diagnosed with-> ',str(self.diagnosis[self.symptoms][1]).capitalize())
                print('\n')
                print(str(list(self.diagnosis[self.symptoms][2].keys())[0]).capitalize())
                print('1. Yes\n2. No')
                c = int(input())
                if(c==1):
                    print('Additional Advice: ', str(list(self.diagnosis[self.symptoms][2].values())[0]).capitalize())
                else:
                    print("Have a Good Day!!.")
            except:
                pass
 
 
if __name__ == "__main__":
    patient = Medical()
    patient.user_data()
    patient.user_diagnosis()
