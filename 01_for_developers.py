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
import sounddevice as sd
import zipfile
import os


# In[3]:


#here create a dict to save important data for further use
#save data:
#1. method option
#2. reference source
#3. test source
#4. anchor
saved_data =  { "method":["default"], 
                "reference_source":["default"], 
                "test_source":["default"],
                "anchor":["default"],
                "hidden_reference_source":["default"] }

#list 1 is the source name
list1 = []

#list 2 is the name of sound files
list2 = []

#combine data for download
name = {}

#--------------------------------------------------------------------------------------------------------#
# 1. page #
#--------------------------------------------------------------------------------------------------------#
#Introduction page

#Introduction
div_title111 = Div(text="""Introduction""", 
                         style={'font-size': '300%', 'color': 'black',
                                'text-align': 'center','width':'100%','font-weight':'bold'})

#introduction in details
div_title112 = Div(text="""This is the a setup browser to let you generate some sound test method.
<br /> <br /> 
At the first step, you should upload up to 16 sound sources. 
<br />
Then you need to choose which test method you want to choose. 
<br />
The 3rd page you need to select your reference source/ test sources/ anchors.
<br /> <br /> 
After click the submit button, you are able to download some important data for further sound testing.
<br /> <br /> 
The file "name.json" is a JSON data which includes each sound source with corresponding sound file name. 
<br />
The file "saved_data.json"  describe some information such as which source is reference source and so on. 
<br />
Those data can be automatically insert in the next step for user testing.
""",style={'font-size': '100%', 'color': 'black','font-weight':'bold','text-align': 'center','width':'100%'})

#button and button bar
button1 = Button(label="start", button_type="success",height_policy = 'auto')
button_bar = RadioButtonGroup(labels=["1.set up sound","2.choose your method", "3.further option"], 
                              active=0, button_type="primary", width=680)


#the rest of setup is underneath

#--------------------------------------------------------------------------------------------------------#
# page 2 :button bar with jumping operation between #
#--------------------------------------------------------------------------------------------------------#

