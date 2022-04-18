# CLOC Analyser
This Python program is used to execute cloc on given Github repository and send output through email as an attachment. 
This program works both on Linux and Windows.

CLOC installation
-----------------
You can download CLOC latest version from https://github.com/AlDanial/cloc/releases/tag/v1.92

CLOC Analyser Configuration
---------------------------
Configure the below parameters to run this program.
1. github_url = "Enter Github repository address"
2. sender_email_addr = "Enter your email address" 
3. sender_email_pass = "Enter your email address password to login into your account"
4. receiver_email_addr = "Enter receiver email address"
5. win_cloc_path = "absolute path to exe file" 
6. linux_cloc_path = "absulute path to cloc executable file" 

NOTE: To login and send email from this script from your gmail account please make 'Allow less secure apps' ON
Go to the Less secure app access section of your Google Account. You might need to sign in.
Turn Allow less secure apps off.
If the two step verification is on, you cannot use the less secure access.

Installation
------------
1. $ sudo git clone https://github.com/hawkflight666/cloc.git 
2. $ cd cloc 
3. $ sudo chmod +x ClocAnalyser.py 
4. $ py ClocAnalyser.py
