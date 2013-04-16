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

def playSequence(noteList):
  for note in noteList:
    playNote(Note[note.name], note.time, note.volume)
    
def parseScript(noteScript):
  noteList = []
  scriptList = noteScript.split(" ")
  for item in scriptList:
    noteTime = item.split(",")
    if noteTime[0] in Note.keys():
      if len(noteTime) == 3:    
        noteList.append(NoteTimeVolume(noteTime[0],int(noteTime[1]),noteTime[2]))
      elif len(noteTime) == 2:
        noteList.append(NoteTimeVolume(noteTime[0],int(noteTime[1])))
      else:
        noteList.append(NoteTimeVolume(noteTime[0]))
    elif noteTime[0] == ";":
      if len(noteTime) == 2:
        noteList.append(NoteTimeVolume("C0", int(noteTime[1]), 0))
      else:
        noteList.append(NoteTimeVolume("C0", DefaultTime, 0))
  return noteList
  
def playScript(noteScript):
  playSequence(parseScript(noteScript))
  
MaryHadALittleLamb = "E5,300 D5,100 C5,200 D5,200 E5,200 E5,200 E5,400 D5,200 D5,200 D5,400 E5,200 G5,200 G5,400 E5,300 D5,100 C5,200 D5,200 E5,200 E5,200 E5,200 E5,200 D5,200 D5,200 E5,200 D5,200 C5,400"
SmokeOnTheWater = "G3,200 ;,200 Bb3,200 ;,200 C4,600 G3,200 ;,200 Bb3,200 ;,200 Db4,200 C4,800 G3,200 ;,200 Bb3,200 ;,200 C4,600 Bb3,200 ;,200 G3,800"


