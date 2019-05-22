def cipher(shift_register):
 x_register = shift_register[0:19]
 y_register = shift_register[19:41]
 z_register = shift_register[41:64]

 x_majority_value = x_register[8]
 y_majority_value = y_register[10]
 z_majority_value = z_register[10]

 ak = [x_majority_value, y_majority_value, z_majority_value]
 majority = 1 if ak.count('1') > ak.count('0') else 0

 new_x = (((int(x_register[13]) ^ int(x_register[16])) ^ int(x_register[17])) ^ int(x_register[18]))
 new_x_register = str(new_x) + x_register[0:18]

 new_y = int(y_register[20]) ^ int(y_register[21])
 new_y_register = str(new_y) + y_register[0:21]

 new_z = (((int(z_register[7]) ^ int(z_register[20])) ^ int(z_register[21])) ^ int(z_register[22]))
 new_z_register = str(new_z) + z_register[0:22]

 if ((int(x_majority_value) == int(majority)) and (int(z_majority_value) == int(majority))):
    x_register = new_x_register
    z_register = new_z_register

 if (int(x_majority_value) == int(majority)) and (int(y_majority_value) == int(majority)):
    x_register = new_x_register
    y_register = new_y_register

 if (int(y_majority_value) == int(majority)) and (int(z_majority_value) == int(majority)):
    y_register = new_y_register
    z_register = new_z_register

 if (int(y_majority_value) == int(majority)) and (int(z_majority_value) == int(majority)) and (int(x_majority_value) == int(majority)):
    y_register = new_y_register
    z_register = new_z_register
    x_register = new_x_register

 new_key = x_register + y_register + z_register
 return new_key

def key(shift_reg):
    key_stream = cipher(shift_reg)
    x_register = key_stream[0:19]
    y_register = key_stream[19:41]
    z_register = key_stream[41:64]
    new_bit_of_keystream = int(x_register[18]) ^ int(y_register[21]) ^ int(z_register[22])
    return new_bit_of_keystream

a = []
shift_reg = "1010101000101010101110011001110110011000111100001110000011110001"
a.append(shift_reg)
for x in range(20):
    print(key(a[x]))
    a.append(cipher(a[x]))
