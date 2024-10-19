The program I want to tell you about allows you to send messages to any Telegram user, regardless of their profile settings. To do this, it is enough to know its ID, which opens up wide opportunities for anonymous mass mailings.
Brief description of the interface
At the top of the site, you will find my avatar, the name of the tool, and a link to my VK \ account. Now let's take a closer look at the\input fields. I will list them from top to bottom:

![image](https://github.com/user-attachments/assets/d0a5b2ca-5dc0-4518-9e19-1ab78c891a6f)


Token field:

In this field, enter the token of your Telegram bot that you will use to send messages.

Text message field:

Here you can specify the text for the\mailing list. All characters are supported, but formatting is not supported by.

Path File Field:

Here you need to specify the path to the\file.xlsx with a list of\IDs. Please note that only the\format is supported.xlsx!

"Send" button

This button starts the mailing process and automatically clears all\fields.

Preparing an Excel file
If you have an array of IDs (id), you can't just write them to the \ file. To simplify this task, you can use a special id parser:



Rules for placing IDs:

The first column must have the name "ID".

Each ID is written in a new cell in this column.

Launch
Download the archive and unzip it.

Open the "Appl" folder and run the file "App.exe".

Your browser will automatically open the site with the\interface. Follow the instructions above to fill in all the required\fields.

To exit, type the following command in the CMD console::

taskkill /im App.exe /f /t*

