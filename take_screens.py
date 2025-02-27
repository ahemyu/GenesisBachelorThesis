import cv2
import numpy as np

def extract_frames(video_path, num_frames=5):
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    # Get video properties
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    
    # Calculate frame intervals
    interval = total_frames // (num_frames)
    frame_indices = [i * interval for i in range(num_frames)]
    
    # Extract frames
    frames = []
    for frame_index in frame_indices:
        # Set the frame position
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
        
        # Read the frame
        ret, frame = cap.read()
        
        if ret:
            # Save the frame
            filename = f'pictures/frame_{frame_index}.jpg'
            cv2.imwrite(filename, frame)
            frames.append(frame)
            print(f"Saved {filename}")
    
    # Release the video capture object
    cap.release()
    
    return frames

# Usage
video_path = 'backflip.mp4' 
extracted_frames = extract_frames(video_path)