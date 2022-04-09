import speech_recognition as sr
import os            
import multiprocessing as mp

# can't be member of SRQueue b/c "weakref can't be pickled"
def asynch_helper(queue):
    while not queue.empty():
        proc = os.getpid()
        audiofile = queue.get()
        print(f"Processing {audiofile} with process id: {proc}")
        source = sr.AudioFile(audiofile)
        recognizer = sr.Recognizer()
        with source as s:
            audio = recognizer.record(s)
        transcription = recognizer.recognize_google(audio)
        name = audiofile.split('.')[0] + '.txt'
        f = open(name,'w')
        f.write(transcription)
        f.close()

class SRQueue:
    def __init__(self, num_processes = 1) -> None:
        max_concurrent = mp.cpu_count() - 1
        self.num_concurrent = max(min(max_concurrent, num_processes),1)
        self.input_queue = mp.Queue()
        self.output_queue = mp.Queue()
        self.processes = []

    def enqueue(self, audiofile:str) -> None:
        self.input_queue.put(audiofile)
  
    def transcribe_asynch(self):
        for _ in range(self.num_concurrent):
            p = mp.Process(target=asynch_helper, args = (self.input_queue,)) # dont know why the comma is needed
            self.processes.append(p)
            p.start()
        for p in self.processes:
            p.join()
        self.processes.clear()

    def transcribe_synch(self):
        while not self.input_queue.empty():
            proc = os.getpid()
            audiofile = self.input_queue.get()
            print(f"Processing {audiofile} with process id: {proc}")
            source = sr.AudioFile(audiofile)
            recognizer = sr.Recognizer()
            with source as s:
                audio = recognizer.record(s)
            transcription = recognizer.recognize_google(audio)
            name = audiofile.split('.')[0] + '.txt'
            f = open(name,'w')
            f.write(transcription)
            f.close()



            



            