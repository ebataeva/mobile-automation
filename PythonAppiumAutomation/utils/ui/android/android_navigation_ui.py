from typing import Final

from utils.ui.navigaion_ui import NavigationUI


class AndroidNavigationUI(NavigationUI):
    my_lists_button: Final = "xpath://android.widget.FrameLayout[@content-desc='My lists']"
    explore_button: Final = "xpath://android.widget.FrameLayout[@content-desc='Explore']"

    def __init__(self, driver):
        super().__init__(driver)
