from os import listdir
from SRQueue import SRQueue
from time import time
import sys

# VERY VERY IMPORTANT: must be inside this if name == main otherwise transcribe_asynch makes recursive processes
if __name__ == '__main__':
    audiofiles = listdir('audio_recordings')
    audiofiles = [ fi for fi in audiofiles if fi.endswith(".flac") ]
    filepath = 'audio_recordings/'

    queue = SRQueue(100)
    for audiofile in audiofiles:
        inputfile = filepath + audiofile
        queue.enqueue(inputfile)
    t1 = time()
    queue.transcribe_synch()
    print('processing synchronously took:', time() - t1, '(s)')

    queue = SRQueue(100)
    num_processes = queue.num_concurrent
    for audiofile in audiofiles:
        inputfile = filepath + audiofile
        queue.enqueue(inputfile)
    t1 = time()
    queue.transcribe_asynch()
    print('processing asynchronously with', num_processes, 'processes:',time() - t1, '(s)')
    