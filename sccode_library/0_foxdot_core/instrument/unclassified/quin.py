sccode = """
SynthDef.new(\\quin,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.01, rel=0.01, peak=1, level=0.8|
var osc, env;
sus = sus * blur;
freq = In.kr(bus, 1);
freq = [freq, freq+fmod];
freq=(freq * [1, 1.01]);
osc=(Klank.ar(`[[1, 2, 4, 2], [100, 50, 0, 10], [1, 5, 0, 1]], Impulse.ar(freq).dup, freq) / 5000);
osc=(osc * LFSaw.ar((freq * (1 + rate))));
env=EnvGen.ar(Env.perc(attackTime: 0.01,releaseTime: sus,level: amp,curve: 1), doneAction: 0);
osc=(osc * env);
osc = Mix(osc) * 0.5;
osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)}).add;

"""

synth = SCInstrument(
    shortname="quin",
    fullname="Quin",
    description="Quin synth",
    code=sccode,
    arguments={}
)
