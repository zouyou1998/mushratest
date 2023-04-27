# Browser Based Audio Test Programs including Drag & Drop MUSHRA Test
This programme focuses on the design of a browser-based, developer-oriented audio testing system. The framework of the programme will allow for extensions through future development to implement further audio testing methods. Through this system, developers will be able to select different types of acoustic test methods and customise their experiments. Once the basic parameters have been set, the developer can share the designed program with the test users. When the test user has completed the appropriate test, the results are sent to the developer for analysis. As part of the programme, a drag & drop MUSHRA test method is implemented and used as an example test method to test the usability of the platform.

The programme is implemented in Python. The main function in the modified MUSHRA test is implemented using the extended Bokeh package to realise the drag and drop function and to play the sound sources. Bokeh is a Python library for creating interactive visualizations for modern web browsers. The first part of the developer design phase is also fully implemented using the Bokeh package to build the browser-based platform.

## Program structure
The overall structure of the software is divided into three parts, each consisting of three .py files, each of which is relatively independent but interlinked. After running the three programs step by step, the developer can obtain the results of the Drag \& Drop MUSHRA test. The overall framework can be seen in the figure below.

![image](https://github.com/zouyou1998/mushratest/blob/main/structure.jpg)

The first part is called 01_for_developers.py and this is the programme that is aimed at the developers. This program allows the developer to upload the sound source files, to select the test method and to set up the parameters of the test. The developer will need to upload all of the necessary files in this step, which will also be the input to this program. The second part is a test section that has been designed for the users. The third section is a simple analysis program designed for developers. When the developer is given a set of result files by the tester, the program will crawl these files and generate a simple graph of the results based on the parameters provided in the first part.

This software uses the latest version of the Bokeh package (3.1.0), which the developer must download in order to run the software. The code does not specify any output or connection methods. It is a simple script that creates and updates objects. The Bokeh command line tools allow you to specify output options after the data has been processed. To run the application on the Bokeh server, use the following command: For the first part, to start the software, enter the following command in a terminal:

    bokeh serve —-show 01_for_developers.py

For the second part, to start the software, enter the following command in a terminal:

    bokeh serve —-show 02_for_users.py
    
This will give you the JSON serialised version of the application.

## The guide to use the program
### First part
The first part (01_for_developers.py) uses the bokeh package as a framework and does not use any extensions other than the json package. It is initialised with a ditc called saved_data which contains method, reference source, test source, anchor and hidden reference source information. all keys have a value of "default". The values in these keys will be replaced later as files are uploaded and parameters are set. There are also two lists: list1 and list2, which each store the source name and the corresponding name of the sound source file, respectively, and are merged into a dict called name at the end. 

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


Those are some of the initial preparations. Now, when the developer runs the programme, the first thing that appears is a welcome page, which introduces some of the programme's features and gives some tips. When the developer has finished reading this, click on the start button and they will be taken to the official setup page.

![image](https://github.com/zouyou1998/pictures/blob/main/introduction.jpeg)

The setup page is divided into three sections: 'set up sound', 'choose your method' and 'more options'. They are linked by the Bokeh's built-in button bar. The user can move between these three buttons at will. The first page the user enters is the 'set up sound' page. Here the user can upload the sound source file they wish to test. Meanwhile, Bokeh's FileInput widget is used to upload the file. It is important to note that the purpose of uploading here is to extract the name of the file, not to upload the audio file. This is because the audio files do not need to be played or processed in the first part. Up to 16 sound sources can be uploaded here. Of course, the code can be extended to include more sound sources depending on the test method, but 16 files is usually sufficient for most audio test methods. The developer does not have to select all 16 audio files, and any unselected uploads can be ignored. The developer doesn't even have to upload the files in order (although this is usually recommended to make the final result more aesthetically pleasing), as the function will only be triggered if the files are uploaded.

Users are restricted to uploading .wav files only. When a file is uploaded to one of the 16 upload entry points, two functions are triggered simultaneously. One function will store the number of the upload location in list1 (e.g. if the user uploads an audio file to test source 1, list1 will store a string called "source 1", which is the source name as mentioned above), while at the same time another function will grab the name of the file and store it in list2. As the two functions are triggered synchronously, the same index in list1 and list2 corresponds to the matching source name and sound source file name. 

![image](https://github.com/zouyou1998/pictures/blob/main/setup.jpeg)

Once the developer has uploaded all the necessary files, they can click on the second section 'Choose your method' to proceed to the next step. This second section allows developers to select the test method they wish to use, which is made possible by Bokeh's built-in single selection widget. It is important to note that this option is stored as the value of the 'method' key of saved_data immediately after the developer has made their initial selection. If the developer wishes to revisit the second section when setting up the third section, the option previously selected by the developer will remain as the default option when the user returns to the second step. Further test method options can be added to this module in future development. The page in programme looks like in figure.

![image](https://github.com/zouyou1998/pictures/blob/main/WechatIMG244.jpeg)

Now the developer has confirmed the test method, they can click on the third section to continue setting the parameters for the experiment. The third section allows the user to set the parameters to complete the setup process. In the case of the MUSHRA test, the parameters to be set are reference source, test source, anchor and hidden reference source, and depending on the type of parameter, Bokeh's built-in multi-select widget is used to display The first section updates list1 (the list containing the source name) with the added sound source name whenever an audio file is uploaded. Every parameter option here uses list1, so the selection is dynamic (depending on how many audio files are uploaded in the first section). For example, if a user uploads 8 files in the first section in test sound source 1 to 8, the parameters available here are source 1 to source 8. This avoids redundant data on the one hand and too much data on the other, so that the developer does not forget which parameter he wants to set. In this section the developer is asked the four questions. For each option selected by the developer, the corresponding data is stored in saved_data. For example, in the first question the developer needs to select the reference source, if the user selects source 1 as the reference source, the string "source 1" will be stored in saved_data Once all questions have been answered and all test sources have been assigned the appropriate roles, the developer can click the green "submit" button. Once clicked, the data cannot be changed and the developer is taken to the final page. An example of the parameter setup page can be found in figure.

![image](https://github.com/zouyou1998/pictures/blob/main/para.jpeg)

In the final page, "please click the button to get your data for testing" directs the developer to download the important data for the test. "Download data" converts the dict saved\_data to JSON and saves it as saved_data.json. In addition, since list1 contains the source name and list2 contains the corresponding source file name (the same index corresponds to the matching source name and audio file name), the values in the same index are matched to create a new dic (the value in list is the key and the value in list2 is the value) and converted to JSON and saved as name.json. The downloading page can be found in figure.

![image](https://github.com/zouyou1998/pictures/blob/main/download.jpg)

The entire first part of the programme starts with the input audio file and ends with the output of two JSON files. These two files along with sound source files will be used in the second and third parts of the programme. Figures beloq show an example of the first part of the output. When a developer enters eight files with names 01test.wav to 08test.wav in test source 1 to test source 8, selects MUSHRA test and sets the corresponding parameters, the two files saved_data.json and name.json are output.

![image](https://github.com/zouyou1998/pictures/blob/main/1682423601178.jpg)
![image](https://github.com/zouyou1998/pictures/blob/main/1682423597981.jpg)

### Second part
The second part (02_for_users.py) is for user testing. As in the first part, the Bokeh package is used as the general framework and the drag & drop functionality is implemented using Bokeh. The wavfile package is used to import the audio files, the soundfile package is used to extract the audio content and the json package is used to process the data from the first part and export the results from the second part. The overall framework of the second part is shown in the figure below. The top part enables the drag & drop function and the bottom part plays the sound function. When the user has finished the test, click on "save the data" to save and download the test results.

![image](https://github.com/zouyou1998/pictures/blob/main/1682425766062.jpg)

The top half of the graph is created using Bokeh, with the x-axis scaled between -10 and 105 to leave some space on the far left for all the sound sources to initialise, and the rightmost part for the reference source, which will only be half or not at all displayed if the scale is exactly 0-100. The y-axis has no real meaning in the test, so it is hidden here. However, the y-axis data is important as it will be used for the different sound sources at the beginning.

The user places the two JSON files obtained in the first part (name.json and saved_data.json) and all the audio files in the same root directory. At this point, the programme grabs the contents of the two JSON files and saves them in the programme. It then pours in all the .wav files that are in the same root directory. Use the soundfile package to extract the audio content and frequency information. If the filename matches the filename in name.json, the data in the corresponding .wav file and the key (source name) in name.json are reconstructed into a new dict called new\_data (source name as key, data in .wav file as value). This is why the filenames are extracted in the first part. This way the user can simply put all the files in the same root directory (there may also be other .wav files in the same root directory, as even these audio files that are not part of the test content cannot be matched to the source name on import and are not really used). 

This new_data is now split into two separate lists: source_list and audio_data, the former storing all the source names (source 1, source 2 ...) and the latter storing the audio files corresponding to each index of the source_list. The latter stores the contents of the audio file corresponding to each index of source_list. If the value matches one of the items in the source_list, it is extracted from the source_list and the data from the corresponding index in the audio_data is extracted and stored in the ref_name and ref_data lists. ref_name lists, which store the name and data of the reference source respectively. The reason for extracting the data of the reference source separately is that the reference source does not take part in the scoring, it always scores 100 and is fixed in the middle of 100 on the way. We now have four lists, each of which serves the following purposes, these four lists will be very important for subsequent setups.

1. source_list: the name of the source other than the reference source
2. audio_dat: the sound data of the sources other than the reference source (each index corresponds to source_list)
3. ref_name: name of the reference source
4. ref_data: sound data of the reference source

Now move on to setting up the chart data. Set up the test for up to 15 sound sources (excluding the reference source), corresponding to the 16 audio files uploaded in the first section. And assign a maximum of 16 colours. If the user needs to test fewer than 8 sound sources (excluding the reference source), all the sound sources will be placed in a row on the far left. If the user needs to test more than or equal to 8 sound sources (excluding the reference source), then all the sound sources are arranged in two columns on the far left, for aesthetic reasons and because if we assume that up to 15 sound sources are arranged in one column, the area of each sound source will be very small and not conducive to dragging. This is because if we assume that up to 15 sources are arranged in a column, the area of each source will be very small and not conducive to dragging and dropping. By extracting the first part of the json file you can see how many sound sources there are, and depending on the number of sound sources, each sound source is evenly spaced between -10 and 0 on the x-axis. This is why the y-axis data is needed, even though it has no effect on the results. y-axis data can help to initialise the layout of the sound sources. Figures below are examples of a single column and a double column arrangement. During initialisation, each source is given a random colour to make it easier to distinguish between them.

![image](https://github.com/zouyou1998/pictures/blob/main/single1.jpeg)
![image](https://github.com/zouyou1998/pictures/blob/main/double.jpeg)

Now pack all the data (x-axis position, y-axis position, source colour for each sound source) into the ColumnDataSource format and start creating the graphs. Design all the sound source modules as boxes, with each sound source in a different coloured square and a dot in the middle that can be positioned for more accurate user evaluation. The icons were designed to resemble the two colours of a football pitch, so that the user could compare them. reference sources were fixed individually in the range of 100 on the x-axis. drag & drop was implemented using Bokeh's built-in PointDrawTool. Another axis at the top of the image is marked with five ratings, similar to those in the ACR, for user evaluation.

In the lower half of the program is the music playback section. According to the original design, the music should be played by clicking on the box in the image above. However, in Bokeh, the PointDrawTool cannot be used in conjunction with the Taptool (which implements the click function). If the developer wanted to implement both functions in the image above, the user would have to switch between the two tools frequently, which would increase the user's workload considerably and make the user experience unfriendly. This is why the lower part of the programme has a music playback section. The principle of this section is similar to the one above, where a new diagram is created and all the sound sources are evenly distributed in the diagram according to their number, with the reference source still on the far right.

![image](https://github.com/zouyou1998/pictures/blob/main/play.jpg)

To implement the click-to-play functionality, a custom Javascript callback is designed where all data, including audio data, is passed to the CustomJS as parameters, and when the user clicks anywhere on the chart, the program detects whether the clicked position is within the box of a sound source. If it is, and no music is currently playing, then the music that matches that box is played. If the users want to stop playback, click on any part of the chart to stop it. The design of this section requires knowledge of Javascript.

The user drags and drops on the top chart. The music plays in the lower chart. In addition, Bokeh's built-in DataTable is used to record the scores. The x-axis coordinates of all the boxes in the above diagram are recorded in real time in the DataTable, and the data in the DataTable changes in real time as the user drags and drops each time. A simple example is shown in figure below:

![image](https://github.com/zouyou1998/pictures/blob/main/table.jpg)

However, this DataTable is not visible to the user (it can be displayed to the user, but this is not very meaningful). If the user wants to visualise their score, there is a section in the code that uses Tooltips to achieve this. With this function, when the user hovers the mouse over the box in the image above, the corresponding score appears next to it. This feature can be used as appropriate.

When the user has finished scoring, they click 'save the data' and the data should be stored in the DataTable mentioned above. Again, CustomJS is used to convert the DataTable to JSON format. It is worth noting that as the x-axis ranges from -10 to 105, if the box stays outside of 0-100 due to user error, data with an x-axis less than 0 will automatically be converted to 0 and data with an x-axis greater than 100 will automatically be converted to 100 during the conversion.The final JSON file is downloaded via url and saved as result.json.Note that the file does not contain information about the reference source, as it is always 100 points, this will be added and analysed in the third part. 

![image](https://github.com/zouyou1998/pictures/blob/main/live.jpg)
![image](https://github.com/zouyou1998/pictures/blob/main/result.jpg)


### Third part
The third part is for the developer's analysis. Once the developer has collected a large number of result.json results, the developer places all the result.json files and the saved_data.json files in the same directory as 03_for_test_result.py. When the programme is running, it first inserts the reference source and its corresponding score (100 points) and then matches each source name and combines it with the data in saved_data using the panda package to produce a visual table. The figure below shows a mean value table of the results of three tests.

The mean value calculation is only an example of the procedure. Developers are free to extend this section to implement other functions according to their individual needs.

![image](https://github.com/zouyou1998/pictures/blob/main/final.jpg)
