# EJR wrote this code to test zoom_game output
import numpy as np
test_add = [True, .5, 2]
alex_sl=test_add+[True, False, True, False, False, False, False, False, True, True, True, True]
alex_sl = np.reshape(alex_sl,[3,5])
print(alex_sl)

crop_level = 2
my_msg = 'We are cropped at level:'
crop_level = str(crop_level)
print(my_msg+crop_level)