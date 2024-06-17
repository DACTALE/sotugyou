#関数：ウィンドウの枠をトグルする
def toggle_decoration(window):

    if window.overrideredirect():
        window.overrideredirect(False)
    else:
        window.overrideredirect(True)