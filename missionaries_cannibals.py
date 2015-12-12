# Missionaries and Cannibals Problem
# Author: Meenal Jain and Maurice Kelly


#breadth first algorithm
def bfs(stateSpace):
    start=[3,3,'L']
    goal=[3,3,'R']
    fringe=[]
    state=[]
    children=[]
    if start==goal:
        return start
    traversed=[]
    fringe.append(start)
    while fringe:
        state=fringe.pop()
        if state==goal:
            return state
        traversed.append(state)
        children=traverse(state, stateSpace, goal)
        for x in children:
            if (x not in traversed) or (x not in fringe):
                fringe.append(x)
    return traversed
    

# to check whether the state is valid or not 
def valid(state, stateSpace):
    if state in stateSpace:
        if (state[0]>=0 and state[1]>=0 and state[0]>=state[1]) or (state[0]==0 and state[1]>=0):
            return True
        else:
            return False

# to traverse the state space
def traverse(tmp_state, stateSpace, goal):
    
    child=[]
    next_state=[]
    if tmp_state in stateSpace:
        if tmp_state[2] == 'L':
            if next_state == goal:
                return child
            else:
                next_state=[tmp_state[0]-1,tmp_state[1]-1,'R'] #1M1CL-->R
                if valid(next_state, stateSpace):
                    parent=tmp_state
                    child.append(next_state)
                    
            if next_state == goal:
                return child
            else:    
                next_state=[tmp_state[0]-2,tmp_state[1],'R'] #2M0CL-->R
                if valid(next_state, stateSpace):
                    parent=tmp_state
                    child.append(next_state)

            if next_state == goal:
                return child
            else:    
                next_state=[tmp_state[0],tmp_state[1]-2,'R'] #0M2CL-->R
                if valid(next_state, stateSpace):
                    parent=tmp_state
                    child.append(next_state)
                
            if next_state == goal:
                return child
            else:
                next_state=[tmp_state[0]-1,tmp_state[1],'R'] #1M0CL-->R
                if valid(next_state, stateSpace):
                    parent=tmp_state
                    child.append(next_state)

            if next_state == goal:
                return child
            else:    
                next_state=[tmp_state[0],tmp_state[1]-1,'R'] #0M1CL-->R
                if valid(next_state, stateSpace):
                    parent=tmp_state
                    child.append(next_state)
        else:
            if next_state == goal:
                return child
            else:
                next_state=[tmp_state[0]-1,tmp_state[1]-1,'L'] #L<--1M1CL
                if valid(next_state, stateSpace):
                    parent=tmp_state
                    child.append(next_state)
            if next_state == goal:
                return child
            else:        
                next_state=[tmp_state[0]-2,tmp_state[1],'L'] #L<--2M0CL
                if valid(next_state, stateSpace):
                    parent=tmp_state
                    child.append(next_state)

            if next_state == goal:
                return child
            else:    
                next_state=[tmp_state[0],tmp_state[1]-2,'L'] #L<--0M2CL
                if valid(next_state, stateSpace):
                    parent=tmp_state
                    child.append(next_state)
            if next_state == goal:
                return child
            else:    
                next_state=[tmp_state[0]-1,tmp_state[1],'L'] #L<--1M0CL
                if valid(next_state, stateSpace):
                    parent=tmp_state
                    child.append(next_state)
            if next_state == goal:
                return child
            else:    
                next_state=[tmp_state[0],tmp_state[1]-1,'L'] #L<--0M1CL
                if valid(next_state, stateSpace):
                    parent=tmp_state
                    child.append(next_state)

    return child

   
def main():
    stateSpace = [
	[3,3,'L'],[3,2,'L'],[2,2,'L'],[3,1,'L'],[1,1,'L'],[0,2,'L'],[0,1,'L'],[0,3,'L'],[0,0,'L'],[3,0,'L'],
	[3,3,'R'],[3,2,'R'],[2,2,'R'],[3,1,'R'],[1,1,'R'],[0,2,'R'],[0,1,'R'],[0,3,'R'],[0,0,'R'],[3,0,'R']]

    goal=[0,0,'R']

    path=bfs(stateSpace)
    print("The path from start to goal in State Space is:", path)
    
    first_path=[]
    for t in path:
        if t!=goal:
            first_path.append(t)
        elif t==goal:
            first_path.append(goal)
            print("The breadth first search solution is:", first_path)
            break
            
