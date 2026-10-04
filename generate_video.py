import cv2
import numpy as np
import random

width, height = 1280, 720
fps = 30
out = cv2.VideoWriter('data/sample.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

# Background (soil)
soil_base = np.zeros((height, width, 3), dtype=np.uint8)
soil_base[:] = (45, 120, 35) # BGR brown/greenish

# Add noise/texture to soil
noise = np.zeros((height, width, 3), dtype=np.uint8)
cv2.randn(noise, 0, 20)
soil_base = cv2.add(soil_base, noise)

y_offset = 0
speed = 5 # pixels per frame downward

# Pre-generate some 'weeds' and 'cotton' absolute Y positions
items = []
for i in range(100):
    y = random.randint(-5000, 720)
    x = random.randint(0, width)
    # Cotton mostly in center corridor
    is_cotton = random.random() < 0.3 and (width*0.3 < x < width*0.7)
    items.append({'x': x, 'y': y, 'cotton': is_cotton, 'size': random.randint(20, 60)})

for frame_idx in range(150):
    frame = soil_base.copy()
    # Move offset
    y_offset += speed
    
    # Draw items
    for item in items:
        cy = item['y'] + y_offset
        if 0 < cy < height + 100:
            color = (30, 200, 50) if item['cotton'] else (10, 150, 20) # BGR
            cv2.circle(frame, (item['x'], cy), item['size'], color, -1)
            # Add some leaf texture
            cv2.circle(frame, (item['x']+5, cy-5), int(item['size']*0.6), (40, 220, 60), -1)

    out.write(frame)

out.release()
