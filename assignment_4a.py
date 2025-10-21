# write a python function that will determine
# the input file type and only accept specific file types (video, image)


image_types = ['jpg', 'jpeg', 'png', 'gif']
video_types = ['mp4', 'avi', 'mov', 'mkv']

file_name = input("Insert file name here: ").lower()
file_name_split = file_name.split('.')
extention = file_name_split[-1]

def file_detector():
    if extention in image_types:
        print(f"Your file {file_name} is a photo")
    elif extention in video_types:
        print(f"Your file {file_name} is a video")
    else:
        print(f"Your file {file_name} is unsupported")

file_detector()
        
    
    
    