sccode = """
SynthDef.new(\\fuzz,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.01, rel=0.01, peak=1, level=0.8|
var osc, env;
sus = sus * blur;
freq = In.kr(bus, 1);
freq = [freq, freq+fmod];
freq=(freq / 2);
amp=(amp / 6);
osc=LFSaw.ar(LFSaw.kr(freq, 0, freq, (freq * 2)));
env=EnvGen.ar(Env(times: [(sus * 0.8), 0.01],levels: [(amp * 1), (amp * 1), (amp * 0.01)],curve: 'step'), doneAction: 0);
osc=(osc * env);
osc = Mix(osc) * 0.5;
osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)}).add;

"""

synth = SCInstrument(
    shortname="fuzz",
    fullname="Fuzz",
    description="Fuzz synth",
    code=sccode,
    arguments={}
)
