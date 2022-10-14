"""
Created on Tue Sep 27 13:43:21 2022
Lab 2 - Vacuum Cleaner Agent
COEN 166L - Wednesday 2:15PM

@author: Marianne Fuyu Yamazaki Dorr

Requirements:
    
• Define the “state” as a list of three elements: the 1st element specifies the status of the left square
(“Clean” or “Dirty”), the 2nd element specifies the status of the right square (“Clean” or “Dirty”),
and the 3rd element specifies the current location of the agent (0 for left square, 1 for right
square).

• The candidate actions are “Suck”, “Left” (moving to the left square), “Right” (moving to the
right square). Each action costs 1 point.

• The agent will take an action based on the current state. The agent program can update the state
immediately after an action is taken. The program terminates when both squares are clean.

• Create a test case to verify your code. The test case takes two inputs: the current state, and an
empty list that will store the actions; then it will generate two outputs: the sequence of actions
taken by the agent to achieve the goal state, and the corresponding total cost.

• Your test case should be able to take any possible inputs, generate the corresponding outputs,
and verify whether the outputs are correct or not. For example, if the outputs are correct, then
your test code can print a message: “Correct Outputs!” Otherwise, it can print: “Wrong
Outputs!”

• Explain in detail how your code works (for example, what each function does, and how the test
case works).

"""

# Lab 2 Vaccuum Bot
# Actions = {"Suck", "Left", "Right"}
# state is list ("Clean", "Dirty", 0 or 1) 0 = left and 1 = right

#Checks if all squares are clean, if yes returns True, if not returns False
def is_goal(state):
    if (state[0] == "Clean") & (state[1] == "Clean"):
        return True
    else:
        return False

#Checks if square at the vaccuum bot's location is dirty. If yes, returns True, False otherwise
def is_dirty(state):
    if(state[2] == 0):
        if(state[0] == "Dirty"):
            return True
        else:
            return False
    else:
        if(state[1] == "Dirty"):
            return True
        else:
            return False

#Changes the state of the square where the vaccuum is at to "Clean" and returns the action "Suck"
def cleanup(state):
    if (state[2] == 0):
        state[0] = "Clean"
    else:
        state[1] = "Clean"
    return "Suck"

#Moves the location of the vaccuum bot and returns the action of the movement made either "Right" or "Left"
def move(state):
    if(state[2] == 0):
        state[2] = 1
        return "Right"
    else:
        state[2] = 0
        return "Left"

#Tests the vaccuum bot code and checks if it returns the correct output
def test_case(state, action_seq):
    
    totalCost = 0
    original_state = state.copy()
    
    #Generate sequence of actions taken by vaccuum bot
    while(is_goal(state) == False):
        if (is_dirty(state) == True):
            action_seq.append(cleanup(state))
            totalCost += 1
        else:
            action_seq.append(move(state))   
            totalCost += 1
    
    #Print sequence of actions and total cost of vaccuum bot
    print("The sequence of actions taken by the vacuum bot is: " + str(action_seq))
    print("The total cost of the sequence is: " + str(totalCost))
    print()
    
    #Check if outputs are correct for all possible inputs
    correct = None
    if (original_state == ['Dirty', 'Dirty', 0]):
        if (action_seq == ["Suck", "Right", "Suck"]):
            correct = True
        else:
            correct = False
    if (original_state == ['Dirty', 'Dirty', 1]):
        if (action_seq == ["Suck", "Left", "Suck"]):
            correct = True
        else:
            correct = False
    
    if (original_state == ['Clean', 'Dirty', 0]):
        if (action_seq == ["Right", "Suck"]):
            correct = True
        else:
            correct = False
    if (original_state == ['Clean', 'Dirty', 1]):
        if (action_seq == ["Suck"]):
            correct = True
        else:
            correct = False
    if (original_state == ['Dirty', 'Clean', 0]):
        if (action_seq == ["Suck"]):
            correct = True
        else:
            correct = False 
    if (original_state == ['Dirty', 'Clean', 1]):
        if (action_seq == ["Left", "Suck"]):
            correct = True
        else:
            correct = False
    if (is_goal(original_state) == True):
        if (action_seq == []):
            correct = True
        else:
            correct = False
    
    #Checks if both the action_seq and totalCost match up        
    success = None     
    if (correct == True) & (totalCost == len(action_seq)):
        print("Correct Outputs!")
        success = True
    else:
        print("Wrong Outputs!")
        success = False
    print()
    #returns the list of actions taken, the cost of those actions, and whether the test was successful or not
    return action_seq, totalCost, success

#Tests:
test1 = ["Dirty", "Dirty", 0]
test2 = ["Dirty", "Dirty", 1]
test3 = ["Clean", "Dirty", 0]
test4 = ["Clean", "Dirty", 1]
test5 = ["Dirty", "Clean", 0]
test6 = ["Dirty", "Clean", 1]
test7 = ["Clean", "Clean", 0]
test8 = ["Clean", "Clean", 1]
list_tests = [test1, test2, test3, test4, test5, test6, test7, test8]

score = 0
for test in list_tests: 
    print("---------------------------------")
    print("Original state is: " + str(test))
    print()
    test_action_seq = []
    result = test_case(test, test_action_seq)
    if (result[2] == True):
        score += 1
    print("End state is: " + str(test))
    print("---------------------------------")

print()
print("##################")
print()
print("Score: " + str(score) + "/" + str(len(list_tests)))
print()
print("###################")



    