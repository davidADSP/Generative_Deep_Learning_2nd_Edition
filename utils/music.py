import os
import pickle as pkl
import music21
import numpy as np

from fractions import Fraction

def get_midi_note(sample_note, sample_duration):
    new_note = None
    
    if "TS" in sample_note:
        new_note = music21.meter.TimeSignature(sample_note.split('TS')[0])
        
    elif "major" in sample_note or "minor" in sample_note:
        tonic, mode = sample_note.split(':')
        new_note = music21.key.Key(tonic, mode)
    
    elif sample_note == "rest":
        new_note = music21.note.Rest()
        new_note.duration = music21.duration.Duration(float(Fraction(sample_duration)))
        new_note.storedInstrument = music21.instrument.Violoncello()

    elif "." in sample_note:
        notes_in_chord = sample_note.split(".")
        chord_notes = []
        for current_note in notes_in_chord:
            n = music21.note.Note(current_note)
            n.duration = music21.duration.Duration(float(Fraction(sample_duration)))
            n.storedInstrument = music21.instrument.Violoncello()
            chord_notes.append(n)
        new_note = music21.chord.Chord(chord_notes)

    elif sample_note == "rest":
        new_note = music21.note.Rest()
        new_note.duration = music21.duration.Duration(float(Fraction(sample_duration)))
        new_note.storedInstrument = music21.instrument.Violoncello()


    elif sample_note != "START":
        new_note = music21.note.Note(sample_note)
        new_note.duration = music21.duration.Duration(float(Fraction(sample_duration)))
        new_note.storedInstrument = music21.instrument.Violoncello()
        
    return new_note

def parse_midi_files(file_list, parser, seq_len):

    notes_list = []
    duration_list = []
    notes = []
    durations = []

    counter = 0

    for i, file in enumerate(file_list):
        print(i + 1, "Parsing %s" % file)
        score = parser.parse(file).chordify()
    
        notes.append("START")
        durations.append("0.0")

        for element in score.flat:
            note_name = None
            duration_name  = None

            if isinstance(element, music21.key.Key):
                note_name = str(element.tonic.name) + ':' + str(element.mode)
                duration_name = "0.0"

            elif isinstance(element, music21.meter.TimeSignature):
                note_name = str(element.ratioString) + 'TS'
                duration_name = "0.0"

            elif isinstance(element, music21.chord.Chord):
                note_name = element.pitches[-1].nameWithOctave
                duration_name = str(element.duration.quarterLength)
                
            elif isinstance(element, music21.note.Rest):
                note_name = str(element.name)
                duration_name = str(element.duration.quarterLength)
              
        
            elif isinstance(element, music21.note.Note):
                note_name = str(element.nameWithOctave)
                duration_name = str(element.duration.quarterLength)
               
            
            if note_name and duration_name:
                notes.append(note_name)
                durations.append(duration_name)

    notes_list = []
    duration_list = []
    print(f"{len(notes)} notes parsed")
    print(f"Building sequences of length {seq_len}")
    for i in range(len(notes)-seq_len):
        notes_list.append(' '.join(notes[i:(i+seq_len)]))
        duration_list.append(' '.join(durations[i:(i+seq_len)]))

    with open(os.path.join('/app/notebooks/music/bach-cello/parsed_data/', "notes"), "wb") as f:
        pkl.dump(notes_list, f)
    with open(os.path.join('/app/notebooks/music/bach-cello/parsed_data/', "durations"), "wb") as f:
        pkl.dump(duration_list, f)

    return notes_list, duration_list


def load_parsed_files():
    with open(os.path.join('/app/notebooks/music/bach-cello/parsed_data/', "notes"), "rb") as f:
        notes = pkl.load(f)
    with open(os.path.join('/app/notebooks/music/bach-cello/parsed_data/', "durations"), "rb") as f:
        durations = pkl.load(f)
    return notes, durations


### CHORALES


def binarise_output(output):
    # output is a set of scores: [batch size , steps , pitches , tracks]
    max_pitches = np.argmax(output, axis = 3)
    return max_pitches


def notes_to_midi(output, filename, n_bars, n_tracks, n_steps_per_bar):
    for score_num in range(len(output)):
        max_pitches = binarise_output(output)
        midi_note_score = max_pitches[score_num].reshape([n_bars * n_steps_per_bar, n_tracks])
        parts = music21.stream.Score()
        parts.append(music21.tempo.MetronomeMark(number= 66))
        for i in range(n_tracks):
            last_x = int(midi_note_score[:,i][0])
            s= music21.stream.Part()
            dur = 0
            for idx, x in enumerate(midi_note_score[:, i]):
                x = int(x)
                if (x != last_x or idx % 4 == 0) and idx > 0:
                    n = music21.note.Note(last_x)
                    n.duration = music21.duration.Duration(dur)
                    s.append(n)
                    dur = 0
                last_x = x
                dur = dur + 0.25
            n = music21.note.Note(last_x)
            n.duration = music21.duration.Duration(dur)
            s.append(n)
            parts.append(s)
            parts.write('midi', fp="./output/{}.midi".format(filename))