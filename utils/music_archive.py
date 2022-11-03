
import os
import pickle as pkl
from music21 import note, chord

def parse_midi_files2(file_list, parser, max_len):

    notes_list = []
    notes = []

    counter = 0

    for i, file in enumerate(file_list):
        print(i + 1, "Parsing %s" % file)
        original_score = parser.parse(file).chordify()
        
        for interval in range(4):
            score = original_score.transpose(interval)
            notes.append("START")

            for element in score.flat:
                note_name = None
                duration_name  = None

                if isinstance(element, chord.Chord):
                    note_name = ".".join(n.nameWithOctave for n in element.pitches)
                    duration_name = str(element.duration.quarterLength)
                    

                elif isinstance(element, note.Rest):
                    note_name = str(element.name)
                    duration_name = str(element.duration.quarterLength)
                
            
                elif isinstance(element, note.Note):
                    note_name = str(element.nameWithOctave)
                    duration_name = str(element.duration.quarterLength)
                
                
                if note_name and duration_name:
                    notes.append(note_name + '|' + duration_name)


    notes_list = []
    print(f"{len(notes)} notes parsed")
    print(f"Building sequences of length {max_len}")
    for i in range(len(notes)-max_len):
        notes_list.append(' '.join(notes[i:(i+max_len)]))

    with open(os.path.join('/app/notebooks/music/bach-cello/parsed_data/', "notes"), "wb") as f:
        pkl.dump(notes_list, f)

    return notes_list

    

def load_parsed_files2():
    with open(os.path.join('/app/notebooks/music/bach-cello/parsed_data/', "notes"), "rb") as f:
        notes = pkl.load(f)
    
    return notes

