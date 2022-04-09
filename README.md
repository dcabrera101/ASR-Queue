# SRQueue

SRQueue.py contains definition of class SRQueue.

audio_recordings folder simply holds some sample audiofiles and corresponding output transcriptions used to demo.

main.py is a demo file that uses the class to transcribe 4 small audio files synchronously and then asynchronously to demonstrate performance boost. Below is a sample output:

```
Processing audio_recordings/Recording.flac with process id: 30980
Processing audio_recordings/Recording2.flac with process id: 30980
Processing audio_recordings/Recording3.flac with process id: 30980
Processing audio_recordings/Recording4.flac with process id: 30980
processing synchronously took: 5.848616600036621 (s)
Processing audio_recordings/Recording.flac with process id: 29100
Processing audio_recordings/Recording2.flac with process id: 32964
Processing audio_recordings/Recording3.flac with process id: 21464
Processing audio_recordings/Recording4.flac with process id: 19308
processing asynchronously with 7 processes: 3.0219314098358154 (s)
```

Instantiate an SRQueue object like so:

``` queue = SRQueue(num_processes) ```

...where *num_processes* is the integer number of processes you want to spawn to transcribe all the wave files in the queue. Passing an integer N less than 1 or no integer at all sets the number of processes to 1 by default. Passing an integer N greater than 1 sets the number of processes to the minimum between N and the max number of processes available based on your hardware.


SRQueue class methods:
- ```append(audiofile)```: appends filepath as a string to queue
- ```transcribe_synch()```: transcribes all files in queue synchronously. Writes each transcription to a text file named the same as its corresponding audiofile.
- ```transcribe_asynch()```: transcribes all files in queue asynchronously. Writes each transcription to a text file named the same as its corresponding audiofile.


