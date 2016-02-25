#!/usr/bin/env python
import flask
from random import randrange


app = flask.Flask(__name__)
input_data_range = 800

@app.route('/')
def index():
    input_ = []
    setpoint = []
    output = []
    ma_output = []
    
    # Raw data
    for i in range(input_data_range):
        if( i%3 == 0):
            input_.append( 0.0 )
        elif( i%5 == 0):
            input_.append( 0.0 )
        else:
            if( True ):
                input_.append( round(randrange(-2,2)/float(randrange(2,5)),1) )
                
        setpoint.append( 0.0 )
    

    # Moving Average Algorithm
    m = input_[0]
    ma_output.append(m)
    for j in range(1,len(input_)):
         m = ( m * j + input_[j])/float(j+1)
         ma_output.append(m)


    # Simple Rolling Avg
    for j in range(0,len(input_)-5):
        temp_ = []
        for wx in range(0,5):
            temp_.append(input_[j + wx])
        output.append( sum(temp_)/float(5))
        
         
    return flask.render_template('index.html', Input=input_, Setpoint=setpoint, Output=output, Output2=ma_output)


if __name__ == '__main__':
    app.debug=True
    app.run()
    
