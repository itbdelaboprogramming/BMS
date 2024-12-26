import pickle
from scipy.interpolate import interp1d


# Load the data
with open('soc_data.pkl', 'rb') as file:
    x, y = pickle.load(file)


# Create an interpolation function for SOC based on OCV
soc_from_TV = interp1d(x, y, kind='cubic', fill_value="extrapolate")
TV_from_soc = interp1d(y, x, kind='cubic', fill_value="extrapolate")

def estimate_initial_soc_from_ocv(voltage):
    # Predict SoC using interpolation function
    estimated_soc_percentage = soc_from_TV(voltage*1000)/100
    return estimated_soc_percentage   # Convert to fraction

def estimate_initial_ocv_from_soc(voltage):
    # Predict SoC using interpolation function
    estimated_soc_percentage = soc_from_TV(voltage*1000)/100
    return estimated_soc_percentage   # Convert to fraction

def DCRfromSoC(SoC):
    # From datasheet graph that has been plotted
    return (5500/(SoC+15)**4+ 18000/(SoC+15)**3-500/(SoC+15)**2+6.3/(SoC+15)+1.1)/1000


