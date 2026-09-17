# GDG-TASK1
# Mini URL Shortener
A simple Python project that converts a long URL into a short code and stores it for later use.

Commands
shorten <url>     - creates a short code
resolve <code>    - shows/opens the original URL
list              - shows all saved URLs
exit              - closes the program
Example
Enter command: shorten https://google.com
Short code: aB72xK

Enter command: list
aB72xK -> https://google.com

Enter command: resolve aB72xK
Original URL: https://google.com
Open URL? (y/n): y
The URLs are saved in urls.json, so they stay saved even after the program is closed.

The program also handles invalid URLs, duplicate URLs, and codes that don't exist.
