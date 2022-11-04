import os
import pickle as pkl
import music21
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



def create_lookup_tables(elements):
    # get the distinct sets of notes and durations
    distinct_list = sorted(list(set(elements)))

    element_to_int = {element: number for number, element in enumerate(distinct_list)}
    int_to_element = {number: element for number, element in enumerate(distinct_list)}

    return element_to_int, int_to_element






def prepare_sequences(notes, durations, lookups, distincts, seq_len=32):
    """Prepare the sequences used to train the Neural Network"""

    note_to_int, int_to_note, duration_to_int, int_to_duration = lookups
    note_names, n_notes, duration_names, n_durations = distincts

    notes_network_input = []
    notes_network_output = []
    durations_network_input = []
    durations_network_output = []

    # create input sequences and the corresponding outputs
    for i in range(len(notes) - seq_len):
        notes_sequence_in = notes[i : i + seq_len]
        notes_sequence_out = notes[i + seq_len]
        notes_network_input.append([note_to_int[char] for char in notes_sequence_in])
        notes_network_output.append(note_to_int[notes_sequence_out])

        durations_sequence_in = durations[i : i + seq_len]
        durations_sequence_out = durations[i + seq_len]
        durations_network_input.append([duration_to_int[char] for char in durations_sequence_in])
        durations_network_output.append(duration_to_int[durations_sequence_out])

    n_patterns = len(notes_network_input)

    # reshape the input into a format compatible with LSTM layers
    notes_network_input = np.reshape(notes_network_input, (n_patterns, seq_len))
    durations_network_input = np.reshape(durations_network_input, (n_patterns, seq_len))
    network_input = [notes_network_input, durations_network_input]

    notes_network_output = to_categorical(notes_network_output, num_classes=n_notes)
    durations_network_output = to_categorical(durations_network_output, num_classes=n_durations)
    network_output = [notes_network_output, durations_network_output]

    return (network_input, network_output)


def sample_with_temp(preds, temperature):

    if temperature == 0:
        return np.argmax(preds)
    else:
        preds = np.log(preds) / temperature
        exp_preds = np.exp(preds)
        preds = exp_preds / np.sum(exp_preds)
        return np.random.choice(len(preds), p=preds)
