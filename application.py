from flask import Flask,render_template,request

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('ind.html')

@application.route('/',methods=['POST'])
def getvalue():
       name = request.form['name']
       from details import abc
       from sampu import punt
       a=abc(name)[0]
       b=abc(name)[1]
       c=abc(name)[2]
       d=abc(name)[3]
       e=abc(name)[4]
       f=punt(name)
       return render_template('index2.html',a=a,b=b,c=c,d=d,e=e,f=f)   

if __name__ == '__main__':
    #application.run(host ='0.0.0.0', port = 5001,debug=True) 
    application.run()



