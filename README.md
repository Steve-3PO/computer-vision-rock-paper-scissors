# Computer Vision RPS

## This project will show how a model can be trained to play Rock, Paper, Scissors with a computer using a webcam to record the user's selection. 
> The Model used can be accessed from Teachable-Machine and the download is shown in the repository under the file named keras_model.h5 with the corresponding labels in the labels.txt file.

### Milestone 2
> The model was trained using over 1000+ pictures for each of the possible inpputs: Rock, Paper, Scissors and Nothing, for when there is a lack of input from the user. The model was then downloaded and imported into this repository to begin accessing it. It was tested to make sure it provided a normalised output of what is seen which is given in the form [xxx, yyy, zzz, nnn] where each value corresponds to the models assertion that the user has provided either rock, paper, scissors or none. 

### Milestone 3
> Before continuing, in this milestone the appropriate packages are installed within a new Conda environment. Opencv-python, tensorflow and ipykernel were installed and the environment was put into the requirements folder so that this project can be accessed by anyone with the correct package versions.

### Milestone 4
> Ignoring the model for a second, basic code was created to play a rock paper scissors game without imaging, so that the model can be inserted into the user's inputs place. Currently, the user can provide an input and the computer will make a choice, the results are compared and a winner is announced or a tie if the inputs match.
> 

### Milestone 5
> In the final milestone, the hardcoded user input is replaced with the prediction from the model. From testing the model works majority of the time. A countdown has replaced the while loop to give the user a set amount of time to engage with the game, with the countdown being displayed on the webcam. General code cleaning, and minor optimisations are made too. 
> Further improvements to the functionality and the code may include requiring user input to initiate the coundown, as well as moving the existing code into a class format