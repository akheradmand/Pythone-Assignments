import pysynth as ps
test = (('b', 5),('c', -4),('d', 1),('f', 6),
        ('a*', 2),('c', 4), ('e', 4), ('g', 4),
		('c5', -2), ('e6', 6), ('d', 2))
ps.make_wav(test, fn = "music_test.wav")
