list1=[128,252,182,115,177,211,142,252,189,248,130,93,154,0,68,90,131,255,204,170,239,167,18,51,233,43,0,26,210,72,95,120,227,7,195,126,207,254,115,53,141,217,0,11,118,192,110,0,0,170,248,73,103,78,10,174,208,233,156,187,185,65,228,0,137,128,228,71,159,10,111,10,29,96,71,238,141,86,91,82,0,214,37,114,7,0,238,114,133,0,140,0,38,36,144,108,164,141,63,2,69,73,15,65,68,0,249,13,0,64,111,220,48,0,55,255,13,12,68,41,66,120,188,0,73,27,173,72,189,80,0,148,0,64,26,123,0,32,44,237,0,252,36,19,52,0,78,227,98,88,1,185,1,128,182,177,155,44,132,162,68,0,1,239,175,248,68,91,84,18,223,223,111,83,26,188,241,12,0,197,57,89,116,96,223,96,161,45,133,127,125,63,80,129,69,59,241,157,0,105,57,23,30,241,62,229,128,91,39,152,125,146,216,91,5,217,16,48,159,4,198,23,108,178,199,14,6,175,51,154,227,45,56,140,221,0,230,228,99,239,132,198,133,72,243,93,3,86,94,246,156,153,123,1,204,200,233,143,127,64,164,203,36,24,2,169,121,122,159,40,4,25,64,0,241,9,94,220,254,221,122,8,22,227,140,221,248,250,141,66,78,126,190,73,248,105,5,14,26,19,119,223,103,165,69,177,68,61,195,239,115,199,126,61,41,242,175,85,211,11,5,250,93,79,194,78,245,223,255,189,0,128,9,150,178,0,112,247,210,21,36,0,2,252,144,59,101,164,185,94,232,59,150,255,187,1,198,171,182,228,147,73,149,47,92,133,147,254,173,242,39,254,223,214,196,135,248,34,146,206,63,127,127,22,191,92,88,69,23,142,167,237,248,23,215,148,166,59,243,248,173,210,169,254,209,157,174,192,32,228,41,192,245,47,207,120,139,28,224,249,29,55,221,109,226,21,129,75,41,113,192,147,45,144,55,228,126,250,127,197,184,155,251,19,220,11,241,171,229,213,79,135,93,49,94,144,38,250,121,113,58,114,77,111,157,146,242,175,236,185,60,67,173,103,233,234,60,248,27,242,115,223,207,218,203,115,47,252,241,152,24,165,115,126,48,76,104,126,42,225,226,211,57,252,239,21,195,205,107,255,219,132,148,81,171,53,79,91,27,174,235,124,213,71,221,243,212,38,224,124,54,77,248,252,88,163,44,191,109,63,189,231,251,189,242,141,246,249,15,0,2,230,7,244,161,31,42,182,219,15,221,164,252,207,53,95,99,60,190,232,78,255,197,16,169,252,100,164,19,158,32,189,126,140,145,158,116,245,68,94,149,111,252,74,135,189,83,74,71,218,99,220,208,87,24,228,11,111,245,1,0,98,131,46,22,94,71,244,22,147,21,83,155,252,243,90,24,59,73,247,223,127,242,183,251,124,28,245,222,199,248,122,204,230,79,219,147,11,225,202,239,24,132,55,89,221,143,151,137,63,150,79,211,8,16,4,60,63,99,65,0,2]
# This code is just to print the hex values
for i in range(42):
    for j in range(16):
        pass
        # print("{:02}".format(hex(list1[i*16+j])[2:]),end=' ')
    # print()

# This is the png header ihdr initialisation
final_header=[0x89,0x50,0x4E,0x47,0x0D,0x0A,0x1A,0x0A,0x00,0x00,0x00,0x0D,0x49,0x48,0x44,0x52]

# The code below will list all the possible key values

for i in range(0,16):
    value=0
    for j in range(0,42):
        if (final_header[i]==list1[j*16+i]):
            if (j<10):
                if (value==0):
                    print(j,end="")
                elif (value==1):
                    print(' ',j," 1st alternate value")
                else:
                    print(' ',j," 2nd alternate value")
            elif(value==0):
                if (value==0):
                    print(42-j,end="")
                elif (value==1):
                    print(' ',42-j," 1st alternate value")
                else:
                    print(' ',42-j," 2nd alternate value")
            value+=1
            # if (value==2):
            #     print("j\n1st alternate value")
            # if (value==3):
            #     print("jn2nd alternate value")
