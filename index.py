from audioProcessing import AudioProcessor
from connecting_system import ConnectingSystem, ConnectingTread
from app_screen import AppScreen

connecting_system = ConnectingSystem()
audio_thread = ConnectingTread(AudioProcessor, connecting_system)
gui_thread = ConnectingTread(AppScreen, connecting_system)
audio_thread.start()
gui_thread.start()
audio_thread.join()
gui_thread.join()
