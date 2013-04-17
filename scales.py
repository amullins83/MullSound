CHROMATIC_STEPS = range(13)
MAJOR_STEPS = [0,2,4,5,7,9,11,12]
MINOR_STEPS = [0,2,3,5,7,8,10,12]
HARMONIC_MINOR_STEPS = [0,2,3,5,7,8,11,12]

NoteLetters = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
Octaves = range(11)
NoteNames = []

for i in Octaves:
 for name in NoteLetters:
   NoteNames.append(name + str(i))

NoteValues = range(128)

Note = dict(zip(NoteNames,NoteValues))

Flats = ["Db","Eb","Gb","Ab","Bb"];
FlatNumber = [1,3,6,8,10];

for i in Octaves:
  for j in range(len(Flats)):
    Note[Flats[j] + str(i)] = FlatNumber[j] + 12*i

def scale(start = "C5", steps=MAJOR_STEPS):
 notes = []
 startNote = Note[start]
 for i in steps:
   notes.append(startNote + i)
 return notes

def playScale(start = "C5", steps=MAJOR_STEPS):
 for note in scale(start, steps):
   playNote(note, 125, 127)

def playChord(noteList, time, amplitude):
  for note in noteList:
    playNote(Note[note], time, amplitude)
    
DefaultTime = 125

class NoteTimeVolume(object):
  def __init__(self, name, time=DefaultTime, volume=127):
    self.name = name
    self.time = time
    self.volume = volume

musicalTimeBase = {
   "Q":1,
   "H":2,
   "W":4,
   "E":0.5,
   "S":0.25,
   "T":0.125,
  }
  
musicalTime = {}

for name in musicalTimeBase:
  musicalTime[name] = musicalTimeBase[name]
  musicalTime[name + "."] = 1.5 * musicalTimeBase[name]
  musicalTime[name + "T"] = 2/3.0 * musicalTimeBase[name] 

def playSequence(noteList, bpm = 120):
  for note in noteList:
    time_in_ms = musicalTime[note.time]*60000/bpm
    playNote(Note[note.name], int(time_in_ms), note.volume)
    
def parseScript(noteScript):
  noteList = []
  scriptList = noteScript.split(" ")
  for item in scriptList:
    noteTime = item.split(",")
    if noteTime[0] in Note.keys():
      if len(noteTime) == 3:    
        noteList.append(NoteTimeVolume(noteTime[0],noteTime[1],int(noteTime[2])))
      elif len(noteTime) == 2:
        noteList.append(NoteTimeVolume(noteTime[0],noteTime[1]))
      else:
        noteList.append(NoteTimeVolume(noteTime[0]))
    elif noteTime[0] == ";":
      if len(noteTime) == 2:
        noteList.append(NoteTimeVolume("C0", noteTime[1], 0))
      else:
        noteList.append(NoteTimeVolume("C0", DefaultTime, 0))
  return noteList
  
def playScript(noteScript, bpm = 120):
  playSequence(parseScript(noteScript), bpm)
  
MaryHadALittleLamb = "E5,Q. D5,E C5,Q D5,Q E5,Q E5,Q E5,H D5,Q D5,Q D5,H E5,Q G5,Q G5,H E5,Q. D5,E C5,Q D5,Q E5,Q E5,Q E5,Q E5,Q D5,Q D5,Q E5,Q D5,Q C5,H"
SmokeOnTheWater = "G3,E ;,E Bb3,E ;,E C4,Q. G3,E ;,E Bb3,E ;,E Db4,E C4,H G3,E ;,E Bb3,E ;,E C4,Q. Bb3,E ;,E G3,H"

DoSoDo = "C5,Q G5,Q C5,H"

tr2 = math.pow(2, 1/12.0)
frequency = {}
frequency["C0"] = 440.0*math.pow(tr2, 3)/math.pow(2,5)
sine = {}

for name in Note:
  frequency[name] = frequency["C0"]*math.pow(tr2, Note[name])
  #sine[name] = MullSound()
  #sine[name].makeNote(frequency[name], 0.125, 1.0)

def playSineScale(startNote = "C5", steps = MAJOR_STEPS):
  sound = MullSound()
  for step in steps:
    sound.addNote(frequency[startNote]*math.pow(tr2, step), 0.125, 1.0)
  sound.play()
  return sound  

def playSineScript(noteScript, bpm = 120):
  return playSineSequence(parseScript(noteScript), bpm)
  
def playSineSequence(noteList, bpm = 120):
  sound = MullSound()
  for note in noteList:
    time_in_s = musicalTime[note.time]*60/float(bpm)
    volume = note.volume / 127
    sound.addNote(frequency[note.name], time_in_s, volume)
  sound.play()
  return sound   