#the page 2 
def page():   
    #clear the former page
    curdoc().clear()
    
    #step 1
    if button_bar.active == 0: #what to do if step 1 is clicked
        list1.clear()
        #the first line "Please add all your sound sources here:"
        div_title1 = Div(text="""Please add all your sound sources here""", 
                         style={'font-size': '300%', 'color': 'black',
                                'text-align': 'center','width':'100%','font-weight':'bold'})

        #select file
        #restrict file type to only sound file
        #allow maximal 16 sound sources
        file_input1 = FileInput(accept=".wav") 
        file_input2 = FileInput(accept=".wav")
        file_input3 = FileInput(accept=".wav")
        file_input4 = FileInput(accept=".wav")
        file_input5 = FileInput(accept=".wav")
        file_input6 = FileInput(accept=".wav")
        file_input7 = FileInput(accept=".wav")
        file_input8 = FileInput(accept=".wav")
        file_input9 = FileInput(accept=".wav")
        file_input10 = FileInput(accept=".wav")
        file_input11 = FileInput(accept=".wav")
        file_input12 = FileInput(accept=".wav")
        file_input13 = FileInput(accept=".wav")
        file_input14 = FileInput(accept=".wav")
        file_input15 = FileInput(accept=".wav")
        file_input16 = FileInput(accept=".wav")
        
        #function for source 1, once one field is uploaded with a file, list1 will get a name corrsponding to the sound source
        #such as "source 1", "source 2" and so on...
        def upload_data1(attr, old, new):
            list1.append("source 1")
        
        #this function is to get the file name and add to list 2
        #list 1 and list 2 are happening at the same time, so same index from these 2 list are having the correct order
        #such as: "source 1","01mps.wav"
        def upload_data11(attr, old, new):
            list2.append(file_input1.filename)
        
        #function for source 2
        def upload_data2(attr, old, new):
            list1.append("source 2")
            
        def upload_data22(attr, old, new):
            list2.append(file_input2.filename)
        
        #function for source 3
        def upload_data3(attr, old, new):
            list1.append("source 3")
        
        def upload_data33(attr, old, new):
            list2.append(file_input3.filename)
        
        #function for source 4
        def upload_data4(attr, old, new):
            list1.append("source 4")
            
        def upload_data44(attr, old, new):
            list2.append(file_input4.filename)    
        
        #function for source 5
        def upload_data5(attr, old, new):
            list1.append("source 5")
        
        def upload_data55(attr, old, new):
            list2.append(file_input5.filename)
        
        #function for source 6
        def upload_data6(attr, old, new):
            list1.append("source 6")
        
        def upload_data66(attr, old, new):
            list2.append(file_input6.filename)
        
        #function for source 7
        def upload_data7(attr, old, new):
            list1.append("source 7")
            
        def upload_data77(attr, old, new):
            list2.append(file_input7.filename)    
        
        #function for source 8
        def upload_data8(attr, old, new):
            list1.append("source 8")
            
        def upload_data88(attr, old, new):
            list2.append(file_input8.filename)  
            
        #function for source 9
        def upload_data9(attr, old, new):
            list1.append("source 9")
            
        def upload_data99(attr, old, new):
            list2.append(file_input9.filename) 
        
        #function for source 10
        def upload_data10(attr, old, new):
            list1.append("source 10")
            
        def upload_data1010(attr, old, new):
            list2.append(file_input10.filename) 
        
        #function for source 11
        def upload_data111(attr, old, new):
            list1.append("source 11")
            
        def upload_data1111(attr, old, new):
            list2.append(file_input11.filename) 
        
        #function for source 12
        def upload_data12(attr, old, new):
            list1.append("source 12")
            
        def upload_data1212(attr, old, new):
            list2.append(file_input12.filename) 
        
        #function for source 13
        def upload_data13(attr, old, new):
            list1.append("source 13")
            
        def upload_data1313(attr, old, new):
            list2.append(file_input13.filename) 
        
        #function for source 14
        def upload_data14(attr, old, new):
            list1.append("source 14")
            
        def upload_data1414(attr, old, new):
            list2.append(file_input14.filename) 
            
        #function for source 15
        def upload_data15(attr, old, new):
            list1.append("source 15")
            
        def upload_data1515(attr, old, new):
            list2.append(file_input15.filename) 
            
        #function for source 16
        def upload_data16(attr, old, new):
            list1.append("source 16")
            
        def upload_data1616(attr, old, new):
            list2.append(file_input16.filename) 
        
        #JS callback once the FileInput is clicked
        #have to be seperated, because one is value, another one is to get the filename
        #or I just realized actually I can just use second one?
        file_input1.on_change('value',upload_data1)
        file_input1.on_change('filename',upload_data11)
        
        file_input2.on_change('value',upload_data2)
        file_input2.on_change('filename',upload_data22)
        
        file_input3.on_change('value',upload_data3)
        file_input3.on_change('filename',upload_data33)
        
        file_input4.on_change('value',upload_data4)
        file_input4.on_change('filename',upload_data44)
        
        file_input5.on_change('value',upload_data5)
        file_input5.on_change('filename',upload_data55)
        
        file_input6.on_change('value',upload_data6)
        file_input6.on_change('filename',upload_data66)
        
        file_input7.on_change('value',upload_data7)
        file_input7.on_change('filename',upload_data77)
        
        file_input8.on_change('value',upload_data8)
        file_input8.on_change('filename',upload_data88)
        
        file_input9.on_change('value',upload_data9)
        file_input9.on_change('filename',upload_data99)
        
        file_input10.on_change('value',upload_data10)
        file_input10.on_change('filename',upload_data1010)
        
        file_input11.on_change('value',upload_data111)
        file_input11.on_change('filename',upload_data1111)
        
        file_input12.on_change('value',upload_data12)
        file_input12.on_change('filename',upload_data1212)
        
        file_input13.on_change('value',upload_data13)
        file_input13.on_change('filename',upload_data1313)
        
        file_input14.on_change('value',upload_data14)
        file_input14.on_change('filename',upload_data1414)
        
        file_input15.on_change('value',upload_data15)
        file_input15.on_change('filename',upload_data1515)
        
        file_input16.on_change('value',upload_data16)
        file_input16.on_change('filename',upload_data1616)

        #description for each file
        div_title11 = Div(text="""test source 1:""",style={'font-size': '100%', 'color': 'black','text-align': 'center',
                       'font-weight':'bold'})
        div_title12 = Div(text="""test source 2:""",style={'font-size': '100%', 'color': 'black','text-align': 'center',
                       'font-weight':'bold'})
        div_title13 = Div(text="""test source 3:""",style={'font-size': '100%', 'color': 'black','text-align': 'center',
                       'font-weight':'bold'})
        div_title14 = Div(text="""test source 4:""",style={'font-size': '100%', 'color': 'black','text-align': 'center',
                       'font-weight':'bold'})
        div_title15 = Div(text="""test source 5:""",style={'font-size': '100%', 'color': 'black','text-align': 'center',
                       'font-weight':'bold'})
        div_title16 = Div(text="""test source 6:""",style={'font-size': '100%', 'color': 'black','text-align': 'center',
                       'font-weight':'bold'})
        div_title17 = Div(text="""test source 7:""",style={'font-size': '100%', 'color': 'black','text-align': 'center',
                        'font-weight':'bold'})
        div_title18 = Div(text="""test source 8:""",style={'font-size': '100%', 'color': 'black','text-align': 'center',
                        'font-weight':'bold'})
        div_title19 = Div(text="""test source 9:""",style={'font-size': '100%', 'color': 'black','text-align': 'center',
                       'font-weight':'bold'})
        div_title110 = Div(text="""test source 10:""",style={'font-size': '100%', 'color': 'black','text-align': 'center',
                       'font-weight':'bold'})
        div_title111 = Div(text="""test source 11:""",style={'font-size': '100%', 'color': 'black','text-align': 'center',
                       'font-weight':'bold'})
        div_title112 = Div(text="""test source 12:""",style={'font-size': '100%', 'color': 'black','text-align': 'center',
                       'font-weight':'bold'})
        div_title113 = Div(text="""test source 13:""",style={'font-size': '100%', 'color': 'black','text-align': 'center',
                       'font-weight':'bold'})
        div_title114 = Div(text="""test source 14:""",style={'font-size': '100%', 'color': 'black','text-align': 'center',
                       'font-weight':'bold'})
        div_title115 = Div(text="""test source 15:""",style={'font-size': '100%', 'color': 'black','text-align': 'center',
                        'font-weight':'bold'})
        div_title116 = Div(text="""test source 16:""",style={'font-size': '100%', 'color': 'black','text-align': 'center',
                        'font-weight':'bold'})

        #layout, combine 16 input together
        col1 = column(div_title11,file_input1,div_title13,file_input3,div_title15,file_input5,div_title17,file_input7,div_title19,file_input9,div_title111,file_input11,div_title113,file_input13,div_title115,file_input15)
        col2 = column(div_title12,file_input2,div_title14,file_input4,div_title16,file_input6,div_title18,file_input8,div_title110,file_input10,div_title112,file_input12,div_title114,file_input14,div_title116,file_input16)
        row1 = row(col1,col2,sizing_mode="stretch_width")
        
        layout = column(div_title1,row1,button_bar,sizing_mode="stretch_width")
        curdoc().add_root(layout)
        
    #step 2
    if button_bar.active == 1: #what to do if step 2 is clicked
    
        #a single selection widget
        div_title2 = Div(text="""Which test method do you want to use to design the test?""", height=50, style={'font-size': '200%', 'color': 'black','text-align': 'center','width':'100%','font-weight':'bold'})
        
        #select
        select = Select(title="Option:", value= saved_data["method"][0], options=["Please select one method", "ACR", "MUSHRA Test", "option 3", "option 4"])
        
        #save selected value and save it to saved_data JSON file
        #the method is saved, so after step 3, if the user wants to come back to step 2, the method should stay there
        #no worry to select again!
        def callback_method(attr, old, new):
            saved_data["method"][0] = select.value
        
        #js callback to select
        select.on_change('value', callback_method)
    
        layout = column(div_title2,select,button_bar,sizing_mode="stretch_width")
        curdoc().add_root(layout)
        
    #step 3
    if button_bar.active == 2: #what to do if step 3 is clicked
    
        #a multi-select widget to present multiple available options in a compact horizontal layout
        #NOTE: option is list1, that's why at the beginning I created the first list
        #which means, only the uploaded sound source will be selected here!
        
        #for reference source
        div_title31 = Div(text="""1. Which test source number you want to be the reference source?""",height=50, style={'font-size': '200%', 'color': 'black','text-align': 'center','width':'100%','font-weight':'bold'})
        multi_choice1 = MultiChoice(value=[], options=list1)
        
        def callback_ref(attr, old, new):
            saved_data["reference_source"][0] = multi_choice1.value
            
        multi_choice1.on_change('value', callback_ref)
    
        #for test source
        #once one is selected, it won't show again
        div_title32 = Div(text="""2. Which test source number you want to be the test source?""",height=50, style={'font-size': '200%', 'color': 'black','text-align': 'center','width':'100%','font-weight':'bold'})
        multi_choice2 = MultiChoice(value=[], options=list1)
        
        def callback_test(attr, old, new):
            saved_data["test_source"][0] = multi_choice2.value
            
        multi_choice2.on_change('value', callback_test)
        
        #for anchor
        div_title33 = Div(text="""3. Which test source number you want to be the anchor?""",height=50, style={'font-size': '200%', 'color': 'black','text-align': 'center','width':'100%','font-weight':'bold'})
        multi_choice3 = MultiChoice(value=[], options=list1)
        
        def callback_anchor(attr, old, new):
            saved_data["anchor"][0] = multi_choice3.value
            
        multi_choice3.on_change('value', callback_anchor)
        
        #for hidden reference source
        div_title44 = Div(text="""4. Which test source number you want to be the hidden reference source?""",height=50, style={'font-size': '200%', 'color': 'black','text-align': 'center','width':'100%','font-weight':'bold'})
        multi_choice4 = MultiChoice(value=[], options=list1)
        
        def callback_hidden(attr, old, new):
            saved_data["hidden_reference_source"][0] = multi_choice4.value
            
        multi_choice4.on_change('value', callback_hidden)
        
        #here button3 is "submit",so in page4() we can generate the stuff we need
        button3 = Button(label="submit", button_type="success")
        button3.on_event(ButtonClick, page4)
    
        layout = column(div_title31,multi_choice1,div_title32,multi_choice2,div_title33,multi_choice3,div_title44,multi_choice4,button3,button_bar,sizing_mode="stretch_width")
        curdoc().add_root(layout)
        
