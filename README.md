# Office-Addin-TaskPane-python
Template to get start started writing a TaskPane Office Add-in using python for the backend

This template is a modified version of the office Addin taskpane JS repository here: https://github.com/OfficeDev/Office-Addin-TaskPane-JS with a combination of the python webapp repository from here: https://github.com/Azure-Samples/python-docs-hello-world.
The html files are placed in the `Templates` folder while the assests pictures, javascript files, and css files are placed in the `static` folder. This is to help flask know where html, css, and javascript files would be.

## Test webapp before deployment
You can't sideload the webapp as there is no module with python that can sideload your app in development mode like a node.js webapp can. **However** you can still run flask locally and double check that your html files are being routed correctly.
1. Download the zip then go to the root of the folder and perform the following commands:
> py -3 -m venv .venv

>.venv\scripts\activate

>pip install -r requirements.txt
2. In cmd, vscode, or powershell, go to the root of your folder and type `flask run`

## Deploy the sample
Follow the same instructions given from the microsoft website: https://docs.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=powershell&pivots=python-framework-flask#deploy-the-sample

Once the sample is deployed, test your webapp's urls to make sure they work. 
After, you can modify the `manifest_python.xml` to route all `https://localhost:3000` urls to your own hosted url.
