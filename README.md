HAND TRACKING WITH OPENCV

MEDIAPIPE PRINCIPLE:
Hand tracking using MediaPipe involves two stages:

PALM DETECTION - MediaPipe works on the complete input image and provides a cropped image of the hand.

HAND LANDMARKS IDENTIFICATION - MediaPipe finds the 21 hand landmarks on the cropped image of the hand.

The 21 hand points that MediaPipe identifies are shown in the image below:
![image](https://github.com/Priyavarthini08/HandTracking/assets/145207599/bb2312f2-7fa8-4669-86d4-38eef62f505d)

REQUIRED MODULES:
–> pip install opencv-python

–> pip install mediapipe

WORKING PROCESS:
we create a class called handDetector with two member functions in it, named findHands and findPosition.

The function findHands will accept an RGB image and detects the hand in the frame and locate the key points and draws the landmarks, 
the function findPosition will give the position of the hand along with the id.

Then the main function where we initialize our module and also we write a while loop to run the model. 
Here you can import this setup or the module to any other further related project works.

The output will detect the hand and give tthe positions of the tracked hands.

APPLICATIONS:
Handtracking can be applied in many fields like virtual touchscreen interface, 3D object manipulation, medical training stimulation, Gesture controlled presentations

