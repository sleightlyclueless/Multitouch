# Multitouch Summary
## Interfaces
Interfaces are needed so humans can interact with computers.
- **C**ommand **L**ine **I**nterface:
    - Only Text In/Output
    - Very abstract
- **G**raphical **U**ser **I**nterface:
    - Most commonly used
    - Indirect control
    - Not intuitive at first
- **N**atural **U**ser **I**nterface:
    - Physical/Direct Interaction
    - Speech Recognition/Face Tracking also belong in this category
### Examples:
- Time-of-Flight Camera:
    - x/y-Rasterization + Color, third parameter describe distance of pixel to camera (done by measuring time the light needs to travel)
    - Good for tracking hands
- Kinect:
    - Projects Point Cloud into the room
    - Infrared sensor picks up points
    - Calculates distances of objects in scene based on point data
- VR:
    - Works with sensors to track head movements
    - Ja diggi ist halt immersive 
## Multi User/Multi Touch
- Capacitive Touch Screen:
    - Based on electrostatic fields
    - Controller recognizes changes and calculates x/y position
- Resistive Touch Screen:
    - Two layers
    - Touch creates current at specific location
    - Controller calculates position
- Optical sensors:
    - Light shines against surface
    - Objects in the way reflect light
    - Camera picks up objects
    - Frustrated Total Internal Reflection
        - Plexiglass "contains" IR LED beams
        - Objects cause them to reflect out of the Glass pane
        - Camera picks up "leaked" IR light
    - Diffused Surface Illumination
        - Same as Frustrated, except glass is always glowing
        - Camera picks up when light is blocked
## Image Processing
- Background Subtraction (difference image)
- Highpass filter (blur + difference image)
- Segmentation (binarization with threshold)
- Edge detection (with i.e. Sobel)

# Gestures
## Continuous 
- No real end or beginning
- "Dragging Gestures"
- Examples include translation, rotation, scaling
## Discrete
- Start- and end point
- Timeframe is very important
- Must be normalized (size, position, number of points)
### Evaluations
#### Region based
- Overlays grid on gesture
- Very simple and fast, but not reliably
#### Directional based
- Keep track of directions of points
- Also not very reliable
#### Vector based 
- Evaluate using the dot product
- Checks the angle between the vectors of all points
- 1 => Identical; -1 => Opposite; 0 => Orthogonal vectors
- Sum all dot products, divide by # of vectors
- The closer to 1 the more likely to match
#### $1 Recognizer Paper
- 4 Steps:
    1. Normalize Points 
    2. Rotate starting point so it touches the x axis
    3. Scale & translate
    4. Evaluate
        1. Calculate & sum the average distance between candidate and template points and then divide by # of points
        2. Calculate score 
        3. Rotate to find optimal angle
- Rotation has 3 possibilities:
    - Brute force: just checks everything, very inefficient
    - Hill climb: checks for first minima and stops, only good for similar gestures
    - Golden ratio: uses golden ratio (a+b is to a as a is to b) to find minima faster