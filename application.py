#!/usr/bin/env python
import flask
from random import randrange
from kalman import Kalman
import time

app = flask.Flask(__name__)
input_data_range = 5000*2

k_f = Kalman()
k_f.setAngle( 0.0 )


@app.route('/')
def index():
    input_          = []
    setpoint        = []
    output_ra       = []
    output_ma       = []
    output_kf       = []
    output_cf       = []
    
    # Raw data
    for i in range(input_data_range):
        input_.append( round(randrange(-4,4)/float(randrange(2,5)),1) )   
        setpoint.append( 0.0 )
    

    # Moving Average Algorithm
    m = input_[0]
    output_ma.append(m)
    for j in range(1,len(input_)):
         m = ( m * j + input_[j])/float(j+1)
         output_ma.append(m)

    # Simple Rolling Average
    for j in range(0,len(input_)-5):
        temp_ = []
        for wx in range(0,5):
            temp_.append(input_[j + wx])
        output_ra.append( sum(temp_)/float(5))

    
    # Kalman filter
    for j in range(1,len(input_)):
        output_kf.append( k_f.getAngle( input_[j], 0.01, 0.01 ) )

         
    return flask.render_template('index.html',
                                 Input      =input_,
                                 Setpoint   =setpoint,
                                 Output     =output_ma,
                                 Output2    =output_ra,
                                 Output3    =output_kf)


if __name__ == '__main__':
    app.debug=True
    app.run()
    
