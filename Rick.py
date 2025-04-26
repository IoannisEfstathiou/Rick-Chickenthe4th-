import webbrowser
import os
import time

def browser_tabs():
    #Open the tabs that match the lyrics. Inbetween, pause to let the user read.
    webbrowser.open("https://www.google.com/search?q=we%27re+no+strangers+to+love")
    time.sleep(3)
    webbrowser.open("https://www.google.com/search?q=you+know+the+rules+and+so+do+i")
    time.sleep(3)
    webbrowser.open("https://www.google.com/search?q=A+full+commitment%27s+what+I%27m+thinkin+of")
    time.sleep(5) 
    webbrowser.open("https://www.google.com/search?q=You+would+not+get+this+from+any+other+guy")
    time.sleep(5)
    webbrowser.open("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSl0VVw-MTE_pKPAdEXxfazhED7StLI4HcDgQ&s")
    time.sleep(2)
    webbrowser.open("")
    time.sleep(3)
    webbrowser.open("https://www.reddit.com/media?url=https%3A%2F%2Fpreview.redd.it%2F64iysb4i3ts41.jpg%3Fwidth%3D640%26crop%3Dsmart%26auto%3Dwebp%26s%3D879a35e8a53002032087f8a81f93b02e9a55cda4&rdt=47888")
    time.sleep(5)
    webbrowser.open("https://youtu.be/DsC8jQXRbQE?si=K5Q3t3V20Qub5F8P&t=53")


def main():
    browser_tabs()

if __name__ == "__main__":
    main()