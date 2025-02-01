# Outlook-Addin-TaskPane-python
Template to get start started writing a TaskPane Outlook Add-in using python for the backend

This template is a modified version of the office Addin taskpane JS repository here: https://github.com/OfficeDev/Office-Addin-TaskPane-JS with a combination of the python webapp repository from here: https://github.com/Azure-Samples/python-docs-hello-world.
The html files are placed in the `Templates` folder while the assests pictures, javascript files, and css files are placed in the `static` folder. This is to help flask know where html, css, and javascript files would be.

## Version Updates

- 1.0.0.1 - Integrated https into development build using office-addin-dev-certs. We re-wrote the [office-addin-dev-certs](https://github.com/OfficeDev/Office-Addin-Scripts/tree/master/packages/office-addin-dev-certs) from typescript to python.
- 1.0.0.0 - Initial release

## Test webapp before deployment
You can run flask locally for development
1. [Download the zip](https://github.com/Masterjx9/Outlook-Addin-TaskPane-python/archive/refs/heads/master.zip) or use `git clone https://github.com/Masterjx9/Outlook-Addin-TaskPane-python.git` then go to the root of the folder and perform the following commands:

### For Windows
```powershell
py -3 -m venv .venv
.venv\scripts\activate
pip install -r requirements.txt
```

### For MacOS/Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. In cmd, vscode, or powershell, go to the root of your folder and type `python app.py` 
3. Go to OWA and add your maniest.xml. There are multiple methods dependings on your permissions and rights to your azure ad - 
- If you are an admin: https://docs.servicenow.com/bundle/quebec-employee-service-management/page/product/workplace-reservations-outlook-addin/task/upload-the-manifest-file-office365.html <br><br>

- If you are a normal user: <br>
  - Go to this link: https://aka.ms/olksideload <br>
  - From the “Custom Add-ins” pop-up click the “My Add-ins” tab <br>
  ![My Add-ins](https://learn.microsoft.com/en-us/office/dev/add-ins/images/outlook-sideload-my-add-ins-owa.png "Image Title")
  - On the “My Add-ins” tab scroll down to bottom of the page and click the “+ Add a Custom Add-in link. <br>
  ![+ Add a Custom Add-in](https://learn.microsoft.com/en-us/office/dev/add-ins/images/outlook-sideload-custom-add-in.png "Image Title")
  - In the older version of Outlook web you may have to go to Add-in management is available under “Settings” > “Manage Add-Ins” >  “Custom Add-ins” > “My Add-ins” > “+ Add a Custom Add-in”
  - select `file` and chose your `manifest_python.xml` file, then choose `install`
  
 **Note** - You will have to change your manifest file to the hosting url later. So you will have to remove and readd the new manifest file later on. 

## Deploy the sample
Follow the same instructions given from the microsoft website: https://docs.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=powershell&pivots=python-framework-flask#deploy-the-sample

Once the sample is deployed, test your webapp's urls to make sure they work. 
After, you can modify the `manifest_python.xml` to route all `https://localhost:5000` urls to your own hosted url.