#downloading page       
def page4():
    curdoc().clear()
    
    #congratulations
    div_title41 = Div(text="""your test is generated! <br /> Please click the button to get your data for testing""", 
                          height=100,
                          style={'font-size': '200%', 'color': 'black','text-align': 'center','width':'100%'})
    
    #here this button should be clicked, in order to let person download
    button4 = Button(label="download data", button_type="warning")
    button4.on_event(ButtonClick,savedata)
    
    layout = column(div_title41,button4,sizing_mode="stretch_width")
    curdoc().add_root(layout)
    
#here make a defination, for downloading!
def savedata():
    for key in list1:
        for value in list2:
            name[key] = value
            list2.remove(value)
            break
    #the name dict to add key as list1, value as list2
    #this is for further use, so when users are testing, they can match the file name with sound sources easily!
    
    #save all important data in JSON
    tf = open("saved_data.json", "w")
    json.dump(saved_data,tf)
    tf.close()
    
    #save source name and file name in JSON
    tf1 = open("name.json", "w")
    json.dump(name,tf1)
    tf1.close()   
    
#--------------------------------------------------------------------------------------------------------#   
#this page is just for testing! Just to show you the value we got!
#if you don't want to download, change button4.on_event(ButtonClick,savedata) to button4.on_event(ButtonClick,showresult)
#--------------------------------------------------------------------------------------------------------#
def showresult():
    curdoc().clear()
    str1 = json.dumps(saved_data)
    str2 = str(list1)
    div_title115 = Div(text=str1 + "uploaded source:" + str2, 
                         style={'font-size': '300%', 'color': 'black',
                                'text-align': 'center','width':'100%','font-weight':'bold'})
    layout = column(div_title115,sizing_mode="stretch_width")
    curdoc().add_root(layout)

