from splearn.datasets.base import load_data_sample
from splearn.spectral import Spectral
train_file = '3.pautomac.train.txt'
test_file = '3.testdata'
train = load_data_sample(train_file)
test = load_data_sample(test_file)
print(train.nbL)    # number of letters
print(train.nbEx)   # number of sequences
print(train.data)   # train data as array
est = Spectral()    # create estimator
print(est.get_params())     # get estimator params
est.set_params(lrows=5, lcolumns=5, smooth_method='trigram', version='factor')  # set estimator params
est.fit(train.data)     # train automata
est.set_params(mode_quiet=True)     # set to quite mode
print(est.automaton.initial)    # print initial probabilities
print(est.automaton.final)      # print final state probabilities
print(est.automaton.transitions)    # print transition matrices
print(est.predict(test.data))       # print prediction
