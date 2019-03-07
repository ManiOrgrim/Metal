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
    return ".....0......"


def evolve(stato):
    new_state=""
    midstate="..."
    new_state+=stato[0]
    
    length=len(stato)
    for i in (2, length-1):
       midstate=stato[i-1]+stato[i]+stato[i+1]
       new_state+=rule30.get(midstate)
    new_state+=stato[len(stato)]
    return new_state

def simulation(nsteps):
    initial_state = generate_state()
    states_seq = [initial_state]
    for i in range(nsteps):
        old_state = states_seq[-1]
        new_state = evolve(old_state)
        states_seq.append(new_state)
    return states_seq

print (simulation(10))



########################################################

def test_generation_valid_state():
    state = generate_state()
    assert set(state) == {'.', '0'}
    

def test_generation_single_alive():
    state = generate_state()
    num_of_0 = sum(1 for i in state if i=='0')
    assert num_of_0 == 1
