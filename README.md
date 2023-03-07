# Schedule start stream with OBS-Studio > 28

| :warning: WARNING          |
|:---------------------------|
| Notice this code work only with the latest version of OBS Studio > 28.0   |

 ## How to use 
 
 You need only to download the artifact from the latest pipeline 
 
 1. Edit `.env` (replace value from your configuration in OBS Studio `Tools`-> `Websocket server settings`, you need server Port, server password  (to see the current value, press to *Show Connect Info*))
 2. Edit `.env` again to configure your BEGIN date and your END date 
 3. Run the tool 
    ```shell
    main.exe
    ````

## How to compile this tools

1. you need to have python on your pc
2. ```pip install -r requirements.txt```
3. ```./main.py```
