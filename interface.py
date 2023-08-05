from utils import SleepDisorder
from flask import Flask,jsonify,render_template,request
import config


app = Flask(__name__)

############################################  Home API  ##############################################################

@app.route('/')
def sleep_disorder_model():

    print('Welcome To The Homepage of Sleep Disorder model ')

    return render_template('home.html')
    # return 'TESTING OF SLEEP DISORDER MODEL' 

############################################  Model API  ##############################################################

@app.route('/predicted_disorder',methods= ['POST','GET'])

def get_sleep_disorder():
    if request.method == 'POST':
        print('We are in POST method')

        data = request.form
        Gender = data['Gender']
        Age = eval(data['Age'])
        Sleep_Duration = eval(data['Sleep_Duration'])
        Quality_of_Sleep = eval(data['Quality_of_Sleep'])
        Physical_Activity_Level = eval(data['Physical_Activity_Level'])
        Stress_Level = eval(data['Stress_Level'])
        BMI_Category = data['BMI_Category']
        Blood_Pressure = data['Blood_Pressure']
        Heart_Rate = eval(data['Heart_Rate'])
        Daily_Steps = eval(data['Daily_Steps'])
        Occupation  = data['Occupation']

        print(f'Gender={Gender},Age={Age},Sleep_Duration={Sleep_Duration},Quality_of_Sleep={Quality_of_Sleep},Physical_Activity_Level={Physical_Activity_Level},Stress_Level={Stress_Level},BMI_Category={BMI_Category},Blood_Pressure={Blood_Pressure},Heart_Rate={Heart_Rate},Daily_Steps={Daily_Steps},Occupation={Occupation}')
        
        sleep_dis = SleepDisorder(Gender,Age,Sleep_Duration,Quality_of_Sleep,Physical_Activity_Level,Stress_Level,BMI_Category,Blood_Pressure,Heart_Rate,Daily_Steps,Occupation)
        disorder = sleep_dis.get_predicted_disorder()
        if disorder[0] == 0:
            return jsonify({'Result':f'This person is Healthy'})
        elif disorder[0]==1:
            return jsonify({'Result':f'This person is Suffering from Apnea'})
        else:
            return jsonify({'Result':f'This person is Suffering from Insomnia'})



    else:
        print('We are in GET method')
        data1 = request.args
        Gender = data1.get('Gender')
        Age = data1.get('Age')
        Sleep_Duration = data1.get('Sleep_Duration')
        Quality_of_Sleep = data1.get('Quality_of_Sleep')
        Physical_Activity_Level = data1.get('Physical_Activity_Level')
        Stress_Level = data1.get('Stress_Level')
        BMI_Category = data1.get('BMI_Category')
        Blood_Pressure = data1.get('Blood_Pressure')
        Heart_Rate = data1.get('Heart_Rate')
        Daily_Steps = data1.get('Daily_Steps')
        Occupation  = data1.get('Occupation')


        print(f'Gender={Gender},Age={Age},Sleep_Duration={Sleep_Duration},Quality_of_Sleep={Quality_of_Sleep},Physical_Activity_Level={Physical_Activity_Level},Stress_Level={Stress_Level},BMI_Category={BMI_Category},Blood_Pressure={Blood_Pressure},Heart_Rate={Heart_Rate},Daily_Steps={Daily_Steps},Occupation={Occupation}')
        
        sleep_dis1 = SleepDisorder(Gender,Age,Sleep_Duration,Quality_of_Sleep,Physical_Activity_Level,Stress_Level,BMI_Category,Blood_Pressure,Heart_Rate,Daily_Steps,Occupation)
        disorder1 = sleep_dis1.get_predicted_disorder()
        if disorder1[0] == 0:
            return jsonify({'Result':f'This person is Healthy'})
        elif disorder1[0]==1:
            return jsonify({'Result':f'This person is Suffering from Apnea'})
        else:
            return jsonify({'Result':f'This person is Suffering from Insomnia'})


if __name__=='__main__':
    app.run(host='0.0.0.0',port=config.PORT_NUMBER,debug=False)

     
            
         