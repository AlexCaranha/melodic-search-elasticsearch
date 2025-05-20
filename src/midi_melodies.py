from music21 import converter, stream, note
import os


def list_midi_files(dir_path) -> list[str]:
    """
    Lists all files with .mid extension in a directory.
    :param diretorio: Path of the directory to be searched.
    :return: List of full paths of the found .mid files.
    """
    arquivos_mid = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.lower().endswith(".mid"):
                arquivos_mid.append(os.path.join(root, file))

    return arquivos_mid


def extract_melody_stream(midi_file_path):
    """
    Extracts the melody from a MIDI file.
    :param midi_file_path: Path to the MIDI file.
    :return: List of notes from the melody.
    """
    from music21.note import Note  # Import here to avoid global import if not used

    midi = converter.parse(midi_file_path)
    melody_notes = [nota for nota in midi.flat.notes if isinstance(nota, Note)]
    result = stream.Stream(melody_notes)
    return result


def extract_melodic_contour(melody_stream):
    notes = [n for n in melody_stream.recurse().notes if isinstance(n, note.Note)]
    contour = []

    for i in range(1, len(notes)):
        prev = notes[i - 1]
        curr = notes[i]

        if curr.pitch.midi > prev.pitch.midi:
            contour.append("U")
        elif curr.pitch.midi < prev.pitch.midi:
            contour.append("D")
        else:
            contour.append("R")

    return "".join(contour)


def get_title_from_midi_file(midi_file):
    """Extracts the title from a midi file path."""
    base = os.path.basename(midi_file)
    if base.lower().endswith(".mid"):
        return base[:-4]
    return base


def build_melodies_from_midi_files():
    midi_files = list_midi_files(dir_path="midi_files")

    melodies = []
    for idx, midi_file_path in enumerate(midi_files):
        melody_stream = extract_melody_stream(midi_file_path)
        contour = extract_melodic_contour(melody_stream)
        title = get_title_from_midi_file(midi_file_path)

        melodies.append(
            {
                "melody_id": f"{idx+1:03}",
                "melody_title": title,
                "melody_pattern": contour,
            }
        )

    return melodies
