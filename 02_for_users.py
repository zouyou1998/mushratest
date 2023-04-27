#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bokeh.io import show
from bokeh.models import Div,Button,FileInput,RadioButtonGroup,Select,CustomJS,MultiChoice
from bokeh.layouts import row,column,layout
from bokeh.models.callbacks import CustomJS
from bokeh.events import ButtonClick
from bokeh.plotting import curdoc, figure
import json
import soundfile as sf
#import sounddevice as sd
import numpy as np
from scipy.io import wavfile
import glob


# In[2]:


#for table test
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, DataTable, PointDrawTool, TableColumn
from bokeh.io import show, output_notebook
import pandas as pd


# In[3]:


from bokeh.plotting import figure, show, output_file
from bokeh.models import Range1d, PointDrawTool, LinearAxis

#setups
#name in the browser
output_file('image.html')

#tooltips to show the current score (not really need, will delete for final use)
TOOLTIPS = [
    ("current points", "$x"),
    ]

#set up the figure, without tooltips
p = figure(width=800, height=400, title="MUSHRA Test",tools='',toolbar_location="right")

# set a range using a Range1d
p.x_range = Range1d(-10, 105, bounds=(-10, 105)) #range should be a bit outside
p.y_range = Range1d(0, 100, bounds=(0, 100))
p.xaxis.bounds = (0, 100)
p.title.align = 'center'

#setup the blocking area, make it more stylish
p.varea(x=[-10,0],
        y1=[0,0],
        y2=[100,100], hatch_pattern = "right_diagonal_line", hatch_color = "grey", color= "white", hatch_weight = 0.1)

p.varea(x=[100,105],
        y1=[0,0],
        y2=[100,100], hatch_pattern = "right_diagonal_line", hatch_color = "grey", color= "white", hatch_weight = 0.1)


# Opening JSON file
f = open('saved_data.json')
# returns JSON object as a dictionary
important_data = json.load(f)

# Opening JSON file
g = open('name.json')
# returns JSON object as a dictionary
source_name = json.load(g)

#get reference source
reference_source = important_data["reference_source"][0]

#get the sound source name in a list (after taking reference source out)
sound = []

for key in source_name:
    if key != reference_source[0]:
        sound.append(key)

#---------------------------------------------

# Load the WAV file
# Initialize lists to store audio data, sampling frequency, and file names
audio_data = []
sampling_freq = []
file_names = []

# Loop over all WAV files in the directory
for wav_file in glob.glob('*.wav'):
    # Load the audio data and sampling frequency
    data, fs = sf.read(wav_file)
    audio_data.append(data)
    sampling_freq.append(fs)
    
    # Store the file name
    file_names.append(wav_file)

#creat a dic: key is sound file name, value is audio_data
dataset = {}
for key in file_names:
    for value in audio_data:
        dataset[key] = value
        audio_data.remove(value)
        break

#combine 2 dict, if the file name are the same, then put the key as source name, value is data name
new_data = {}

for key in source_name:
    if source_name[key] in dataset:
        new_data[key] = dataset[source_name[key]]
        

#create 2 list, seperat them
source_list = []
audio_data = []

for key, value in new_data.items():
    source_list.append(key)
    audio_data.append(value)

#get the reference source data
ref_name = []
ref_data = []
if reference_source[0] in source_list:
    index = source_list.index(reference_source[0])
    ref_name = source_list.pop(index)
    ref_data = audio_data.pop(index)
    
#print(source_list)
#print(audio_data)
#print(ref_name)
#print(ref_data)

#---------------------------------------------

#we have len(source_name) sources in total
#maximal allow 15 sources (tho easy to change)
#doesn't include reference source!
#setup all sound sources
number = len(source_name)-1
case = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"]
color = ["red","yellow","pink","orange","navy","brown","turquoise","olive","lavender","chartreuse","firebrick","lightslategray","maroon","mistyrose","olivedrab"]
order = []
position_x = []
position_y = []
color_update = []
size = []

#if number is less than 8
#one column
if number < 8:
    for i in np.arange(number):
        #case[i] = p.square([0],[100/number/2+i*100/number], color=color[i], alpha=0.5,size=50-number*2)
        position_x.append(-5)
        position_y.append(100/number/2+i*100/number)
        color_update.append(color[i])
        size.append(50-number*2)
        #order.append(case[i])
    
