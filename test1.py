from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from moviepy.editor import *
import time

# Set up the Chrome driver (you can use other browsers as well)
driver = webdriver.Chrome()

# Replace 'localhost' with your webpage's URL
driver.get("https://guru.mylanguage.net.au/life")
time.sleep(10)
# switch to the iframe
iframe = driver.find_element_by_tag_name('iframe')
driver.switch_to.frame(iframe)

# Find the play button and click it
wait = WebDriverWait(driver, 10)
play_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'vjs-big-play-button')))
play_button.click()

# Switch back to the main content
driver.switch_to.default_content()

# Wait for some time to ensure the video starts playing
# You might need to adjust the waiting time depending on the video's length
time.sleep(10)

# Save the video using moviepy and extract the audio
video_path = "c:/python/jfilm/video/test.mp4"  # Change this to your video file's path
video = VideoFileClip(video_path)
audio = video.audio
audio.write_audiofile("output_audio.mp3")

# Close the browser
driver.quit()
