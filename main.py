# import cv2
# import pickle
# import cvzone
# import numpy as np

# # Load image
# img = cv2.imread('Image.png')  # Use the same image as in the position generator

# # Load parking positions
# with open('CarParkPos', 'rb') as f:
#     posList = pickle.load(f)

# width, height = 107, 48

# def checkParkingSpace(imgPro):
#     spaceCounter = 0

#     for pos in posList:
#         x, y = pos

#         imgCrop = imgPro[y:y + height, x:x + width]
#         count = cv2.countNonZero(imgCrop)

#         if count < 900:
#             color = (0, 255, 0)
#             thickness = 5
#             spaceCounter += 1
#         else:
#             color = (0, 0, 255)
#             thickness = 2

#         cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
#         cvzone.putTextRect(img, str(count), (x, y + height - 3), scale=1,
#                            thickness=2, offset=0, colorR=color)

#     cvzone.putTextRect(img, f'Free: {spaceCounter}/{len(posList)}', (100, 50), scale=3,
#                        thickness=5, offset=20, colorR=(0,200,0))

# # Image processing
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
# imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#                                     cv2.THRESH_BINARY_INV, 25, 16)
# imgMedian = cv2.medianBlur(imgThreshold, 5)
# kernel = np.ones((3, 3), np.uint8)
# imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

# # Check parking spaces
# checkParkingSpace(imgDilate)

# # Display result
# cv2.imshow("Image", img)
# cv2.waitKey(0)  # Wait for key press to close
# cv2.destroyAllWindows()



# 2nd one


# import cv2
# import pickle
# import cvzone
# import numpy as np

# # Load image
# img = cv2.imread('Image.png')  # Use the same image as in the position generator

# # Load parking positions
# with open('CarParkPos', 'rb') as f:
#     posList = pickle.load(f)

# width, height = 107, 48

# def checkParkingSpace(imgPro):
#     spaceCounter = 0
#     freeSlots = []  # List to store the numbers of free slots

#     for i, pos in enumerate(posList, start=1):  # Start numbering from 1
#         x, y = pos

#         # Crop the image for the current slot
#         imgCrop = imgPro[y:y + height, x:x + width]
#         count = cv2.countNonZero(imgCrop)

#         # Determine if the slot is free
#         if count < 900:
#             color = (0, 255, 0)  # Green for free
#             thickness = 5
#             spaceCounter += 1
#             freeSlots.append(i)  # Add slot number to free slots
#         else:
#             color = (0, 0, 255)  # Red for occupied
#             thickness = 2

#         # Draw the rectangle for the parking slot
#         cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)

#         # Display the slot number at the top-left of the slot
#         cvzone.putTextRect(img, f'Slot {i}', (x, y - 5), scale=1, thickness=2, offset=0, colorR=color)

#         # Display the pixel count at the bottom of the slot
#         cvzone.putTextRect(img, str(count), (x, y + height - 3), scale=1, thickness=2, offset=0, colorR=color)

#     # Display the free slots count and their numbers at the top
#     free_text = f'Free: {spaceCounter}/{len(posList)}'
#     free_slots_text = f'Free Slots: {", ".join(map(str, freeSlots))}' if freeSlots else 'Free Slots: None'

#     # Display the free slots count
#     cvzone.putTextRect(img, free_text, (100, 50), scale=3, thickness=5, offset=20, colorR=(0, 200, 0))

#     # Display the free slot numbers below the count
#     cvzone.putTextRect(img, free_slots_text, (100, 110), scale=2, thickness=3, offset=10, colorR=(0, 200, 0))

# # Image processing
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
# imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#                                     cv2.THRESH_BINARY_INV, 25, 16)
# imgMedian = cv2.medianBlur(imgThreshold, 5)
# kernel = np.ones((3, 3), np.uint8)
# imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

# # Check parking spaces
# checkParkingSpace(imgDilate)

# # Display result
# cv2.imshow("Image", img)
# cv2.waitKey(0)  # Wait for key press to close
# cv2.destroyAllWindows()



import cv2
import pickle
import cvzone
import numpy as np

# Load image
img = cv2.imread('output2.png')  # Ensure the image path is correct
if img is None:
    raise FileNotFoundError("Image.png not found. Please check the file path.")

# Load parking positions
try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
except FileNotFoundError:
    raise FileNotFoundError("CarParkPos file not found. Please ensure it exists.")

# Define slot dimensions
width, height = 107, 48

def checkParkingSpace(imgPro):
    spaceCounter = 0
    freeSlots = []

    # Iterate through positions with correct slot numbering
    for i, pos in enumerate(posList, start=1):  # Start numbering from 1
        x, y = pos

        # Ensure coordinates are within image bounds
        if x + width > imgPro.shape[1] or y + height > imgPro.shape[0]:
            print(f"Warning: Slot {i} at position ({x}, {y}) exceeds image dimensions.")
            continue

        # Crop the image for the current slot
        imgCrop = imgPro[y:y + height, x:x + width]
        if imgCrop.size == 0:
            print(f"Warning: Slot {i} crop is empty at position ({x}, {y}).")
            continue

        # Count non-zero pixels to determine occupancy
        count = cv2.countNonZero(imgCrop)

        # Threshold for free/occupied slot
        if count < 900:  # Adjust threshold if needed
            color = (0, 255, 0)  # Green for free
            thickness = 5
            spaceCounter += 1
            freeSlots.append(i)
        else:
            color = (0, 0, 255)  # Red for occupied
            thickness = 2

        # Draw rectangle for the parking slot
        cv2.rectangle(img, pos, (x + width, y + height), color, thickness)

        # Display slot number at the top-left of the slot
        cvzone.putTextRect(img, f'Slot {i}', (x, y - 5), scale=1, thickness=2, offset=0, colorR=color)

        # Display pixel count at the bottom of the slot
        cvzone.putTextRect(img, str(count), (x, y + height - 3), scale=1, thickness=2, offset=0, colorR=color)

    # Display free slots count and numbers
    free_text = f'Free: {spaceCounter}/{len(posList)}'
    free_slots_text = f'Free Slots: {", ".join(map(str, freeSlots))}' if freeSlots else 'Free Slots: None'

    # Display free slots count at the top
    cvzone.putTextRect(img, free_text, (100, 50), scale=3, thickness=5, offset=20, colorR=(0, 200, 0))

    # Display free slot numbers below
    cvzone.putTextRect(img, free_slots_text, (100, 110), scale=2, thickness=3, offset=10, colorR=(0, 200, 0))

# Image processing
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
imgMedian = cv2.medianBlur(imgThreshold, 5)
kernel = np.ones((3, 3), np.uint8)
imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

# Check parking spaces
checkParkingSpace(imgDilate)

# Display result
cv2.imshow("Parking Lot", img)
cv2.waitKey(0)
cv2.destroyAllWindows()