import numpy as np 
import pandas as pd

def main():
    params = [0, 5, 500e-6, 5e-9, 5e-9, 0.5, 50e3, 60e3, 0.5e3, 7]
    low = float(params[0])
    high = float(params[1])
    delay = float(params[2])
    rise = float(params[3])
    fall = float(params[4])
    duty = float(params[5])
    fstart = float(params[6])
    fstop = float(params[7])
    fstep = float(params[8])
    num_pulses = int(params[9])
   
    pwl = []
    pwl.extend((0.0, 0.0))

    curr_time = float(delay)
    period = 1/float(fstart)
    on_time = duty * period
    # seven pulses 
    freq_sweep = np.arange(fstart, fstop, fstep)
    for freq in freq_sweep:
        period = 1/float(freq)
        on_time = duty * period
        for i in range(num_pulses):
            pwl.extend((curr_time, low))
            curr_time += rise
            pwl.extend((curr_time, high))
            curr_time += on_time
            pwl.extend((curr_time, high))
            curr_time += fall
            pwl.extend((curr_time, low))
            curr_time += (1-duty)*period
        
    csv_data = ','.join(['{:.7e}'.format(x) for x in pwl])
    with open('pwl.txt', 'w') as f:
        f.write(csv_data)

    time = pwl[::2]
    volts = pwl[1::2]
    df = pd.DataFrame(list(zip(time, volts)), columns=['Time', 'Volts'])
    print(df)
    df.to_excel("pwl.xlsx")

if __name__ == "__main__":
    main()
