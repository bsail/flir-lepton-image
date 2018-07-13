#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 21:22:06 2018

@author: dmitry
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 15:50:31 2018

@author: dmitry
"""
data=(open('new.ir','rb').read())
image = []
telemetry=[]
for x in range (0,59):
    for y in range (0,79):
        high = data[x*164 + 4 + y*2]
        low = data[x*164 + 5 + y*2]
        image.append((high&(~(3<<14)))+low)
from PIL import Image
im=Image.new("RGB",(80,60),0)
k=0
for j in range (0,59):
    for i in range (0,79):
        im.putpixel((i,j),(image[k],image[k],image[k]))
        k+=1
#im.show()
im.save("1.bmp")
a=0
for x in range (60,63):
    for y in range (0,179):
        telemetry.append(data[x*164 + 4 + y])
        a+=1
print(telemetry)
#trev=0
trev=telemetry[48]+(telemetry[49]<<8)
#print(trev)
tcount=telemetry[26]+(telemetry[27]<<8)+(telemetry[28]<<16)+(telemetry[29]<<24)
#print(tcount)
#print((telemetry[26*2+1]+(telemetry[26*2]<<8))/100)
def valueator(start,end,group,tele):
    if (group=="A"):
        par = 0
        rra=(end-start+1)
        val = []
        for j in range(0,rra):
            val.append(tele[2*(start+j)]*256 + tele[2*(start+j)+1])

        print(val)
        for (j,item) in enumerate(val):
            par = (par*256*256) + val[j]
        return val[0]
    elif (group=="B"):
        #print("B!!")
        par = 0
        rra=(end-start+1)
        val = []
        for j in range(0,rra):
            val.append(tele[2*(start+79+j)]*256 + tele[2*(start+79+j)+1])

        print(val)
        for (j,item) in enumerate(val):
            par = (par*256*256) + val[j]
        return val[0]
import json
#from pprint import pprint

#json_file='a.json' 
json_input='telemetry_lepton.json'
json_output='telemetry_output_lepton.json'

json_data=open(json_input)
template = json.load(json_data)
json_data.close()
tele_types=["Tel_rev",
            "Time_count",
            "Status_bits",
            "Module_num",
            "Soft_rev",
            "Frame_count",
            "Frame_mean",
            "FPA_Temp",
            "FPA_Temp_2",
            "House_Temp",
            "House_Temp_2",
            "FPA_Temp_at_last",
            "Time_count_at_last",
            "House_Temp_at_last",
            "AGC_ROI",
            "AGC_Clip_high",
            "AGC_Clip_low",
            "Video_output",
            "Log2_of_FFC",
            "Emessivity",
            "Back_Temp",
            "Atmo_Trans",
            "Atmo_Temp",
            "Window_Trans",
            "Window_Ref",
            "Window_Temp",
            "Window_Ref_Temp"]
#print(template["Lepton"][tele_types[3]]["value"])
#print(template["Lepton"]["Tel_rev"]["start"])
#print(template["Lepton"]["Tel_rev"]["end"])
#print(template["Lepton"]["Time_count"]["end"])
#print(template["Lepton"]["Soft_rev"]["end"]+template["Lepton"]["Time_count"]["end"])
for j in range (0,len(tele_types)):
     template["Lepton"][tele_types[j]]["value"]=valueator(template["Lepton"][tele_types[j]]["start"],template["Lepton"][tele_types[j]]["end"],template["Lepton"][tele_types[j]]["group"],telemetry)
     #print(j)
#template["Lepton"][tele_types[0]]["value"]=valueator(template["Lepton"][tele_types[0]]["start"],template["Lepton"][tele_types[0]]["end"],telemetry)
json_final=open(json_output,"w")
json.dump(template,json_final)
json_final.close()