#if number is 8 or more than 8
#2 columns
if number >= 8:
    for i in np.arange(number):
        if i < number//2:
            #case[i] = p.square([0],[100/number/2+i*100/number], color=color[i], alpha=0.5,size=50-number*2)
            position_x.append(-7.5)
            if number%2 == 0:
                position_y.append(100/((number//2)+1)+i*100/((number//2)+1))
            else:
                position_y.append(100/((number//2)+1)+i*100/((number//2)+1))
            color_update.append(color[i])
            size.append(50-number)
            #order.append(case[i])
        if i >= number//2:
            #case[i] = p.square([0],[100/number/2+i*100/number], color=color[i], alpha=0.5,size=50-number*2)
            position_x.append(-3.5)
            if number%2 == 0:
                position_y.append(100/((number//2)+1)+(i-number//2)*100/((number//2)+1))
            else:
                position_y.append(100/((number//2)+6)+(i-number//2)*100/((number//2)+1)) #number=9 100/6
            color_update.append(color[i])
            size.append(50-number)
            #order.append(case[i])


#combine all data
source = ColumnDataSource(data=dict(x=position_x, y=position_y,color=color_update,size=size,sound=sound))
    
#add all points
r = p.square_dot(x='x', y='y', source=source, color='color', alpha=1,size="size",line_color="black",line_width=0,line_alpha=0.7)
 
#make the y axis not visible
p.yaxis.visible = False

#make it more elegant (can be changed)
p.outline_line_width = 7
p.outline_line_alpha = 0.3
p.outline_line_color = "black"
p.xgrid.band_fill_alpha = 0.1
p.xgrid.band_fill_color = "black"
p.ygrid.grid_line_color = None

#the reference picture
ref = p.image_url(url=['A.png'], x=100, y=50, w=4, h=12, anchor = "center")

#drag and drop action
#don't allow to add new (add=False)
#make it always active
tool1 = PointDrawTool(renderers=[r],add=False)
p.add_tools(tool1)
p.toolbar.active_tap = tool1

#make an extra axis to describe
p.extra_x_ranges['temp'] = Range1d(start=-10, end=105, bounds=(0, 100))
p.extra_x_ranges.visible = False
p.add_layout(LinearAxis( x_range_name='temp', axis_label='          schlecht                                                          mäßig                                                 ordentlich                                                  gut                                                    ausgezeichnet'), 'above')


#----------------------------------------------------#

#make a second graphic for sound playing
p1 = figure(width=800, height=150, title="PLAT SOUND",tools='',toolbar_location="right")
p1.title.align = 'center'
p1.x_range = Range1d(-5, 105, bounds=(-5, 105))
p1.y_range = Range1d(0, 100, bounds=(0, 100))
p1.xaxis.bounds = (0, 100)
p1.xgrid.grid_line_color = None
p1.ygrid.grid_line_color = None
p1.xaxis.visible = False
p1.yaxis.visible = False

#set the position
position_x1 = []
position_y1 = []
size1 = []

for i in np.arange(number):
    position_y1.append(50)
    position_x1.append(i*(100/(number+1)))
    size1.append(50)
    
source1 = ColumnDataSource(data=dict(x1=position_x1, y1=position_y1,color=color_update,size=size1,sound=sound))
r1 = p1.square_dot(x='x1', y='y1', source=source1, color='color', alpha=1,size="size",line_color="black",line_width=0,line_alpha=0.7)
ref1 = p1.image_url(url=['A.png'], x=100, y=50, w=4, h=40, anchor = "center")

# create the JavaScript callback
#using cb_obj. to get the position of the boxes
#if the area of the box is clicked, check if it is playing music first
#if it is playing now, stop music first
#if the area is reference source, play reference source
#make a loop to go through each boxes
#if clicked the area of an area belongs to one box
#play the music of the box

#Note: for stop playing music you can click any area to stop
#this is due to the design, otherwise 2 sounds will play at the same time

#audio_data is already excluded reference source!
#here assume sample_rate is the same overall, if not it's easy to change, following the previous step to create a sample rate list
callback1 = CustomJS(args=dict(source1=source1, ref_data=ref_data, audio_data=audio_data, 
                               sample_rate=sampling_freq), code="""  
    var xp = cb_obj.x;
    var xt = cb_obj.y;
    if (window.source && window.source.playbackState === window.source.PLAYING_STATE) {
        window.source.stop();
        window.source = null;
    }else{
    if (xp > 97.25 && xp < 102.25 && xt > 25 && xt < 75)
{
    var context = new AudioContext();
    var buffer = context.createBuffer(1, ref_data.length, sample_rate[0]);
    buffer.getChannelData(0).set(ref_data);
    window.source = context.createBufferSource();
    window.source.buffer = buffer;
    window.source.connect(context.destination);
    window.source.start(0);

}
    for (var i=0;i<source1.data.x1.length;i++)
{ 
    if (xp > source1.data.x1[i]-2.25 && xp < source1.data.x1[i]+2.25 && xt > 25 && xt < 75)
{
    var t = i+1
    var context = new AudioContext();
    var buffer = context.createBuffer(1, audio_data[i].length, sample_rate[0]);
    buffer.getChannelData(0).set(audio_data[i]);
    window.source = context.createBufferSource();
    window.source.buffer = buffer;
    window.source.connect(context.destination);
    window.source.start(0);
}
}
}
""")

# add the JS callback to the plot
p1.js_on_event('tap', callback1)

#the table to show all value, this is LIVE
#so once users dragging sth, the value will change!
columns = [TableColumn(field="color", title="color(sound source)"),
           TableColumn(field="x", title="score")]
table = DataTable(source=source, columns=columns, editable=True)


# get the data from the DataTable
# define the JavaScript callback function

#this callback means once the user click submit, the data will be downloaded
#if the x-axis value is smaller than 0, it will be set to 0 
#if the x-axis value is bigger than 100, it will be set to 100 

#it will create a downloading link, it will includes sounce name and their scores
callback2 = CustomJS(args=dict(source=source), code="""
    const data = source.data;
    const json = JSON.stringify(data);
    const jsonObject = JSON.parse(json);

    const newObject = {
      sound: jsonObject.sound,
      x: jsonObject.x,
    };


    newObject.x = newObject.x.map((value) => {
  if (value < 0) {
    return 0;
  } else if (value > 100) {
    return 100;
  } else {
    return value;
  }
});

    const newJsonString = JSON.stringify(newObject);
    const blob = new Blob([newJsonString], {type: 'application/json'});
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = 'result.json';
    link.click();
    URL.revokeObjectURL(url);
""")

#the button to save the data for downloading
button1 = Button(label="save the data", button_type="success",height_policy = 'auto')
button1.js_on_click(callback2)

#layout setting
layout = column(p,p1,button1,table,sizing_mode="stretch_width")
#show(layout)
curdoc().add_root(layout)
curdoc().title = "MUSHRA test"


# In[ ]:





# In[ ]:





# In[ ]:




