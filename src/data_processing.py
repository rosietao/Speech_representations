# pip install torchaudio librosa


from torchaudio.datasets import LIBRISPEECH
librispeech = LIBRISPEECH(root="./data", url="train-clean-100", download=True)

