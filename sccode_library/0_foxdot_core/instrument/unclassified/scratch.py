sccode = """
SynthDef.new(\\scratch,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0.04, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.01, rel=0.01, peak=1, level=0.8, depth=0.5|
var osc, env;
sus = sus * blur;
freq = In.kr(bus, 1);
freq = [freq, freq+fmod];
amp=(amp / 4);
freq=(freq * Crackle.ar(1.5));
osc=SinOsc.ar(Vibrato.kr(freq, 2, 3, rateVariation: rate, depthVariation: depth), mul: amp);
env=EnvGen.ar(Env(times: [(sus / 2), (sus / 2)],levels: [0, amp, 0],curve: 'lin'), doneAction: 0);
osc=(osc * env);
osc = Mix(osc) * 0.5;
osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)}).add;

"""

synth = SCInstrument(
    shortname="scratch",
    fullname="Scratch",
    description="Scratch synth",
    code=sccode,
    arguments={}
)
