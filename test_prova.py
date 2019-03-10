#file test_prova.py

rule30 = {"000": '.',
          "00.": '.',
          "0.0": '.',
          "...": '.',
          "0..": '0',
          ".00": '0',
          ".0.": '0',
          "..0": '0',
         }
def generate_state():
    return "....0......."


def evolve(stato, leng):
    new_state=""
    new_state+=stato[0]
    for i in range (1, leng-1):
        midstate=stato[i-1]+stato[i]+stato[i+1]
        new_state+=rule30.get(midstate)
    new_state+=stato[leng-1]
    return new_state


def simulation(nsteps):
    initial_state = generate_state()
    leng=len(initial_state)
    states_seq = [initial_state]
    for i in range(nsteps):
        old_state = states_seq[-1]
        new_state = evolve(old_state, leng)
        states_seq.append(new_state)
    return states_seq

def simulation_setstart(nsteps, initial):
    initial_state = initial 
    leng=len(initial_state)
    states_seq = [initial_state]
    for i in range(nsteps):
        old_state = states_seq[-1]
        new_state = evolve(old_state, leng)
        states_seq.append(new_state)
    return states_seq

print (simulation(100))



########################################################

def test_generation_valid_state():
    state = generate_state()
    assert set(state) == {'.', '0'}
    

def test_generation_single_alive():
    state = generate_state()
    num_of_0 = sum(1 for i in state if i=='0')
    assert num_of_0 == 1

def test_conservation():
    timeline=simulation(100)
    initial_state_length=len(generate_state())
    for timestep in timeline:
        assert initial_state_length==len(timestep)



from hypothesis import given
import hypothesis.strategies as st 

@given (counter1=st.integers(), counter2=st.integers())
def test_linearity(counter1, counter2):
    first_left_step=simulation(counter1)
    second_left_step=simulation_setstart(counter2, first_left_step[counter1])
    sim_right=simulation(counter1+counter2)
    assert sim_right[counter1+counter2]==second_left_step[counter2]

