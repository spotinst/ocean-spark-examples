# Notebook for Ocean for Apache Spark

This doc explain how to run notebook connected to a Ocean Spark cluster with VSCode

## Installation

- Prerequisites: 
  - You should be familiar with running a notebook on OfAS, you can follow this [doc](https://docs.spot.io/ocean-spark/tools-integrations/connect-jupyter-notebooks) 
  - You should have the Jupyter notebook Python package installed locally

You have 2 options to enable Ocean for Apache Spark connection with your notebook in VSCode, you can either: 
- Clone this repo and put your notebooks in it [Option 1](#option-1---clone-this-repo)
- Copy configuration into your existing vscode folder or workspace [Option 2](#option-2---copy-config-files)

### Option 1 - Clone this repo

Clone this repo :   
`git clone https://github.com/epignot/vscode-ofas-notebook-template.git`

> Your notebook files should live in the `vscode-ofas-notebook-template` folder  

Open the folder `vscode-ofas-notebook-template` with VSCode

Next : [Connect to Remote server](#connect-to-remote-server)

### Option 2 - Copy config files

Open your existing project with VSCode

Open or create `.vscode` folder at the root of your project  

In `.vscode` folder, create or open `launch.json` file :  
Insert or merge this configuration in it : 
```json
{
    "configurations": [
        {
            "name": "Connect to remote Jupyter",
            "request": "launch",
            "type": "node-terminal",
            "command": "jupyter notebook --no-browser --GatewayClient.url=https://api.spotinst.io/ocean/spark/cluster/${input:clusterId}/notebook/ --GatewayClient.auth_token=${input:token} --GatewayClient.request_timeout=600 ",
        }
    ],
    "inputs": [
        {
            "id": "clusterId",
            "type": "promptString",
            "description": "OfAS Cluster Id",
        },
        {
            "id": "token",
            "type": "promptString",
            "description": "Spot Personal Access Token",
        }
    ]
}
```


In `.vscode` folder, create or open `settings.json` file : 
Insert or merge this settings in it : 
```json
{
    "jupyter.jupyterLaunchTimeout": 600000,
    "jupyter.disableJupyterAutoStart": true,
}
```

If you're versionning your code with git, we recommend adding this line to your `.gitignore`:
```
.ipynb_checkpoints
``` 


## Install Jupyter extension

Be sure to have this VSCode extension installed in your workspace :  
- [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) Jupyter notebook support, interactive programming and computing that supports Intellisense, debugging and more.



## Connect to Remote server

- Go to "Run and Debug" panel
- Select `Connect to remote Jupyter`
- Click on triangle icon  
- Enter your OfAS cluster id when prompted and hit enter
- Enter your Spot personal access token when prompted and hit enter


You should see the notebook app starting in the terminal

**copy the url in the output like :  `http://localhost:8888/?token=xxx`**


## Launch a notebook  

- Open a notebook file (.ipynb)
- In the status bar, click on "Jupyter Server: remote" (down-right corner)
- When the Palette input prompts: 
  - Select : `Existing`
  - Paste the url copied before
  - And hit Enter
  - wait few seconds for the palette to close
- In the upper-right corner of the notebook, click on the kernel, and pick a config-template

Now, if you run code in your notebook, it will start an app for you in OfAS.  
_Please note that it can take few minutes for the app to be ready to execute your code_

Note: Auto-start of notebooks is disabled to avoid starting multiple app before you're sure of the config template you want to use. Feel free to change this in the setting file. (`jupyter.disableJupyterAutoStart`)

### End connection to remote server
When you're done, Go to terminal panel and Hit `Ctrl-C` then enter `y` to shutdown connections and kernels.  



