import pyautogui

class MouseController:
    def __init__(self):
        pass

    def move_to(self, x, y, duration=0.0):
        """
        Move the mouse to the specified x, y coordinates.
        :param x: X-coordinate on the screen.
        :param y: Y-coordinate on the screen.
        :param duration: Time taken to move the mouse (in seconds).
        """
        pyautogui.moveTo(x, y, duration=duration)

    def click(self, x=None, y=None, button='left'):
        """
        Click at the specified x, y coordinates. If no coordinates are provided, click at the current mouse position.
        :param x: X-coordinate on the screen (optional).
        :param y: Y-coordinate on the screen (optional).
        :param button: Button to click ('left', 'right', 'middle').
        """
        if x is not None and y is not None:
            pyautogui.click(x, y, button=button)
        else:
            pyautogui.click(button=button)

    def double_click(self, x=None, y=None, button='left'):
        """
        Perform a double click at the specified coordinates or current position.
        :param x: X-coordinate on the screen (optional).
        :param y: Y-coordinate on the screen (optional).
        :param button: Button to click ('left', 'right', 'middle').
        """
        if x is not None and y is not None:
            pyautogui.doubleClick(x, y, button=button)
        else:
            pyautogui.doubleClick(button=button)

    def right_click(self, x=None, y=None):
        """
        Perform a right click at the specified coordinates or current position.
        :param x: X-coordinate on the screen (optional).
        :param y: Y-coordinate on the screen (optional).
        """
        self.click(x, y, button='right')

    def find_image(self, image_path, confidence):
        """
        Finds the location of the image on the screen.
        :param confidence: Float value between 0 and 1, specifying the accuracy required to detect the image.
                           Higher confidence means stricter matching. (Requires opencv-python)
        :return: The top-left coordinates of the found image (x, y) or None if not found.
        """
        location = pyautogui.locateOnScreen(image_path, confidence=confidence)
        if location:
            return location.left, location.top
        return None

# Example usage
if __name__ == "__main__":
    mouse = MouseController()

    # Move to position (100, 200) and click
    mouse.move_to(100, 200, duration=0.5)
    mouse.click()

    # Right-click at position (150, 250)
    mouse.right_click(150, 250)

    # Double-click at current mouse position
    mouse.double_click()