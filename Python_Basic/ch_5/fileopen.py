import tkinter.filedialog as tk
videotype = [("Video file","*mp4 *mkv")]
video = tk.askopenfilename(title="video",filetypes=videotype )

print(video)