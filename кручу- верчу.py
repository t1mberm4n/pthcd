import wave
import struct


def pitch_and_toss():
    source = wave.open("in.wav", mode="rb")
    dest = wave.open("out.wav", mode="wb")

    dest.setparams(source.getparams())

    frames_count = source.getnframes()

    data = struct.unpack("<" + str(frames_count) + "h",
                         source.readframes(frames_count))

    l1 = l2 = l3 = len(data) // 4
    p1 = data[l1 + l2: l1 + l2 + l3]
    p2 = data[l1 + l2 + l3:]
    p3 = data[:l1]
    p4 = data[l1: l1 + l2]
    newdata = p1 + p2 + p3 + p4

    newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata)

    dest.writeframes(newframes)
    source.close()
    dest.close()
    