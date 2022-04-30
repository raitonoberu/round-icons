For example, let's add the telegram icon to the list.

1. Find a white PNG square logo without a background. I googled `telegram logo png white`. That's what I found: <img width="50" src="logos/telegram.png">
2. Resize it to `512x512`. Make sure you crop it properly.
3. Find a suitable background color. I use [brandcolors.net](https://brandcolors.net). For telegram it's `#0088CC`.
4. Put the logo to the `logos` folder.
5. Edit `icons.yaml`. Set the name (in lowercase) and color in HEX format without `#`.
6. Install Python dependencies. Run `python -m pip install -r requirements.txt`.
7. Use the generator. Run `python generate.py telegram` with your icon name.
8. Check if everything is okay. Open one of the folders and look at your new cute icon.
9. Edit `README.md`. Add your icon to the list.
10. Open a pull request.

Alternatively, find the logo and color and create a new issue, I'll do the rest for you.
