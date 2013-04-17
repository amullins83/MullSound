MullSound
=========

Jython class for use with the JES package. Wraps JES media functions with object oriented tools.

Scales.py
=========

Scales is a module that utilizes the JES `playNote` function to implement a simple melody scripting
language.

Usage
-----

All of the functions and variables instantiated in `scales.py` can be utilized by moving the file to your
working directory and adding `from scales import *` to the file where you intend to use them.

Playing a Scale
---------------

To have JES play a scale, call `playScale(`_noteName_`, `_stepsList_`)`,
where _noteName_ is a note identifier and _stepsList_ is a list of intervals representing the scale.

Notes
-----

Valid note names consist of one of the letters A through G, possibly one of the symbols *b* or *#*, and a number from 0
to 10. As you may have guessed, the letter represents the musical note, the optional symbol represents flat or sharp,
respectively, and the number represents the octave. Some examples of valid notes are: *G5*, *Bb3*, *C#10*.

The lowest available note is *C0*, and the highest is *G10*. There are 128 total valid notes.

Every note designated by a *b* symbol is equivalent to one designated by *#* symbol. In other words, *Gb5* is
equivalent to *F#5*, etc. The two possible representations are both available for convenience when composing
or transcribing melodies from various keys.

Step Lists
----------

Step lists define which notes will be heard in a scale. Each element in a step list is an integer offset from the
starting note in terms of the Western 12-tone chromatic scale. Provided in the module are four example step sets,
*CHROMATIC_STEPS*, *MAJOR_STEPS*, *MINOR_STEPS*, and *HARMONIC_MINOR_STEPS*. These represent the scales of the
same name. The lists themselves are as follows:

    CHROMATIC_STEPS = range(13)
    MAJOR_STEPS = [0,2,4,5,7,9,11,12]
    MINOR_STEPS = [0,2,3,5,7,8,10,12]
    HARMONIC_MINOR_STEPS = [0,2,3,5,7,8,11,12]
    
These serve as starting points that demonstrate how to build additional scales. For example, we could compose a
mixolydian mode as follows:

    MIXOLYDIAN_STEPS = [0, 2, 4, 5, 7, 9, 10, 12]
    
Also, there is nothing preventing you from composing arbitrary step lists. For example, you could use the following
step list to arpeggiate a minor-9th chord:

    MINOR_NINTH_STEPS = [0, 3, 7, 10, 14, 10, 7, 3, 0]
    
This syntax is not intended to be used to compose melodies, as it offers no rhythm or volume variation.

Song Scripts
------------

To compose or transcribe melodies using this module, you must call the `playScript` method with a valid script string.
Valid script strings are space-separated lists of notes, which are themselves comma-separated lists consisting of at
most three parts: the note name, the duration (in musical time), and the volume (0-127). Valid note names follow the
same syntax as that for starting notes in scales as described above in the previous section. Valid musical time values
are strings of length one to three beginning with one of the following letters: "W", "H", "Q", "E", "S", or "T". These
represent whole, half, quarter, eighth, sixteenth, and thirty-second notes, respectively. A second character, if
provided, must be either a "." or "T", representing a dot or triplet, respectively.

As of April 17th, tied notes are not implemented with this scripting syntax.

Examples of song scripts for familiar melodies are provided in the string variables `MaryHadALittleLamb` and
`SmokeOnTheWater`.

Playing Scripts
---------------

Since the scripting language utilizes musical time, a number of beats per minute should be specified to establish a
tempo. The default tempo is 120 beats per minute (bpm). Therefore, you would hear a piano playing a few seconds of
Deep Purple's "Smoke on the Water" if you call `playScript(SmokeOnTheWater)` with just one argument. The default
tempo works well for this.

However, the default is painfully slow for `playScript(MaryHadALittleLamb)`, so you would probably prefer to hear
`playScript(MaryHadALittleLamb, 240)`, which establishes the tempo as 240 bpm.

Requested Features
------------------

It is my intent to implement the following features with this module:

- Tied notes to extend the possible rhythmic combinations.
- Chords / polyphony.
- File IO for scripts.
