# Office-Addin-TaskPane-python
Template to get start started writing a TaskPane Office Add-in using python for the backend

This template is a modified version of the office Addin taskpane JS repository here: https://github.com/OfficeDev/Office-Addin-TaskPane-JS with a combination of the python webapp repository from here: https://github.com/Azure-Samples/python-docs-hello-world.
The html files are placed in the `Templates` folder while the assests pictures, javascript files, and css files are placed in the `static` folder. This is to help flask know where html, css, and javascript files would be.

## Test webapp before deployment
You can run flask locally and then `temporarily` change the manifest_python.xml file to your local development url.
1. Download the zip then go to the root of the folder and perform the following commands:
> py -3 -m venv .venv

>.venv\scripts\activate

>pip install -r requirements.txt
2. In cmd, vscode, or powershell, go to the root of your folder and type `flask run`
3. in vscode, or any editor, go to the `manifest_python.xml` replace all "https://localhost:3000" with url development server's url. (for normal flask, that is usually "http://localhost:5000") 
4. Go to OWA and add your maniest.xml. There are multiple methods dependings on your permissions and rights to your azure ad - 
<br><br>If you are an admin: https://docs.servicenow.com/bundle/quebec-employee-service-management/page/product/workplace-reservations-outlook-addin/task/upload-the-manifest-file-office365.html <br><br>
  If you are a normal user: <br>
    Navigate to the “Add-Ins” menu after logging into Outlook on the web <br>
    Go to `Add-in management` under “...” ('More actions' menu which is visible from a selected email) <br>
    Click “Get Add-ins” from the "..." menu <br>
    From the “Custom Add-ins” pop-up click the “My Add-ins” tab <br>
    On the “My Add-ins” tab scroll down to bottom of the page and click the “+ Add a Custom Add-in link. <br>
    In the older version of Outlook web you may have to go to Add-in management is available under “Settings” > “Manage Add-Ins” >  “Custom Add-ins” > “My Add-ins” > “+ Add a Custom Add-in”
    select `file` and chose your `manifest_python.xml` file, then choose `install`
  
 **Note** - You will have to change your manifest file to the hosting url later. So you will have to remove and readd the new manifest file later on. 

## Deploy the sample
Follow the same instructions given from the microsoft website: https://docs.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=powershell&pivots=python-framework-flask#deploy-the-sample

Once the sample is deployed, test your webapp's urls to make sure they work. 
After, you can modify the `manifest_python.xml` to route all `https://localhost:3000` urls to your own hosted url.
