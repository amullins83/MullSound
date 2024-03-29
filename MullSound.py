class MullSound(object):
  ampmax = 32757
  ampmin = -32757
  
  def __init__(self, oldSound=makeEmptySound(1)):
    self.sound = duplicateSound(oldSound)
    self.numSamples = getNumSamples(oldSound)
    self.rate = int(getSamplingRate(oldSound))
  
  def __getitem__(self, i):
    return getSampleObjectAt(self.sound, i)
  
  def __setitem__(self, i, sample):
    setSampleValueAt(self.sound, i, sample)
    return getSampleObjectAt(self.sound, i)
    
  def samples(self):
    return self.sound.samples
    
  def makeNote(self, frequency, time, amplitude):
    numSamples = int(time*self.rate)
    if numSamples > self.numSamples:
      self.sound = makeEmptySound(numSamples, self.rate)
      self.numSamples = numSamples
      
    for i in range(numSamples):
      setSampleValueAt(self.sound, i, math.sin(i/(1.0*self.rate)*frequency*2*math.pi)*amplitude*self.ampmax)

  def addNote(self, frequency, time, amplitude):
    newGuy = MullSound()
    newGuy.makeNote(frequency, time, amplitude)
    self.append(newGuy)

  def play(self):
    return self.sound.play()

  def append(self, otherSound):
    newSamples = self.numSamples + otherSound.numSamples
    result = makeEmptySound(newSamples, self.rate)
    for i in range(self.numSamples):
      setSampleValueAt(result, i, getSampleValueAt(self.sound, i))
    for j in range(self.numSamples,newSamples):
      setSampleValueAt(result, j, getSampleValueAt(otherSound.sound, j - self.numSamples))
    self.sound = result
    self.numSamples = newSamples
    
  def makeChord(self, notes, time, amplitude):
    pass 
    
class MullError(Exception):
     def __init__(self, value):
         self.value = value
     def __str__(self):
         return repr(self.value)
  
class testMullSound(object):
  def __init__(self):
    try:
      self.testInit()
      self.testIndex()
      self.testSetIndex()
      self.testGetSamples()
    except MullError, e:
      print "Error!",e.value
  
  def testInit(self):
    self.sound = makeEmptySound(10000, 44100)
    self.mullSound = MullSound(self.sound)
    if self.mullSound.__class__ != MullSound:
      raise MullError("testInit: failed to create new MullSound")
    
  def testIndex(self):
    sample = self.mullSound[0]
    if getSampleValue(sample) != getSampleValueAt(self.mullSound.sound, 0):
      raise MullError("testIndex: failed to get sample from mullSound[]")
    
  def testSetIndex(self):
    self.mullSound[0] = 32000
    if getSampleValueAt(self.mullSound.sound, 0) != 32000:
      raise MullError("testSetIndex: failed to set sample with mullSound[]")
    
  def testGetSamples(self):
    samples = self.mullSound.samples()
    if len(samples) != len(self.sound.samples):
      raise MullError("testGetSamples: failed to return mullSound.sound.samples: not even the same length!") 

  def testMakeNote(self):
    self.mullSound.makeNote(440, 2, 0.5)
    if getSampleValueAt(self.mullSound.sound, 25) == 0:
      raise MullError("testMakeNote: failed to make 440Hz note")
      

  
