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
    return "..0..00....."


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

print (simulation(100))



########################################################

def test_generation_valid_state():
    state = generate_state()
    assert set(state) == {'.', '0'}
    

def test_generation_single_alive():
    state = generate_state()
    num_of_0 = sum(1 for i in state if i=='0')
    assert num_of_0 == 1
