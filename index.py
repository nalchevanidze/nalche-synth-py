from audioProcessing import AudioProcessor
from connecting_system import SharedData, ConnectingTread
from app_screen import AppScreen

shared_data = SharedData()
audio_thread = ConnectingTread(AudioProcessor, shared_data)
gui_thread = ConnectingTread(AppScreen, shared_data)
audio_thread.start()
gui_thread.start()
audio_thread.join()
gui_thread.join()