#--------------------------------------------------------------------------------------------------------#
# the rest of 1. page 
#--------------------------------------------------------------------------------------------------------#
#the layout for the first page

button1.on_event(ButtonClick, page)   
button_bar.on_change('active', lambda attr, old, new: page())

layout = column(div_title111,div_title112,button1,sizing_mode="stretch_width")
curdoc().add_root(layout)
curdoc().title = "welcome"


# In[2]:


#Here are some code for testiong/learning while coding, trash but might be useful for future


#callback = CustomJS(code="alert('you are done')")
#button.js_on_event("button_click", CustomJS(code="show(div_title)"))
#button.js_on_click(callback)



#def callback():
    #curdoc().clear() #clear the document
    #show(column(div_title,row1,button,button,sizing_mode="stretch_width"))

#button.on_event(ButtonClick, callback())

#def callback():
    #curdoc().clear() #clear the document
    #show(column(div_title,row1,button,button,sizing_mode="stretch_width"))

#gui_step = RadioButtonGroup(labels=["1.set up sound","choose your method", "further option", "download link"], 
                            #active=1, button_type="primary", width=680)

#gui_step.on_change('active', lambda attr, old, new: steps())

#def steps():
    #curdoc().clear() #clear the document
    #if gui_step.active == 0: #what to do if page 0 is clicked
        #show(column(div_title,row1,gui_step,sizing_mode="stretch_width"))
    
#show(column(div_title,row1,gui_step,sizing_mode="stretch_width"))

#button1 = Button(label="next step", button_type="success",height_policy = 'auto')


# In[ ]:




