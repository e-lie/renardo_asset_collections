sccode = """
SynthDef.new(\\klank,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.01, rel=0.01, peak=1, level=0.8|
var osc, env;
sus = sus * blur;
freq = In.kr(bus, 1);
freq = [freq, freq+fmod];
sus=(sus * 1.5);
osc=Klank.ar(`[[1, 2, 3, 4], [1, 1, 1, 1], [2, 2, 2, 2]], ClipNoise.ar(0.0005).dup, freq);
env=EnvGen.ar(Env(times: (sus * 2),levels: [0, amp, 0],curve: 'lin'), doneAction: 0);
osc=(osc * env);
osc = Mix(osc) * 0.5;
osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)}).add;

"""

synth = SCInstrument(
    shortname="klank",
    fullname="Klank",
    description="Klank synth",
    code=sccode,
    arguments={}
)
