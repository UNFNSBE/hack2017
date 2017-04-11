from data import DataGrabber
from flask import Flask, request
from flask_cors import CORS, cross_origin
from pytrends.request import TrendReq
import time

app = Flask(__name__)
CORS(app)

usAbrv = { 'Alabama': 'AL','Alaska': 'AK','Arizona': 'AZ','Arkansas': 'AR',
'California': 'CA', 'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE',
'Florida': 'FL','Georgia': 'GA','Hawaii': 'HI','Idaho': 'ID','Illinois': 'IL',
'Indiana': 'IN','Iowa': 'IA','Kansas': 'KS','Kentucky': 'KY','Louisiana': 'LA',
'Maine': 'ME','Maryland': 'MD','Massachusetts': 'MA','Michigan': 'MI',
'Minnesota': 'MN','Mississippi': 'MS','Missouri': 'MO','Montana': 'MT',
'Nebraska': 'NE','Nevada': 'NV','New Hampshire': 'NH','New Jersey': 'NJ',
'New Mexico': 'NM','New York': 'NY','North Carolina': 'NC','North Dakota': 'ND',
'Ohio': 'OH','Oklahoma': 'OK','Oregon': 'OR','Pennsylvania': 'PA','Rhode Island': 'RI','South Carolina': 'SC','South Dakota': 'SD','Tennessee': 'TN','Texas': 'TX',
'Utah': 'UT','Vermont': 'VT','Virginia': 'VA','Washington': 'WA','West Virginia': 'WV','Wisconsin': 'WI','Wyoming': 'WY'}

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/getTopic/<topic>')
def getData(topic):
    # region, topic 1, topic 2 url grab, 
    start = request.args.get('start', '')
    end = request.args.get('end', '')
    dat = getArray(topic,start,end)
    return str(dat)

@app.route('/getByDate/<topic>')
def getStates(topic):
    dateVal = request.args.get('date', '')
    print dateVal
    raw = DataGrabber().getByDate(topic,dateVal.strip()+" "+dateVal.strip())
    clean = convertToArr(raw,topic)
    ans = []
    for key in clean.keys():
        ans.append([key,clean[key]])
    print ans
    return str(ans)
    
def convertToArr(pan,topic):
    val = pan.to_dict()[topic]
#    print val.keys()
#    print len(usAbrv)
    for key in usAbrv.keys():
	if(val.has_key(key)):
            val[usAbrv[key]] = val.pop(key)
#    print val
    return val

def getArray(topic,start,end):
    states = open('states','r')
    data = []
    for i in states:
	state = ("US-"+i).strip()
        timeSpan = str(start)+" "+str(end)
        data.append(DataGrabber().getState(state,topic,timeSpan))
#        time.sleep(.1)
    return data

if __name__ == "__main__":
    app.run(host='138.197.98.147')
